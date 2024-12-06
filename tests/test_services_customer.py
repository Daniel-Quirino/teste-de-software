from app.services.customer import *


def test_initialize_empty_customer_service():
    # Arrange/Act.
    customer_service = CustomerService()

    # Assert.
    assert len(customer_service.customers) == 0


def test_add_valid_customer():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    customer = customer_service.add_customer("Alice", "alice@email.com")

    # Assert.
    assert customer.name == "Alice"
    assert customer.email == "alice@email.com"
    assert len(customer_service.customers) == 1


def test_add_multiple_valid_customers():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    alice = customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("Eve", "eve@email.com")

    # Assert.
    assert alice.id != bob.id != eve.id
    assert len(customer_service.customers) == 3


def test_add_invalid_customer():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    invalid_name = customer_service.add_customer("", "alice@email.com")
    invalid_email = customer_service.add_customer("Alice", "")

    # Assert.
    assert invalid_name == invalid_email == None
    assert len(customer_service.customers) == 0


def test_list_customers():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    customer_service.add_customer("Bob", "bob@email.com")
    customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    customers = customer_service.list_customers()

    # Assert.
    assert len(customers) == 3
    assert customers[1].name == "Bob"
    assert customers[2].email == "eve@email.com"


def test_find_customer_by_id_that_is_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    customer = customer_service.find_customer_by_id(bob.id)

    # Assert.
    assert customer == bob


def test_find_customer_by_id_that_is_not_on_list():
    # Arrange.
    customer_service = CustomerService()
    alice = customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    customer = customer_service.find_customer_by_id(alice.id + 1)

    # Assert.
    assert customer == None


def test_update_customer_that_is_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    new_eve = customer_service.update_customer(eve.id, eve.name, "eve2@email.com")

    # Assert.
    assert new_eve.name == "Eve"
    assert new_eve.email == "eve2@email.com"


def test_update_customer_that_is_not_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")

    # Act.
    new_eve = customer_service.update_customer(bob.id + 1, "Eve", "eve2@email.com")

    # Assert.
    assert new_eve == None


def test_update_customer_with_invalid_parameters():
    # Arrange.
    customer_service = CustomerService()
    alice = customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    invalid_name = customer_service.update_customer(alice.id, "", "alice@email.com")
    invalid_email = customer_service.update_customer(alice.id, "Alice", "")

    # Assert.
    assert invalid_name == invalid_email == None


def test_delete_customer_that_is_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    deleted_bob = customer_service.delete_customer(bob.id)

    # Assert.
    assert deleted_bob == bob
    assert len(customer_service.customers) == 2


def test_delete_customer_that_is_not_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")

    # Act.
    deleted_customer = customer_service.delete_customer(bob.id + 1)

    # Assert.
    assert deleted_customer == None
    assert len(customer_service.customers) == 2
