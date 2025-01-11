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
