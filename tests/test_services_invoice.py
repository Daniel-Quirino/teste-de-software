import pytest
from app.services.invoice import *
from app.services.product import *
from app.services.customer import *


# Arrange.
@pytest.fixture()
def product_service():
    return ProductService()


# Arrange.
@pytest.fixture()
def customer_service():
    return CustomerService()


# Arrange.
@pytest.fixture()
def invoice_service(product_service, customer_service):
    return InvoiceService(product_service, customer_service)


def test_calculate_total(invoice_service):
    # Arrange.
    products = [Product(0, "Rice", 11.0), Product(1, "Beans", 12.0)]

    # Act.
    total = invoice_service._calculate_total(products)

    # Assert.
    assert total == 23.0


def test_calculate_total_empty_list(invoice_service):
    # Act.
    total = invoice_service._calculate_total([])

    # Assert.
    assert total == 0.0


def test_create_valid_invoice(product_service, customer_service, invoice_service):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    invoice = invoice_service.create_invoice(alice.id, [rice.id, beans.id])

    # Assert.
    assert invoice.customer == alice
    assert invoice.products == [rice, beans]
    assert hasattr(invoice, "id")
    assert hasattr(invoice, "total")
    assert hasattr(invoice, "date")


def test_create_multiple_valid_invoices(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    meat = product_service.add_product("Meat", 13.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    alice_invoice = invoice_service.create_invoice(alice.id, [rice.id, beans.id])
    bob_invoice = invoice_service.create_invoice(bob.id, [rice.id, beans.id, meat.id])
    eve_invoice = invoice_service.create_invoice(eve.id, [meat.id])

    # Assert.
    assert alice_invoice.id != bob_invoice.id != eve_invoice.id


def test_create_invalid_invoice(product_service, customer_service, invoice_service):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    with pytest.raises(Exception) as invalid_customer:
        invoice_service.create_invoice(alice.id + 1, [rice.id])
    with pytest.raises(Exception) as invalid_product:
        invoice_service.create_invoice(alice.id, [rice.id + 1])

    # Assert.
    assert invalid_customer.value.args[0] == "Cliente não encontrado!"
    assert invalid_product.value.args[0] == "Produto não encontrado!"


def test_list_invoices(product_service, customer_service, invoice_service):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    meat = product_service.add_product("Meat", 13.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("Eve", "eve@email.com")
    invoice_service.create_invoice(alice.id, [rice.id, beans.id])
    invoice_service.create_invoice(bob.id, [meat.id])
    invoice_service.create_invoice(eve.id, [])

    # Act.
    invoices = invoice_service.list_invoices()

    # Assert.
    assert len(invoices) == 3
    assert invoices[0].customer == alice
    assert invoices[1].products == [meat]


def test_find_invoice_by_id_that_is_on_list(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    invoice = invoice_service.create_invoice(alice.id, [rice.id])

    # Act.
    found_invoice = invoice_service.find_invoice_by_id(invoice.id)

    # Assert.
    assert found_invoice == invoice


def test_find_invoice_by_id_that_is_not_on_list(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    invoice = invoice_service.create_invoice(alice.id, [rice.id])

    # Act.
    with pytest.raises(Exception) as inexistent_invoice:
        invoice_service.find_invoice_by_id(invoice.id + 1)

    # Assert.
    assert inexistent_invoice.value.args[0] == "Fatura não encontrada!"


def test_find_invoice_by_customer_with_parameters_that_match(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    alice = customer_service.add_customer("Alice", "alice@gmail.com")
    bob = customer_service.add_customer("Bob", "bob@hotmail.com")
    invoice_alice = invoice_service.create_invoice(alice.id, [rice.id, beans.id])
    invoice_bob = invoice_service.create_invoice(bob.id, [beans.id])

    # Act.
    result_name = invoice_service.find_invoice_by_customer(name="Alice")
    result_email = invoice_service.find_invoice_by_customer(email="hotmail")

    # Assert.
    assert result_name == [invoice_alice]
    assert result_email == [invoice_bob]


def test_find_invoice_by_customer_with_parameters_that_do_not_match(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    beans = product_service.add_product("Beans", 12.0)
    alice = customer_service.add_customer("Alice", "alice@gmail.com")
    bob = customer_service.add_customer("Bob", "bob@hotmail.com")
    invoice_service.create_invoice(alice.id, [rice.id, beans.id])
    invoice_service.create_invoice(bob.id, [beans.id])

    # Act.
    result = invoice_service.find_invoice_by_customer(name="Alice", email="hotmail")

    # Assert.
    assert result == []


def test_delete_invoice_that_is_on_list(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    invoice = invoice_service.create_invoice(alice.id, [rice.id])

    # Act.
    deleted_invoice = invoice_service.delete_invoice(invoice.id)

    # Assert.
    assert deleted_invoice == invoice


def test_delete_invoice_that_is_not_on_list(
    product_service, customer_service, invoice_service
):
    # Arrange.
    rice = product_service.add_product("Rice", 11.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    invoice = invoice_service.create_invoice(alice.id, [rice.id])

    # Act.
    with pytest.raises(Exception) as inexistent_invoice:
        invoice_service.delete_invoice(invoice.id + 1)

    # Assert.
    assert inexistent_invoice.value.args[0] == "Fatura não encontrada!"
