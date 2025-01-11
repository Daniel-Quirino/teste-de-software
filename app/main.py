from services.menu import MenuService
from services.invoice import InvoiceService
from services.product import ProductService
from services.customer import CustomerService

# Declaring services.
product_service = ProductService()
customer_service = CustomerService()
menu_service = MenuService()
invoice_service = InvoiceService(product_service, customer_service)

# Loading persisted data.
product_service.load_persisted()
customer_service.load_persisted()
invoice_service.load_persisted()


def client_menu():
    while True:
        menu_service.show_header("client")
        action = input("Escolha uma opção: ")

        actions = {
            "1": lambda: menu_service.execute_with_error_handling(
                callback=lambda: customer_service.add_customer(
                    input("\nNome do cliente: "), input("E-mail do cliente: ")
                ),
                success_message="\nCliente adicionado:",
            ),
            "2": lambda: menu_service.execute_with_error_handling(
                callback=lambda: customer_service.delete_customer(
                    int(input("\nID do cliente: "))
                ),
                success_message="\nCliente removido:",
            ),
            "3": lambda: menu_service.execute_with_error_handling(
                callback=lambda: customer_service.update_customer(
                    int(input("\nID do cliente: ")),
                    input("Novo nome do cliente: "),
                    input("Novo e-mail do cliente: "),
                ),
                success_message="\nCliente atualizado:",
            ),
            "4": lambda: [
                menu_service.display_json_message("", customer)
                for customer in customer_service.list_customers()
            ],
            "5": lambda: menu_service.execute_with_error_handling(
                callback=lambda: customer_service.find_customer_by_id(
                    int(input("\nID do cliente: "))
                ),
                success_message="\nCliente encontrado:",
            ),
            "6": lambda: [
                menu_service.display_json_message("", customer)
                for customer in customer_service.find_customer_by_name(
                    input("\nEntrada: ")
                )
            ],
            "7": lambda: [
                menu_service.display_json_message("", customer)
                for customer in customer_service.find_customer_by_email(
                    input("\nEntrada: ")
                )
            ],
            "0": lambda: "break",
        }

        if actions.get(action, lambda: print("\nOpção inválida"))() == "break":
            break

        input("\nPressione ENTER para continuar...")


def product_menu():
    while True:
        menu_service.show_header("product")
        action = input("Escolha uma opção: ")

        actions = {
            "1": lambda: menu_service.execute_with_error_handling(
                callback=lambda: product_service.add_product(
                    input("\nNome do produto: "), float(input("Preço do produto: "))
                ),
                success_message="\nProduto adicionado:",
            ),
            "2": lambda: menu_service.execute_with_error_handling(
                callback=lambda: product_service.delete_product(
                    int(input("\nID do produto: "))
                ),
                success_message="\nProduto removido:",
            ),
            "3": lambda: menu_service.execute_with_error_handling(
                callback=lambda: product_service.update_product(
                    int(input("\nID do produto: ")),
                    input("Novo nome do produto: "),
                    float(input("Novo preço do produto: ")),
                ),
                success_message="\nProduto atualizado:",
            ),
            "4": lambda: [
                menu_service.display_json_message("", product)
                for product in product_service.list_products()
            ],
            "5": lambda: menu_service.execute_with_error_handling(
                callback=lambda: product_service.find_product_by_id(
                    int(input("\nID do produto: "))
                ),
                success_message="\nProduto encontrado:",
            ),
            "6": lambda: [
                menu_service.display_json_message("", product)
                for product in product_service.find_product_by_name(
                    input("\nEntrada: ")
                )
            ],
            "7": lambda: menu_service.execute_with_error_handling(
                callback=lambda: product_service.find_product_by_price(
                    float(input("\nLimite inferior: ")),
                    float(input("Limite superior: ")),
                ),
                success_message="\n=== Resultados ===",
            ),
            "0": lambda: "break",
        }

        if actions.get(action, lambda: print("\nOpção inválida"))() == "break":
            break

        input("\nPressione ENTER para continuar...")


def invoice_menu():
    while True:
        menu_service.show_header("invoice")
        action = input("Escolha uma opção: ")

        actions = {
            "1": lambda: menu_service.execute_with_error_handling(
                callback=lambda: invoice_service.create_invoice(
                    int(input("\nID do cliente: ")),
                    [
                        int(product_id)
                        for product_id in input(
                            "IDs dos produtos (separados por vírgula): "
                        ).split(",")
                        if product_id.isnumeric()
                    ],
                ),
                success_message="\nFatura criada:",
            ),
            "2": lambda: menu_service.execute_with_error_handling(
                callback=lambda: invoice_service.delete_invoice(
                    int(input("\nID da fatura: "))
                ),
                success_message="\nFatura removida:",
            ),
            "3": lambda: [
                menu_service.display_json_message("", invoice)
                for invoice in invoice_service.list_invoices()
            ],
            "4": lambda: menu_service.execute_with_error_handling(
                callback=lambda: invoice_service.find_invoice_by_id(
                    int(input("\nID da fatura: "))
                ),
                success_message="\nFatura encontrada:",
            ),
            "5": lambda: [
                menu_service.display_json_message("", invoice)
                for invoice in invoice_service.find_invoice_by_customer(
                    input("\nFiltro de nome: "), input("Filtro de e-mail: ")
                )
            ],
            "6": lambda: [
                menu_service.display_json_message("", invoice)
                for invoice in invoice_service.find_invoice_by_product(
                    input("\nFiltro de nome: "),
                    float(input("Limiar inferior de preço: ") or float("-inf")),
                    float(input("Limiar superior de preço: ") or float("inf")),
                )
            ],
            "0": lambda: "break",
        }

        if actions.get(action, lambda: print("\nOpção inválida"))() == "break":
            break

        input("\nPressione ENTER para continuar...")


while True:
    menu_service.show_header("main")

    action = input("Escolha uma opção: ")

    if action == "1":
        client_menu()
    if action == "2":
        product_menu()
    if action == "3":
        invoice_menu()
    if action == "0":
        break

# Updates persisted data.
invoice_service.persist()
customer_service.persist()
product_service.persist()
