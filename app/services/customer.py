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
        self.customers = []
        self.id_counter = 0

    def add_customer(self, name: str, email: str):
        """
        Appens a new customer to the list of customers.
        """
        # Checks if customer parameters are valid.
        if email == "" or name == "":
            return None

        customer = Customer(self.id_counter, name, email)
        self.customers.append(customer)
        self.id_counter += 1

        return customer

    def list_customers(self):
        """
        Returns the stored list of customers.
        """
        return self.customers

    def find_customer_by_id(self, customer_id: int):
        """
        Returns the customer with the given id if on the list.
        Returns a None object otherwise.
        """
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def update_customer(self, customer_id: int, name: str, email: str):
        """
        Returns the new customer if successfull.
        Returns a None object otherwise.
        """
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                # Checks if customer parameters are valid.
                if email == "" or name == "":
                    return None

                self.customers[i] = Customer(customer_id, name, email)
                return self.customers[i]
        return None

    def delete_customer(self, customer_id: int):
        """
        Returns the deleted customer if successful.
        Returns a None object otherwise.
        """
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                return self.customers.pop(i)
        return None
