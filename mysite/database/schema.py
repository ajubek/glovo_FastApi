from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from .models import RoleChoices, StatusChoices, CourierStatusChoices


# ---------------- USER ----------------


class UserLoginSchema(BaseModel):
    username: str
    password: str



class UserProfileInputSchema(BaseModel):
    username: str
    password: str
    phone_number: Optional[str] = None
    role: RoleChoices = RoleChoices.client


class UserProfileOutSchema(BaseModel):
    id: int
    username: str
    password: str
    phone_number: Optional[str]
    role: RoleChoices
    date_registered: date

    class Config:
        from_attributes = True


# ---------------- CATEGORY ----------------

class CategoryInputSchema(BaseModel):
    category_name: str


class CategoryOutSchema(BaseModel):
    id: int
    category_name: str

    class Config:
        from_attributes = True


# ---------------- STORE ----------------

class StoreInputSchema(BaseModel):
    category_id: int
    address: str
    store_name: str
    description: str
    contact_info: str
    owner_id: int


class StoreOutSchema(BaseModel):
    id: int
    category_id: int
    address: str
    store_name: str
    description: str
    contact_info: str
    date_registered: date
    owner_id: int

    class Config:
        from_attributes = True


# ---------------- CONTACT ----------------

class ContactInputSchema(BaseModel):
    contact_name: str
    contact_number: str
    store_id: int


class ContactOutSchema(BaseModel):
    id: int
    contact_name: str
    contact_number: str
    store_id: int

    class Config:
        from_attributes = True


# ---------------- ADDRESS ----------------

class AddressInputSchema(BaseModel):
    store_id: int
    address_name: str


class AddressOutSchema(BaseModel):
    id: int
    store_id: int
    address_name: str

    class Config:
        from_attributes = True


# ---------------- STORE MENU ----------------

class StoreMenuInputSchema(BaseModel):
    store_id: int
    menu_name: str


class StoreMenuOutSchema(BaseModel):
    id: int
    store_id: int
    menu_name: str

    class Config:
        from_attributes = True


# ---------------- PRODUCT ----------------

class ProductInputSchema(BaseModel):
    product_name: str
    product_descriptions: str
    price: int
    quantity: int = 1
    store_menu_id: int


class ProductOutSchema(BaseModel):
    id: int
    product_name: str
    product_descriptions: str
    price: int
    quantity: int
    store_menu_id: int

    class Config:
        from_attributes = True


# ---------------- ORDER ----------------

class OrderInputSchema(BaseModel):
    status: StatusChoices = StatusChoices.pending
    delivery_address: str
    courier_id: int
    client_id: int
    products_id: int


class OrderOutSchema(BaseModel):
    id: int
    status: StatusChoices
    delivery_address: str
    created_date: datetime
    courier_id: int
    client_id: int
    products_id: int

    class Config:
        from_attributes = True


# ---------------- COURIER PRODUCT ----------------

class CourierProductInputSchema(BaseModel):
    courier_status: CourierStatusChoices = CourierStatusChoices.pending
    current_orders_id: int
    user_id: int


class CourierProductOutSchema(BaseModel):
    id: int
    courier_status: CourierStatusChoices
    current_orders_id: int
    user_id: int

    class Config:
        from_attributes = True


# ---------------- REVIEW ----------------

class ReviewInputSchema(BaseModel):
    rating: int = Field(ge=1, le=5)
    text: str
    client_id: int
    store_id: int
    courier_id: int


class ReviewOutSchema(BaseModel):
    id: int
    rating: int
    text: str
    created_date: datetime
    client_id: int
    store_id: int
    courier_id: int

    class Config:
        from_attributes = True


# ---------------- REFRESH TOKEN ----------------

class RefreshTokenInputSchema(BaseModel):
    user_id: int
    token: str
    created_date: datetime


class RefreshTokenOutSchema(BaseModel):
    id: int
    user_id: int
    token: str
    created_date: datetime

    class Config:
        from_attributes = True



# ---------------- CART ----------------

class CartInputSchema(BaseModel):
    user_id: int


class CartOutSchema(BaseModel):
    id: int
    user_id: int

    class Config:
        from_attributes = True


# ---------------- CART ITEM ----------------

class CartItemInputSchema(BaseModel):
    cart_id: int
    product_id: int
    quantity: int = 1


class CartItemOutSchema(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True


# ---------------- REFRESH TOKEN ----------------

class RefreshTokenInputSchema(BaseModel):
    user_id: int
    token: str


class RefreshTokenOutSchema(BaseModel):
    id: int
    user_id: int
    token: str
    created_date: datetime

    class Config:
        from_attributes = True