import pytest
from app.services.product import *


def test_add_valid_product():
    # Arrange.
    product_service = ProductService()

    # Act.
    product = product_service.add_product("Rice", 11.0)

    # Assert.
    assert product.name == "Rice"
    assert product.price == 11.0
    assert hasattr(product, "id")


def test_add_multiple_valid_products():
    # Arrange.
    product_service = ProductService()

    # Act.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    meat = product_service.add_product("Meat", 13.0)

    # Assert.
    assert rice.id != beans.id != meat.id


def test_add_invalid_product():
    # Arrange.
    product_service = ProductService()

    # Act.
    with pytest.raises(Exception) as invalid_name:
        product_service.add_product("", 11.0)
    with pytest.raises(Exception) as invalid_price:
        product_service.add_product("Rice", -11.0)

    # Assert.
    assert invalid_name.value.args[0] == "Nome e/ou preço inválido(s)!"
    assert invalid_price.value.args[0] == "Nome e/ou preço inválido(s)!"


def test_list_products():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    product_service.add_product("Beans", 12.0)
    product_service.add_product("Meat", 13.0)

    # Act.
    products = product_service.list_products()

    # Assert.
    assert len(products) == 3
    assert products[1].name == "Beans"
    assert products[2].price == 13.0


def test_find_product_by_id_that_is_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    product_service.add_product("Meat", 13.0)

    # Act.
    product = product_service.find_product_by_id(beans.id)

    # Assert.
    assert product == beans


def test_find_product_by_id_that_is_not_on_list():
    # Arrange.
    product_service = ProductService()
    rice = product_service.add_product("Rice", 11.0)

    # Act.
    with pytest.raises(Exception) as inexistent_product:
        product_service.find_product_by_id(rice.id + 1)

    # Assert.
    assert inexistent_product.value.args[0] == "Produto não encontrado!"


def test_update_product_that_is_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    product_service.add_product("Beans", 12.0)
    meat = product_service.add_product("Meat", 13.0)

    # Act.
    new_meat = product_service.update_product(meat.id, "New Meat", 15.0)

    # Assert.
    assert new_meat.name == "New Meat"
    assert new_meat.price == 15.0
    assert new_meat.id == meat.id


def test_update_product_that_is_not_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)

    # Act.
    with pytest.raises(Exception) as inexistent_customer:
        product_service.update_product(beans.id + 1, "Meat", 15.0)

    # Assert.
    assert inexistent_customer.value.args[0] == "Produto não encontrado!"


def test_update_product_with_invalid_parameters():
    # Arrange.
    product_service = ProductService()
    rice = product_service.add_product("Rice", 11.0)

    # Act.
    with pytest.raises(Exception) as invalid_name:
        product_service.update_product(rice.id, "", 11.0)
    with pytest.raises(Exception) as invalid_price:
        product_service.update_product(rice.id, "Rice", -11.0)

    # Assert.
    assert invalid_name.value.args[0] == "Nome e/ou preço inválido(s)!"
    assert invalid_price.value.args[0] == "Nome e/ou preço inválido(s)!"


def test_delete_product_that_is_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    product_service.add_product("Meat", 13.0)

    # Act.
    deleted_beans = product_service.delete_product(beans.id)

    # Assert.
    assert deleted_beans == beans


def test_delete_product_that_is_not_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)

    # Act.
    with pytest.raises(Exception) as deleted_product:
        product_service.delete_product(beans.id + 1)

    # Assert.
    assert deleted_product.value.args[0] == "Produto não encontrado!"
