import os
import json


class MenuService:
    def __init__(self):
        self.headers = {
            "client": "\n=== Ações sobre Clientes ===\n1. Adicionar\n2. Remover\n3. Atualizar\n4. Listar\n5. Buscar por ID\n6. Buscar por nome\n7. Buscar por e-mail\n0. Voltar",
            "product": "\n=== Ações sobre Produtos ===\n1. Adicionar\n2. Remover\n3. Atualizar\n4. Listar\n5. Buscar por ID\n6. Buscar por nome\n7. Buscar por preço\n0. Voltar",
            "invoice": "\n=== Ações sobre Faturas ===\n1. Adicionar\n2. Remover\n3. Listar\n4. Buscar por ID\n5. Buscar por cliente\n6. Buscar por produto\n0. Voltar",
            "main": "\n=== Gerenciador de Faturas ===\n1. Clientes\n2. Produtos\n3. Faturas\n0. Sair",
        }

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def show_header(self, menu_type):
        self.clear_screen()
        print(self.headers.get(menu_type, "\n=== Menu Não Encontrado ==="))

    def display_json_message(self, message, obj):
        print(message, json.dumps(obj, default=lambda o: o.__dict__, skipkeys=True))

    def execute_with_error_handling(
        self, callback, success_message, error_message="\nErro:"
    ):
        try:
            result = callback()  # Execute the callback function
            self.display_json_message(success_message, result)
        except Exception as e:
            print(error_message, e)
