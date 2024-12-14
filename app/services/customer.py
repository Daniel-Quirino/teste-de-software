import json
import re


class Customer:
    """
    Defines a customer.
    """

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email


class CustomerService:
    """
    Class for manipulating the existent customers.
    """

    def __init__(self):
        self._customers = []
        self._id_counter = 0
        self._base_id = -1

    def load_persisted(self):
        """
        Reads persisted data.
        """
        file = open("./app/data/customers.jsonl", "r")
        for line in file:
            customer = Customer(**json.loads(line))
            self._customers.append(customer)
            if customer.id > self._base_id:
                self._base_id = customer.id
                self._id_counter = self._base_id + 1
        file.close()

    def persist(self):
        """
        Persists the data.
        """
        file = open("./app/data/customers.jsonl", "a")
        for customer in self._customers:
            if customer.id > self._base_id:
                file.write(
                    json.dumps(customer, default=lambda o: o.__dict__, skipkeys=True)
                    + "\n"
                )
        file.close()

    def add_customer(self, name: str, email: str):
        """
        Appends a new customer to the list of customers.

        Raises specific exceptions if parameters are invalid or email is not in valid format.
        """

        if name == "":
            raise ValueError("O nome não pode ser vazio.")

        if email == "":
            raise ValueError("O e-mail não pode ser vazio.")

        # Regex for validating an Email
        email_regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        if not re.match(email_regex, email):
            raise ValueError(
                "Formato de e-mail inválido. Por favor, insira um e-mail correto."
            )

        if any(customer.email == email for customer in self._customers):
            raise ValueError("Este e-mail já está cadastrado.")

        customer = Customer(self._id_counter, name, email)
        self._customers.append(customer)
        self._id_counter += 1

        return customer

    def list_customers(self):
        """
        Returns the stored list of customers.
        """
        return self._customers

    def find_customer_by_id(self, customer_id: int):
        """
        Returns the customer with the given id if on the list.

        Raises Exception() if customer is not found.
        """

        if customer_id is None:
            raise ValueError("O ID do cliente não pode ser nulo.")

        for customer in self._customers:
            if customer.id == customer_id:
                return customer
        raise Exception("Cliente não encontrado!")

    def find_customer_by_name(self, search_string: str):
        """
        Receive a 'search string' and returns customers whose names match it.

        Returns an empty list if there are no matches.
        """
        results = []
        for customer in self._customers:
            if search_string.lower() in customer.name.lower():
                results.append(customer)
        return results

    def find_customer_by_email(self, search_string: str):
        """
        Receive a 'search string' and returns customers whose e-mails match it.

        Returns an empty list if there are no matches.
        """
        results = []
        for customer in self._customers:
            if search_string.lower() in customer.email.lower():
                results.append(customer)
        return results

    def update_customer(self, customer_id: int, name: str, email: str):
        """
        Returns the new customer if successfull.

        Raises Exception() if parameters are invalid or customer is not found.
        """
        for i in range(len(self._customers)):
            if self._customers[i].id == customer_id:
                # Checks if customer parameters are valid.
                if email == "" or name == "":
                    raise Exception("Nome e/ou e-mail inválido(s)!")

                self._customers[i] = Customer(customer_id, name, email)
                return self._customers[i]
        raise Exception("Cliente não encontrado!")

    def delete_customer(self, customer_id: int):
        """
        Returns the deleted customer if successful.

        Raises Exception() if customer is not found.
        """
        for i in range(len(self._customers)):
            if self._customers[i].id == customer_id:
                return self._customers.pop(i)
        raise Exception("Cliente não encontrado!")
