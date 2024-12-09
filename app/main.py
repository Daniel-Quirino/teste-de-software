from services.invoice import InvoiceService

invoice_service = InvoiceService()

print("=== Gerenciador de Faturas ===")
print("1. Adicionar Cliente")
print("2. Listar Clientes")
print("3. Adicionar Produto")
print("4. Listar Produtos")
print("5. Criar Fatura")
print("6. Listar Faturas")
print("7. Sair")

input = input("Escolha uma opção: ")

match input:
    case "1":
        