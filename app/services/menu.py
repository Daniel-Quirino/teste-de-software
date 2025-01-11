import os
import json
import logging


class MenuService:
    def __init__(self):
        logging.basicConfig(
            filename="example.log",
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )

        self.headers = {
            "client": "\n=== Ações sobre Clientes ===\n1. Adicionar\n2. Remover\n3. Atualizar\n4. Listar\n5. Buscar por ID\n6. Buscar por nome\n7. Buscar por e-mail\n0. Voltar",
            "product": "\n=== Ações sobre Produtos ===\n1. Adicionar\n2. Remover\n3. Atualizar\n4. Listar\n5. Buscar por ID\n6. Buscar por nome\n7. Buscar por preço\n0. Voltar",
            "invoice": "\n=== Ações sobre Faturas ===\n1. Adicionar\n2. Remover\n3. Listar\n4. Buscar por ID\n5. Buscar por cliente\n6. Buscar por produto\n0. Voltar",
            "main": "\n=== Gerenciador de Faturas ===\n1. Clientes\n2. Produtos\n3. Faturas\n0. Sair",
        }

        logging.log(logging.INFO, "Menu - Inicializando")

    def clear_screen(self):
        logging.log(logging.INFO, "Menu - Limpar tela")

        os.system("cls" if os.name == "nt" else "clear")

    def show_header(self, menu_type):
        logging.log(logging.INFO, "Menu - Mostrar Cabeçalho")

        self.clear_screen()
        print(self.headers.get(menu_type, "\n=== Menu Não Encontrado ==="))

    def display_json_message(self, message, obj):
        logging.log(logging.INFO, "Menu - Mostrar mensagem em JSON")

        print(message, json.dumps(obj, default=lambda o: o.__dict__, skipkeys=True))

    def execute_with_error_handling(
        self, callback, success_message, error_message="\nErro:"
    ):
        logging.log(logging.INFO, "Menu - Execução")

        try:
            result = callback()  # Execute the callback function
            self.display_json_message(success_message, result)
        except Exception as e:
            print(error_message, str(e))
