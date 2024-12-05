from app.services.product import *


def test_initialize_empty_product_service():
    # Arrange/Act.
    product_service = ProductService()

    # Assert.
    assert len(product_service.products) == 0


def test_add_valid_product():
    # Arrange.
    product_service = ProductService()

    # Act.
    product = product_service.add_product("Rice", 11.0)

    # Assert.
    assert product.name == "Rice"
    assert product.price == 11.0
    assert len(product_service.products) == 1


def test_add_multiple_valid_products():
    # Arrange.
    product_service = ProductService()

    # Act.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    meat = product_service.add_product("Meat", 13.0)

    # Assert.
    assert rice.id != beans.id != meat.id
    assert len(product_service.products) == 3


def test_add_invalid_product():
    # Arrange.
    product_service = ProductService()

    # Act.
    invalid_name = product_service.add_product("", 11.0)
    invalid_price = product_service.add_product("Rice", -11.0)

    # Assert.
    assert invalid_name == invalid_price == None
    assert len(product_service.products) == 0


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
    product = product_service.find_product_by_id(rice.id + 1)

    # Assert.
    assert product == None


def test_update_product_that_is_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    product_service.add_product("Beans", 12.0)
    meat = product_service.add_product("Meat", 13.0)

    # Act.
    new_meat = product_service.update_product(meat.id, meat.name, 15.0)

    # Assert.
    assert new_meat.name == "Meat"
    assert new_meat.price == 15.0


def test_update_product_that_is_not_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)

    # Act.
    new_meat = product_service.update_product(beans.id + 1, "Meat", 15.0)

    # Assert.
    assert new_meat == None


def test_update_product_with_invalid_parameters():
    # Arrange.
    product_service = ProductService()
    rice = product_service.add_product("Rice", 11.0)

    # Act.
    invalid_name = product_service.update_product(rice.id, "", 11.0)
    invalid_price = product_service.update_product(rice.id, "Rice", -11.0)

    # Assert.
    assert invalid_name == invalid_price == None


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
    assert len(product_service.products) == 2


def test_delete_product_that_is_not_on_list():
    # Arrange.
    product_service = ProductService()
    product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)

    # Act.
    deleted_product = product_service.delete_product(beans.id + 1)

    # Assert.
    assert deleted_product == None
    assert len(product_service.products) == 2
