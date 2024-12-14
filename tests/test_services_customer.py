import pytest
from app.services.customer import *


def test_add_valid_customer():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    customer = customer_service.add_customer("Alice", "alice@email.com")

    # Assert.
    assert customer.name == "Alice"
    assert customer.email == "alice@email.com"
    assert hasattr(customer, "id")


def test_add_multiple_valid_customers():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    alice = customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("Eve", "eve@email.com")

    # Assert.
    assert alice.id != bob.id != eve.id


def test_add_customer_with_empty_name():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    with pytest.raises(ValueError) as exc_info:
        customer_service.add_customer("", "alice@email.com")

    # Assert.
    assert str(exc_info.value) == "O nome não pode ser vazio."


def test_add_customer_with_empty_email():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    with pytest.raises(ValueError) as exc_info:
        customer_service.add_customer("Alice", "")

    # Assert.
    assert str(exc_info.value) == "O e-mail não pode ser vazio."


def test_add_customer_with_invalid_email():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    with pytest.raises(ValueError) as exc_info:
        customer_service.add_customer("Alice", "aliceemail.com")

    # Assert.
    assert (
        str(exc_info.value)
        == "Formato de e-mail inválido. Por favor, insira um e-mail correto."
    )


def test_add_customer_with_duplicate_email():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    with pytest.raises(ValueError) as exc_info:
        customer_service.add_customer("Bob", "alice@email.com")

    # Assert.
    assert str(exc_info.value) == "Este e-mail já está cadastrado."


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
    with pytest.raises(Exception) as inexistent_customer:
        customer_service.find_customer_by_id(alice.id + 1)

    # Assert.
    assert inexistent_customer.value.args[0] == "Cliente não encontrado!"


def test_find_customer_by_id_with_none_id():
    # Arrange.
    customer_service = CustomerService()

    # Act.
    with pytest.raises(ValueError) as exc_info:
        customer_service.find_customer_by_id(None)

    # Assert.
    assert str(exc_info.value) == "O ID do cliente não pode ser nulo."


def test_find_customer_by_name_that_matches():
    # Arrange.
    customer_service = CustomerService()
    alice = customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    result_single = customer_service.find_customer_by_name("Bob")
    result_multiple = customer_service.find_customer_by_name("e")

    # Assert.
    assert result_single == [bob]
    assert result_multiple == [alice, eve]


def test_find_customer_by_name_that_does_not_match():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    customer_service.add_customer("Bob", "bob@email.com")
    customer_service.add_customer("Eve", "eve@email.com")

    # Act.
    result = customer_service.find_customer_by_name("Gregory")

    # Assert.
    assert result == []


def test_find_customer_by_email_that_matches():
    # Arrange.
    customer_service = CustomerService()
    alice = customer_service.add_customer("Alice", "alice@gmail.com")
    bob = customer_service.add_customer("Bob", "bob@gmail.com")
    eve = customer_service.add_customer("Eve", "eve@hotmail.com")

    # Act.
    result_single = customer_service.find_customer_by_email("hotmail")
    result_multiple = customer_service.find_customer_by_email("gmail")

    # Assert.
    assert result_single == [eve]
    assert result_multiple == [alice, bob]


def test_find_customer_by_email_that_does_not_match():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@gmail.com")
    customer_service.add_customer("Bob", "bob@gmail.com")
    customer_service.add_customer("Eve", "eve@hotmail.com")

    # Act.
    result = customer_service.find_customer_by_email("yahoo")

    # Assert.
    assert result == []


def test_update_customer_that_is_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    customer_service.add_customer("Bob", "bob@email.com")
    eve = customer_service.add_customer("New Eve", "eve@email.com")

    # Act.
    new_eve = customer_service.update_customer(eve.id, "New Eve", "new_eve@email.com")

    # Assert.
    assert new_eve.name == "New Eve"
    assert new_eve.email == "new_eve@email.com"
    assert new_eve.id == eve.id


def test_update_customer_that_is_not_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")

    # Act.
    with pytest.raises(Exception) as inexistent_customer:
        customer_service.update_customer(bob.id + 1, "Eve", "eve@email.com")

    # Assert.
    assert inexistent_customer.value.args[0] == "Cliente não encontrado!"


def test_update_customer_with_invalid_parameters():
    # Arrange.
    customer_service = CustomerService()
    alice = customer_service.add_customer("Alice", "alice@email.com")

    # Act.
    with pytest.raises(Exception) as invalid_name:
        customer_service.update_customer(alice.id, "", "alice@email.com")
    with pytest.raises(Exception) as invalid_email:
        customer_service.update_customer(alice.id, "Alice", "")

    # Assert.
    assert invalid_name.value.args[0] == "Nome e/ou e-mail inválido(s)!"
    assert invalid_email.value.args[0] == "Nome e/ou e-mail inválido(s)!"


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


def test_delete_customer_that_is_not_on_list():
    # Arrange.
    customer_service = CustomerService()
    customer_service.add_customer("Alice", "alice@email.com")
    bob = customer_service.add_customer("Bob", "bob@email.com")

    # Act.
    with pytest.raises(Exception) as inexistent_customer:
        customer_service.delete_customer(bob.id + 1)

    # Assert.
    assert inexistent_customer.value.args[0] == "Cliente não encontrado!"
