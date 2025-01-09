import os
import pytest
from app.services.invoice import *
from app.services.product import *
from app.services.customer import *


def test_persist_and_load_products_from_file():
    # Arrange.
    data_path = "temp_products.jsonl"
    product_service = ProductService()
    product = product_service.add_product("Rice", 10.0)

    # Act.
    product_service.persist(data_path)

    # Assert.
    new_product_service = ProductService()
    new_product_service.load_persisted(data_path)
    new_product = new_product_service.find_product_by_id(product.id)
    assert os.path.exists(data_path)
    assert new_product.name == product.name
    assert new_product.price == product.price
    assert len(new_product_service.list_products()) == 1

    # Clean up.
    os.remove(data_path)


def test_persist_and_load_customers_from_file():
    # Arrange.
    data_path = "temp_customers.jsonl"
    customer_service = CustomerService()
    customer = customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    customer_service.persist(data_path)

    # Assert.
    new_customer_service = CustomerService()
    new_customer_service.load_persisted(data_path)
    new_customer = new_customer_service.find_customer_by_id(customer.id)
    assert os.path.exists(data_path)
    assert new_customer.name == customer.name
    assert new_customer.email == customer.email
    assert len(new_customer_service.list_customers()) == 1

    # Clean up.
    os.remove(data_path)


def test_persist_and_load_invoices_from_file():
    # Arrange.
    data_path = "temp_invoices.jsonl"
    product_service = ProductService()
    customer_service = CustomerService()
    invoice_service = InvoiceService(product_service, customer_service)
    rice = product_service.add_product("Rice", 10.0)
    alice = customer_service.add_customer("Alice", "alice@email.com")
    invoice = invoice_service.create_invoice(alice.id, [rice.id])

    # Act.
    invoice_service.persist(data_path)

    # Assert.
    new_invoice_service = InvoiceService(product_service, customer_service)
    new_invoice_service.load_persisted(data_path)
    new_invoice = new_invoice_service.find_invoice_by_id(invoice.id)
    assert os.path.exists(data_path)
    assert new_invoice.customer.name == invoice.customer.name
    assert new_invoice.products[0].name == invoice.products[0].name
    assert len(new_invoice_service.list_invoices()) == 1

    # Clean up.
    os.remove(data_path)


def test_remove_product_and_persist_change():
    # Arrange.
    data_path = "temp_products.jsonl"
    with open(data_path, "w") as file:
        file.write('{"id": 0, "name": "Arroz", "price": 11.0}')
    product_service = ProductService()
    product_service.load_persisted(data_path)

    # Act.
    product_service.delete_product(0)
    product_service.persist(data_path)

    # Assert.
    new_product_service = ProductService()
    new_product_service.load_persisted(data_path)
    with pytest.raises(Exception) as inexistent_product:
        new_product_service.find_product_by_id(0)
    assert inexistent_product.value.args[0] == "Produto não encontrado!"
    assert len(new_product_service.list_products()) == 0

    # Clean up.
    os.remove(data_path)


def test_remove_customer_and_persist_change():
    # Arrange.
    data_path = "temp_customers.jsonl"
    with open(data_path, "w") as file:
        file.write('{"id": 2, "name": "Andre", "email": "andre@email.com"}')
    customer_service = CustomerService()
    customer_service.load_persisted(data_path)

    # Act.
    customer_service.delete_customer(2)
    customer_service.persist(data_path)

    # Assert.
    new_customer_service = CustomerService()
    new_customer_service.load_persisted(data_path)
    with pytest.raises(Exception) as inexistent_customer:
        new_customer_service.find_customer_by_id(2)
    assert inexistent_customer.value.args[0] == "Cliente não encontrado!"
    assert len(new_customer_service.list_customers()) == 0


def test_remove_invoice_and_persist_change():
    # Arrange.
    data_path = "temp_invoices.jsonl"
    with open(data_path, "w") as file:
        file.write(
            '{"id": 0, "customer": {"id": 0, "name": "Bernardo", "email": "bernardo@email.com"}, "products": [{"id": 0, "name": "Arroz", "price": 11.0}], "total": 11.0, "date": "2024-12-13 17:11:32.099151"}'
        )
    product_service = ProductService()
    customer_service = CustomerService()
    invoice_service = InvoiceService(product_service, customer_service)
    invoice_service.load_persisted(data_path)

    # Act.
    invoice_service.delete_invoice(0)
    invoice_service.persist(data_path)

    # Assert.
    new_invoice_service = InvoiceService(product_service, customer_service)
    new_invoice_service.load_persisted(data_path)
    with pytest.raises(Exception) as inexistent_invoice:
        new_invoice_service.find_invoice_by_id(0)
    assert inexistent_invoice.value.args[0] == "Fatura não encontrada!"
    assert len(new_invoice_service.list_invoices()) == 0

    # Clean up.
    os.remove(data_path)
