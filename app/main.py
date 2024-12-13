import os
import json
from services.invoice import InvoiceService
from services.product import ProductService
from services.customer import CustomerService

# Declaring services.
product_service = ProductService()
customer_service = CustomerService()
invoice_service = InvoiceService(product_service, customer_service)


# Declaring menus.
def client_menu():
    while True:
        # Clears console.
        os.system("cls" if os.name == "nt" else "clear")

        # Displays action menu.
        print("\n=== Ações sobre Clientes ===")
        print("1. Adicionar")
        print("2. Remover")
        print("3. Atualizar")
        print("4. Listar")
        print("5. Buscar por ID")
        print("6. Buscar por nome")
        print("7. Buscar por e-mail")
        print("0. Voltar")

        action = input("Escolha uma opção: ")
        match action:
            case "1":
                name = input("\nNome do cliente: ")
                email = input("E-mail do cliente: ")

                try:
                    customer = customer_service.add_customer(name, email)
                    print(
                        "\nCliente adicionado:",
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "2":
                id = int(input("\nID do cliente: "))

                try:
                    customer = customer_service.delete_customer(id)
                    print(
                        "\nCliente removido:",
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "3":
                id = int(input("\nID do cliente: "))
                new_name = input("Novo nome do cliente: ")
                new_email = input("Novo e-mail do cliente: ")

                try:
                    customer = customer_service.update_customer(id, new_name, new_email)
                    print(
                        "\nCliente atualizado:",
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "4":
                customers = customer_service.list_customers()
                print("\n=== Clientes ===")
                for customer in customers:
                    print(
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        )
                    )
                input("\nPressione ENTER para continuar...")

            case "5":
                id = int(input("\nID do cliente: "))

                try:
                    customer = customer_service.find_customer_by_id(id)
                    print(
                        "\nCliente encontrado:",
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "6":
                search_string = input("\nEntrada: ")
                results = customer_service.find_customer_by_name(search_string)
                print("\n=== Resultados ===")
                for customer in results:
                    print(
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        )
                    )
                input("\nPressione ENTER para continuar...")

            case "7":
                search_string = input("\nEntrada: ")
                results = customer_service.find_customer_by_email(search_string)
                print("\n=== Resultados ===")
                for customer in results:
                    print(
                        json.dumps(
                            customer, default=lambda o: o.__dict__, skipkeys=True
                        )
                    )
                input("\nPressione ENTER para continuar...")

            case "0":
                break


def product_menu():
    while True:
        # Clears console.
        os.system("cls" if os.name == "nt" else "clear")

        # Displays action menu.
        print("\n=== Ações sobre Produtos ===")
        print("1. Adicionar")
        print("2. Remover")
        print("3. Atualizar")
        print("4. Listar")
        print("0. Voltar")

        action = input("Escolha uma opção: ")
        match action:
            case "1":
                name = input("\nNome do produto: ")
                price = float(input("Preço do produto: "))

                try:
                    product = product_service.add_product(name, price)
                    print(
                        "\nProduto adicionado:",
                        json.dumps(
                            product, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "2":
                id = int(input("\nID do produto: "))

                try:
                    product = product_service.delete_product(id)
                    print(
                        "\nProduto removido:",
                        json.dumps(
                            product, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "3":
                id = int(input("\nID do produto: "))
                new_name = input("Novo nome do produto: ")
                new_price = float(input("Novo preço do produto: "))

                try:
                    product = product_service.update_product(id, new_name, new_price)
                    print(
                        "\nProduto atualizado:",
                        json.dumps(
                            product, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "4":
                products = product_service.list_products()
                print("\n=== Produtos ===")
                for product in products:
                    print(
                        json.dumps(product, default=lambda o: o.__dict__, skipkeys=True)
                    )
                input("\nPressione ENTER para continuar...")

            case "0":
                break


def invoice_menu():
    while True:
        # Clears console.
        os.system("cls" if os.name == "nt" else "clear")

        # Displays action menu.
        print("\n=== Ações sobre Faturas ===")
        print("1. Adicionar")
        print("2. Remover")
        print("3. Listar")
        print("0. Voltar")

        action = input("Escolha uma opção: ")
        match action:
            case "1":
                customer_id = int(input("\nID do cliente: "))
                product_ids = [
                    int(product_id)
                    for product_id in input(
                        "IDs dos produtos (separados por vírgula): "
                    ).split(",")
                    if product_id.isnumeric()
                ]

                try:
                    invoice = invoice_service.create_invoice(customer_id, product_ids)
                    print(
                        "\nFatura criada:",
                        json.dumps(
                            invoice, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "2":
                id = int(input("\nID da fatura: "))

                try:
                    invoice = invoice_service.delete_invoice(id)
                    print(
                        "\nFatura removida:",
                        json.dumps(
                            invoice, default=lambda o: o.__dict__, skipkeys=True
                        ),
                    )

                except Exception as e:
                    print("\n" + e.args[0])

                input("\nPressione ENTER para continuar...")

            case "3":
                invoices = invoice_service.list_invoices()
                print("\n=== Faturas ===")
                for invoice in invoices:
                    print(
                        json.dumps(invoice, default=lambda o: o.__dict__, skipkeys=True)
                    )
                input("\nPressione ENTER para continuar...")

            case "0":
                break


while True:
    # Clears console.
    os.system("cls" if os.name == "nt" else "clear")

    # Displays action menu.
    print("\n=== Gerenciador de Faturas ===")
    print("1. Clientes")
    print("2. Produtos")
    print("3. Faturas")
    print("0. Sair")

    action = input("Escolha uma opção: ")
    match action:
        case "1":
            client_menu()

        case "2":
            product_menu()

        case "3":
            invoice_menu()

        case "0":
            break

# Cleanup.
invoice_service = None
customer_service = None
product_service = None
