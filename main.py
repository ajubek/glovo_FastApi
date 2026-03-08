from fastapi import FastAPI
from mysite.database.db import engine, Base
from mysite.api import (auth, UserProfile, Category, Store, Contact, Address, StoreMenu, Product, Order, CourierProduct, Review, Cart, CartItem, RefreshToken)
from mysite.admin.setup import setup_admin
import uvicorn
glovo_app = FastAPI(
    title="Glovo API"
)


Base.metadata.create_all(bind=engine)

glovo_app.include_router(auth.auth_router)
glovo_app.include_router(UserProfile.user_router)
glovo_app.include_router(Category.category_router)
glovo_app.include_router(Store.store_router)
glovo_app.include_router(Contact.contact_router)
glovo_app.include_router(Address.address_router)
glovo_app.include_router(StoreMenu.store_menu_router)
glovo_app.include_router(Product.product_router)
glovo_app.include_router(Order.order_router)
glovo_app.include_router(CourierProduct.courier_product_router)
glovo_app.include_router(Review.review_router)
glovo_app.include_router(Cart.cart_router)
glovo_app.include_router(CartItem.cart_item_router)
glovo_app.include_router(RefreshToken.refresh_token_router)
setup_admin(glovo_app)



if __name__ == '__main__':
    uvicorn.run(glovo_app, host='127.0.0.1', port=8000)
