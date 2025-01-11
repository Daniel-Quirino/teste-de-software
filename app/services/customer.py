import re
import json
import logging


class Customer:
    """
    Defines a customer.
    """

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

        logging.basicConfig(
            filename="example.log",
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )

        logging.log(logging.INFO, "Customer - Inicializando")

    def __repr__(self):
        logging.log(logging.INFO, "Customer - Visualizando Cliente")

        return f"Customer(id={self.id}, name='{self.name}', email='{self.email}')"


class CustomerService:
    """
    Class for manipulating the existent customers.
    """

    def __init__(self):
        self.__customers = []
        self.__id_counter = 0

        logging.basicConfig(
            filename="example.log",
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )

        logging.log(logging.INFO, "Customer Service - Inicializando")

    def __validate_email(self, email: str):
        logging.log(logging.INFO, "Customer Service - Validando Email")

        email_regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(email_regex, email):
            raise ValueError(
                "Formato de e-mail inválido. Por favor, insira um e-mail correto."
            )

    def __next_id(self):
        current_id = self.__id_counter
        self.__id_counter += 1
        return current_id

    def load_persisted(self, path: str = "./app/data/customers.jsonl"):
        """
        Reads persisted data.
        """
        logging.log(
            logging.INFO, "Customer Service - Carregar dados armazenados de clientes"
        )

        with open(path, "a+") as file:
            file.seek(0)
            for line in file:
                customer = Customer(**json.loads(line))
                self.__customers.append(customer)
                if customer.id > self.__id_counter:
                    self.__id_counter = customer.id
        self.__id_counter += 1

    def persist(self, path: str = "./app/data/customers.jsonl"):
        """
        Persists the data.
        """
        logging.log(logging.INFO, "Customer Service - Persistir dados - cliente")

        with open(path, "w") as file:
            for customer in self.__customers:
                file.write(
                    json.dumps(customer, default=lambda o: o.__dict__, skipkeys=True)
                    + "\n"
                )

    def add_customer(self, name: str, email: str):
        """
        Appends a new customer to the list of customers.

        Raises specific exceptions if parameters are invalid or email is not in valid format.
        """
        if not name:
            logging.log(logging.INFO, "Customer Service - O nome não pode ser vazio")
            raise ValueError("O nome não pode ser vazio.")

        if not email:
            logging.log(logging.INFO, "Customer Service - O e-mail não pode ser vazio.")
            raise ValueError("O e-mail não pode ser vazio.")

        self.__validate_email(email)

        if any(customer.email == email for customer in self.__customers):
            logging.log(logging.INFO, "Customer Service - O e-mail não pode ser vazio.")
            raise ValueError("Este e-mail já está cadastrado.")
        new_customer = Customer(self.__next_id(), name, email)
        self.__customers.append(new_customer)

        return new_customer

    def list_customers(self):
        """
        Returns the stored list of customers.
        """
        logging.log(logging.INFO, "Customer Service - Listar clientes")
        return self.__customers

    def find_customer_by_id(self, customer_id: int):
        """
        Returns the customer with the given id if on the list.

        Raises Exception() if customer is not found.
        """
        logging.log(logging.INFO, "Customer Service - Encontrar Cliente Pelo ID")

        if customer_id is None:
            logging.log(
                logging.INFO, "Customer Service - O ID do cliente não pode ser nulo."
            )
            raise ValueError("O ID do cliente não pode ser nulo.")

        for customer in self.__customers:
            if customer.id == customer_id:
                return customer

        logging.log(logging.INFO, "Customer Service - Cliente não encontrado!")
        raise Exception("Cliente não encontrado!")

    def find_customer_by_name(self, search_string: str):
        """
        Receive a 'search string' and returns customers whose names match it.

        Returns an empty list if there are no matches.
        """
        logging.log(logging.INFO, "Customer Service - Encontrar Cliente pelo nome")
        return [
            customer
            for customer in self.__customers
            if search_string.lower() in customer.name.lower()
        ]

    def find_customer_by_email(self, search_string: str):
        """
        Receive a 'search string' and returns customers whose e-mails match it.

        Returns an empty list if there are no matches.
        """
        logging.log(logging.INFO, "Customer Service - Encontrar Cliente pelo email")
        return [
            customer
            for customer in self.__customers
            if search_string.lower() in customer.email.lower()
        ]

    def update_customer(self, customer_id: int, name: str, email: str):
        """
        Returns the new customer if successfull.

        Raises Exception() if parameters are invalid or customer is not found.
        """
        logging.log(logging.INFO, "Customer Service - Atualizar cliente")

        customer = self.find_customer_by_id(customer_id)
        if not name or not email:
            raise ValueError("Nome e/ou e-mail inválido(s)!")
        self.__validate_email(email)
        customer.name = name
        customer.email = email
        return customer

    def delete_customer(self, customer_id: int):
        """
        Returns the deleted customer if successful.

        Raises Exception() if customer is not found.
        """
        logging.log(logging.INFO, "Customer Service - Deletar Cliente")

        customer = self.find_customer_by_id(customer_id)
        self.__customers.remove(customer)

        logging.log(logging.INFO, "Customer Service - Cliente deletado")

        return customer


# Example of usage
service = CustomerService()
service.add_customer("John Doe", "john.doe@example.com")
print(service.list_customers())
