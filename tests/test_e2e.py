import re
import os
import json
import pytest
import pexpect


@pytest.mark.skipif(condition=(os.name == "nt"), reason="Not compatible with Windows")
def test_add_new_client_and_remove_it_through_cli():
    # Initializes the app and checks if the menu screen is reached.
    app = pexpect.spawn("python3 app/main.py")
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )

    # Chooses the client operations and checks if the client screen is reached.
    app.sendline("1")
    app.expect(
        re.compile(r"=== Ações sobre Clientes ==="),
        timeout=3,
    )

    # Chooses to create a client and checks if a client was created.
    app.sendline("1")
    app.sendline("CLITest")
    app.sendline("cli@test.com")
    app.expect(
        re.compile(
            r'Cliente adicionado: \{"id": ., "name": "CLITest", "email": "cli@test\.com"\}'
        ),
        timeout=3,
    )

    # Recovers the client id from the output.
    client_id = str(
        json.loads(
            re.search(
                r'\{"id": ., "name": .*, "email": .*\}',
                str(app.match.group()),
            ).group()
        )["id"]
    )
    app.sendline("")

    # Chooses to remove a client and checks if the client was removed.
    app.sendline("2")
    app.sendline(client_id)
    app.expect(
        re.compile(
            r'Cliente removido: \{"id": ., "name": "CLITest", "email": "cli@test\.com"\}'
        ),
        timeout=3,
    )
    app.sendline("")

    # Closes the application.
    app.sendline("0")
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )
    app.sendline("0")
    app.sendline("")
    app.close()


@pytest.mark.skipif(condition=(os.name == "nt"), reason="Not compatible with Windows")
def test_add_new_product_and_remove_it_through_cli():
    # Initializes the app and checks if the main menu screen is reached.
    app = pexpect.spawn("python3 app/main.py")
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )

    # Navigates to the product operations menu.
    app.sendline("2")
    app.expect(
        re.compile(r"=== Ações sobre Produtos ==="),
        timeout=3,
    )

    # Adds a new product and checks if the product was added.
    app.sendline("1") 
    app.sendline("ProdutoTeste")
    app.sendline("123.45")
    app.expect(
        re.compile(
            r'Produto adicionado: \{"id": ., "name": "ProdutoTeste", "price": 123.45\}'
        ),
        timeout=3,
    )

    # Extracts the product ID from the output for later deletion.
    product_id = str(
        json.loads(
            re.search(
                r'\{"id": ., "name": "ProdutoTeste", "price": 123.45\}',
                str(app.match.group())
            ).group()
        )["id"]
    )
    app.sendline("")

    # Removes the product and checks if it was removed successfully.
    app.sendline("2") 
    app.sendline(product_id)
    app.expect(
        re.compile(
            r'Produto removido: \{"id": ., "name": "ProdutoTeste", "price": 123.45\}'
        ),
        timeout=3,
    )
    app.sendline("")

    # Exits the product menu.
    app.sendline("0")
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )
    app.sendline("0")  # Exits the application.
    app.close()


@pytest.mark.skipif(condition=(os.name == "nt"), reason="Not compatible with Windows")
def test_update_existing_client_through_cli():
    # Initializes the app and checks if the main menu screen is reached.
    app = pexpect.spawn("python3 app/main.py")
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )

    # Navigates to the client operations menu.
    app.sendline("1")  
    app.expect(
        re.compile(r"=== Ações sobre Clientes ==="),
        timeout=3,
    )

    # Adds a new client to update later.
    app.sendline("1") 
    app.sendline("ClienteInicial")
    app.sendline("initial@client.com")
    app.expect(
        re.compile(
            r'Cliente adicionado: \{"id": ., "name": "ClienteInicial", "email": "initial@client.com"\}'
        ),
        timeout=3,
    )

    # Extracts the client ID from the output.
    client_id = str(
        json.loads(
            re.search(
                r'\{"id": ., "name": .*, "email": .*\}',
                str(app.match.group())
            ).group()
        )["id"]
    )
    app.sendline("")

    # Updates the previously added client.
    app.sendline("3") 
    app.sendline(client_id)
    app.sendline("ClienteAtualizado")
    app.sendline("updated@client.com")
    app.expect(
        re.compile(
            r'Cliente atualizado: \{"id": ., "name": "ClienteAtualizado", "email": "updated@client.com"\}'
        ),
        timeout=3,
    )
    app.sendline("")

    # Exits the client menu.
    app.sendline("0") 
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )
    app.sendline("0")  # Exits the application.
    app.close()


@pytest.mark.skipif(condition=(os.name == "nt"), reason="Not compatible with Windows")
def test_find_product_by_price_range():
    app = pexpect.spawn("python3 app/main.py")
    app.expect(
        re.compile(r"=== Gerenciador de Faturas ==="),
        timeout=3,
    )

    # Navigate to product menu
    app.sendline("2")
    app.expect(
        re.compile(r"=== Ações sobre Produtos ==="),
        timeout=3,
    )

    # Search for products by price range
    app.sendline("7")
    app.sendline("100")  # Lower price limit
    app.sendline("200")  # Upper price limit
    app.expect(r'\n=== Resultados ===', timeout=3)
    app.sendline("")

    # Close the application
    app.sendline("0")
    app.sendline("0")
    app.close()