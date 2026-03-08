from sqladmin import ModelView
from mysite.database.models import (
    UserProfile, Category, Store, Contact, Address,
    StoreMenu, Product, Order, CourierProduct,
    Review, Cart, CartItem, RefreshToken
)


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [
        UserProfile.id,
        UserProfile.username,
        UserProfile.phone_number,
        UserProfile.role,
        UserProfile.date_registered
    ]


class CategoryAdmin(ModelView, model=Category):
    column_list = [
        Category.id,
        Category.category_name
    ]


class StoreAdmin(ModelView, model=Store):
    column_list = [
        Store.id,
        Store.store_name,
        Store.address,
        Store.category_id,
        Store.owner_id,
        Store.date_registered
    ]


class ContactAdmin(ModelView, model=Contact):
    column_list = [
        Contact.id,
        Contact.contact_name,
        Contact.contact_number,
        Contact.store_id
    ]


class AddressAdmin(ModelView, model=Address):
    column_list = [
        Address.id,
        Address.address_name,
        Address.store_id
    ]


class StoreMenuAdmin(ModelView, model=StoreMenu):
    column_list = [
        StoreMenu.id,
        StoreMenu.menu_name,
        StoreMenu.store_id
    ]


class ProductAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.product_name,
        Product.price,
        Product.quantity,
        Product.store_menu_id
    ]


class OrderAdmin(ModelView, model=Order):
    column_list = [
        Order.id,
        Order.status,
        Order.delivery_address,
        Order.courier_id,
        Order.client_id,
        Order.products_id,
        Order.created_date
    ]


class CourierProductAdmin(ModelView, model=CourierProduct):
    column_list = [
        CourierProduct.id,
        CourierProduct.courier_status,
        CourierProduct.current_orders_id,
        CourierProduct.user_id
    ]


class ReviewAdmin(ModelView, model=Review):
    column_list = [
        Review.id,
        Review.rating,
        Review.text,
        Review.client_id,
        Review.store_id,
        Review.courier_id,
        Review.created_date
    ]


class CartAdmin(ModelView, model=Cart):
    column_list = [
        Cart.id,
        Cart.user_id
    ]


class CartItemAdmin(ModelView, model=CartItem):
    column_list = [
        CartItem.id,
        CartItem.cart_id,
        CartItem.product_id,
        CartItem.quantity
    ]


class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [
        RefreshToken.id,
        RefreshToken.user_id,
        RefreshToken.token,
        RefreshToken.created_date
    ]