from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, ForeignKey,  Text,  DateTime
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import date, datetime



class RoleChoices(str,PyEnum):
    client = "client"
    owner = "owner"
    courier = "courier"



class StatusChoices(str, PyEnum):
    pending='pending'
    canceled='canceled'
    delivered='delivered'

import enum

class CourierStatusChoices(str, enum.Enum):
    pending = "pending"
    delivered = "delivered"
    cancelled = "cancelled"




class UserProfile(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    role: Mapped[str] = mapped_column(Enum(RoleChoices), default=RoleChoices.client)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)

    owner: Mapped[List['Store']] = relationship(back_populates='owner', cascade='all, delete-orphan')

    courier_orders: Mapped[List['Order']] = relationship(
        back_populates='courier',
        cascade='all, delete-orphan',
        foreign_keys='Order.courier_id'
    )

    client_order: Mapped[List['Order']] = relationship(
        back_populates='client',
        cascade='all, delete-orphan',
        foreign_keys='Order.client_id'
    )

    user_couriers_product: Mapped[List['CourierProduct']] = relationship(
        back_populates='user_couriers_product',
        cascade='all, delete-orphan'
    )

    client_review: Mapped[List['Review']] = relationship(
        back_populates='client_review',
        cascade='all, delete-orphan'
    )

    cart_user: Mapped[Optional['Cart']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )

    user_token: Mapped[List['RefreshToken']] = relationship(
        back_populates='token_user',
        cascade='all, delete-orphan'
    )


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_name:Mapped[str] = mapped_column(String,unique=True)
    category:Mapped[List['Store']] = relationship(back_populates='category', cascade='all, delete-orphan')

    def __str__(self):
        return self.category_name


class Store(Base):
    __tablename__ = 'store'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    address:Mapped[str] = mapped_column(String)
    store_name:Mapped[str] = mapped_column(String,unique=True)
    description: Mapped[str] = mapped_column(Text)
    contact_info:Mapped[str] = mapped_column(Text)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))


    owner:Mapped[UserProfile] = relationship(back_populates='owner')
    category:Mapped[Category] = relationship(back_populates='category')
    store_contact:Mapped[List['Contact']] = relationship(back_populates='store', cascade='all , delete-orphan')
    store_address:Mapped[List['Address']] = relationship(back_populates='store_address',  cascade='all , delete-orphan')
    store_menu:Mapped[List['StoreMenu']] = relationship(back_populates='store_menu',  cascade='all , delete-orphan')
    store_review:Mapped[List['Review']] = relationship(back_populates='store_review', cascade='all, delete-orphan')





    def __str__(self):
        return self.store_name



class Contact(Base):
    __tablename__ = 'Contact'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    contact_name:Mapped[str] = mapped_column(String(30))
    contact_number:Mapped[str] = mapped_column(String, unique=True)
    store_id:Mapped[int] = mapped_column(Integer, ForeignKey('store.id'))
    store:Mapped[Store] = relationship(back_populates='store_contact')


    def __str__(self):
        return f'{self.contact_name},{self.contact_number}'


class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    store_id: Mapped[int] = mapped_column(Integer, ForeignKey('store.id'))
    address_name:Mapped[str] = mapped_column(String(50))

    store_address:Mapped[Store] = relationship(back_populates='store_address')



    def __str__(self):
        return self.address_name



class StoreMenu(Base):
    __tablename__ = 'store_menu'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    store_id:Mapped[int] = mapped_column(Integer, ForeignKey('store.id'))
    menu_name:Mapped[str] = mapped_column(String(50),unique=True)

    store_menu: Mapped[Store] = relationship(back_populates='store_menu')
    product:Mapped[List['Product']] = relationship(back_populates='store_menu' , cascade='all, delete-orphan')



    def __str__(self):
        return self.menu_name



class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_name:Mapped[str] = mapped_column(String(40))
    product_descriptions:Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)
    quantity:Mapped[int] = mapped_column(Integer,default=1)

    store_menu_id:Mapped[int] = mapped_column(ForeignKey('store_menu.id'))
    store_menu:Mapped[StoreMenu] = relationship(back_populates='product')
    order_product:Mapped[List['Order']] = relationship(back_populates='products', cascade='all , delete-orphan')


    def __str__(self):
        return self.product_name



class Order(Base):
    __tablename__ = 'order'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(Enum(StatusChoices), default=StatusChoices.pending)
    delivery_address: Mapped[str] = mapped_column(Text)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.today)

    courier_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    courier: Mapped[UserProfile] = relationship(
        back_populates='courier_orders',
        foreign_keys=[courier_id]
    )

    client_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    client: Mapped[UserProfile] = relationship(
        back_populates='client_order',
        foreign_keys=[client_id]
    )

    products_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    products: Mapped[Product] = relationship(back_populates='order_product')

    courier_order: Mapped[List['CourierProduct']] = relationship(
        back_populates='current_orders',
        cascade='all, delete-orphan'
    )




    def __str__(self):
        return f'{self.client},{self.products},{self.status}'

class CourierProduct(Base):
    __tablename__ = 'courier_product'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    courier_status:Mapped[str] = mapped_column(Enum(CourierStatusChoices), default=CourierStatusChoices.pending)
    current_orders_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
    current_orders:Mapped[Order] = relationship(back_populates='courier_order')
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    user_couriers_product:Mapped[UserProfile] = relationship(back_populates='user_couriers_product')
    courier_review:Mapped[List['Review']] = relationship(back_populates='courier_review', cascade='all , delete-orphan')


    def __str__(self):
        return f'{self.user_couriers_product},{self.courier_status}'



class Review (Base):
    __tablename__ = 'review'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    rating: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(Text)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.today)
    client_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    client_review: Mapped[UserProfile] = relationship(back_populates='client_review')
    store_id:Mapped[int] = mapped_column(ForeignKey('store.id'))
    store_review:Mapped[Store] = relationship(back_populates='store_review')
    courier_id:Mapped[int] = mapped_column(ForeignKey('courier_product.id'))
    courier_review:Mapped[CourierProduct] = relationship(back_populates='courier_review')

    def __str__(self):
        return f'{self.client_review},{self.rating}'



class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id:  Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    user: Mapped['UserProfile'] = relationship(UserProfile, back_populates='cart_user')
    items: Mapped[List['CartItem']] = relationship('CartItem', back_populates='cart',
                                                   cascade='all, delete-orphan')


class CartItem(Base):
    __tablename__ = 'cartitem'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey('cart.id'))
    cart: Mapped['Cart'] = relationship(Cart, back_populates='items')
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped['Product'] = relationship(Product)
    quantity: Mapped[int] = mapped_column(Integer, default=1)



class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')



    def __repr__(self):
        return f'{self.token}'