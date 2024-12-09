import json
from services.invoice import InvoiceService
from services.product import ProductService
from services.customer import CustomerService

product_service = ProductService()
customer_service = CustomerService()
invoice_service = InvoiceService(product_service, customer_service)

while True:
    # Displays action menu.
    print("\n=== Gerenciador de Faturas ===")
    print("1. Adicionar Cliente")
    print("2. Listar Clientes")
    print("3. Adicionar Produto")
    print("4. Listar Produtos")
    print("5. Criar Fatura")
    print("6. Listar Faturas")
    print("7. Sair")

    action = input("Escolha uma opção: ")

    # Matches the chosen action.
    match action:
        case "1":
            name = input("Nome do cliente: ")
            email = input("E-mail do cliente: ")
            customer = customer_service.add_customer(name, email)

            print(
                "Cliente adicionado:",
                json.dumps(customer, default=lambda o: o.__dict__, skipkeys=True),
            )

        case "2":
            customers = customer_service.list_customers()
            for customer in customers:
                print(json.dumps(customer, default=lambda o: o.__dict__, skipkeys=True))

        case "3":
            name = input("Nome do produto: ")
            price = float(input("Preço do produto: "))
            product = product_service.add_product(name, price)

            print(
                "Produto adicionado:",
                json.dumps(product, default=lambda o: o.__dict__, skipkeys=True),
            )

        case "4":
            products = product_service.list_products()
            for product in products:
                print(json.dumps(product, default=lambda o: o.__dict__, skipkeys=True))

        case "5":
            customer_id = int(input("ID do cliente: "))
            product_ids = [
                int(product_id)
                for product_id in input(
                    "IDs dos produtos (separados por vírgula): "
                ).split(",")
                if product_id.isnumeric()
            ]
            invoice = invoice_service.create_invoice(customer_id, product_ids)

            print(
                "Fatura criada:",
                json.dumps(invoice, default=lambda o: o.__dict__, skipkeys=True),
            )

        case "6":
            invoices = invoice_service.list_invoices()
            for invoice in invoices:
                print(json.dumps(invoice, default=lambda o: o.__dict__, skipkeys=True))

        case "7":
            break
