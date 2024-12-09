from services.invoice import InvoiceService
from services.product import ProductService
from services.customer import CustomerService

product_service = ProductService()
customer_service = CustomerService()
invoice_service = InvoiceService(product_service, customer_service)

print("=== Gerenciador de Faturas ===")
print("1. Adicionar Cliente")
print("2. Listar Clientes")
print("3. Adicionar Produto")
print("4. Listar Produtos")
print("5. Criar Fatura")
print("6. Listar Faturas")
print("7. Sair")

action = input("Escolha uma opção: ")

match action:
    case "1":
        name = input("Nome do cliente: ")
        email = input("E-mail do cliente: ")
        customer = customer_service.add_customer(name, email)

        print("Cliente adicionado:", str(customer))
