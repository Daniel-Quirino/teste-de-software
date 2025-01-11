import pytest
from unittest.mock import patch, MagicMock
from app.services.menu import MenuService
import os


@pytest.fixture
def menu():
    return MenuService()


def test_clear_screen(menu):
    # Arrange.
    with patch("os.system") as mock_system:

        # Act.
        menu.clear_screen()

        # Assert.
        mock_system.assert_called_once_with("cls" if os.name == "nt" else "clear")


def test_execute_with_error_handling_failure(menu):
    # Arrange.
    mock_callback = MagicMock(side_effect=Exception("Falha na operação"))
    error_message = "\nErro:"

    with patch("builtins.print") as mock_print:
        # Act.
        menu.execute_with_error_handling(
            mock_callback, "\nOperação deveria ter sucesso:", error_message
        )

        # Assert.
        mock_callback.assert_called_once()
        mock_print.assert_called_with(
            error_message, str(Exception("Falha na operação"))
        )


def test_show_header_client(menu):
    with patch("builtins.print") as mock_print:
        # Act.
        menu.show_header("client")

        # Assert.
        mock_print.assert_called_with(
            "\n=== Ações sobre Clientes ===\n1. Adicionar\n2. Remover\n3. Atualizar\n4. Listar\n5. Buscar por ID\n6. Buscar por nome\n7. Buscar por e-mail\n0. Voltar"
        )


def test_show_header_invalid(menu):
    with patch("builtins.print") as mock_print:
        # Act.
        menu.show_header("invalid")

        # Assert.
        mock_print.assert_called_with("\n=== Menu Não Encontrado ===")


def test_display_json_message(menu):
    with patch("builtins.print") as mock_print:
        # Arrange.
        message = "\nProduto removido:"
        obj = {"id": 1, "name": "Produto 1", "price": 100.0}
        expected_json = '{"id": 1, "name": "Produto 1", "price": 100.0}'

        # Act.
        menu.display_json_message(message, obj)

        # Assert.
        mock_print.assert_called_once_with(message, expected_json)


def test_execute_with_error_handling_success(menu):
    # Arrange.
    mock_callback = MagicMock(return_value={"id": 1, "name": "Test"})
    success_message = "\nOperation successful:"

    with patch("builtins.print") as mock_print:
        # Act.
        menu.execute_with_error_handling(mock_callback, success_message)

        # Assert.
        mock_callback.assert_called_once()
        mock_print.assert_any_call(success_message, '{"id": 1, "name": "Test"}')
