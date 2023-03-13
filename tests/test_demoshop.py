import os
import allure
from dotenv import load_dotenv
from selene import have, be
from selene.support.shared import browser

load_dotenv()

LOGIN = os.getenv("DEMOSHOP_LOGIN")
WEB_URL = os.getenv("DEMOSHOP_WEB_URL")

browser.config.base_url = WEB_URL


def test_add_product_to_cart(demoshop_browser, demoshop):
    with allure.step('Open start page'):
        browser.open("")

    with allure.step('Add product to cart'):
        demoshop.post(
            "/addproducttocart/details/72/1",
            data={
                "product_attribute_72_5_18": 53,
                "product_attribute_72_6_19": 54,
                "product_attribute_72_3_20": 57,
                "addtocart_72.EnteredQuantity": 1,
            }
        )

    with allure.step('Check product in cart'):
        browser.element(".header-links #topcartlink").click()
        browser.element(".product-name").should(have.text('Build your own cheap computer'))

    with allure.step('Remove products from the cart'):
        browser.element('.remove-from-cart > [name = "removefromcart"]').click()
        browser.element('.update-cart-button').click()
        browser.element('div.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_delete_product_from_the_cart(demoshop_browser, demoshop):
    with allure.step('Open start page'):
        browser.open("")

    with allure.step('Add product to cart'):
        demoshop.post(
            "/addproducttocart/details/72/1",
            data={
                "product_attribute_72_5_18": 53,
                "product_attribute_72_6_19": 54,
                "product_attribute_72_3_20": 57,
                "addtocart_72.EnteredQuantity": 1,
            }
        )

    with allure.step('Delete product from the cart'):
        browser.element(".header-links #topcartlink").click()
        browser.element('.remove-from-cart > [name = "removefromcart"]').click()
        browser.element('.update-cart-button').click()
        browser.element(".order-summary-content").should(have.text('Your Shopping Cart is empty!'))


def test_add_product_to_wishlist(demoshop_browser, demoshop):
    with allure.step('Open start page'):
        browser.open("")

    with allure.step('Add product to wishlist'):
        demoshop.post(
            '/addproducttocart/details/43/2',
            data={
                'addtocart_43.EnteredQuantity': 1
            }
        )

    with allure.step('Check product in wishlist'):
        browser.element('.header-links .ico-wishlist').click()
        browser.element('.cart-item-row .product > [href="/smartphone"]').should(have.text('Smartphone'))

    with allure.step('Remove products from the wishlist'):
        browser.element('.remove-from-cart > [name = "removefromcart"]').click()
        browser.element('.update-wishlist-button').click()
        browser.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_the_wishlist(demoshop_browser, demoshop):
    with allure.step('Open start page'):
        browser.open("")

    with allure.step('Add product to wishlist'):
        demoshop.post(
            '/addproducttocart/details/43/2',
            data={
                'addtocart_43.EnteredQuantity': 1
            }
        )

    with allure.step('Delete product from the wishlist'):
        browser.element('.header-links .ico-wishlist').click()
        browser.element('.remove-from-cart > [name = "removefromcart"]').click()
        browser.element('.update-wishlist-button').click()
        browser.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_logout(demoshop_browser):
    with allure.step('Open start page'):
        browser.open("")

    with allure.step('Verify successful authorization'):
        browser.element(".account").should(have.text(LOGIN))

    with allure.step('Logout'):
        browser.element('.ico-logout').click()
        browser.element('.ico-login').should(be.visible)

