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

    def add_customer(self, name: str, email: str):
        """
        Appens a new customer to the list of customers.

        Raises Exception() if parameters are invalid.
        """
        # Checks if customer parameters are valid.
        if email == "" or name == "":
            raise Exception("Nome e/ou e-mail inválido(s)!")

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
