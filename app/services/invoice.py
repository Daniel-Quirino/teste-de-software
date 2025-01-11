from .product import *
from .customer import *
from datetime import datetime

import logging

class Invoice:
    """
    Defines an invoice.
    """

    def __init__(
        self,
        id: int,
        customer: Customer,
        products: list[Product],
        total: float,
        date: str,
    ):
        self.id = id
        self.customer = customer
        self.products = products
        self.total = total
        self.date = date

        logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class InvoiceService:
    """
    Class for manipulating invoices.
    """

    def __init__(
        self, product_service: ProductService, customer_service: CustomerService
    ):
        self.product_service = product_service
        self.customer_service = customer_service

        self._invoices = []
        self._id_counter = 0

    def load_persisted(self, path: str = "./app/data/invoices.jsonl"):
        """
        Reads persisted data.
        """
        logging.log(logging.INFO, "Carregar Faturas")

        self._id_counter = -1

        file = open(path, "a+")
        file.seek(0)
        for line in file:
            invoice = Invoice(**json.loads(line))
            invoice.customer = Customer(**invoice.customer)
            invoice.products = [Product(**product) for product in invoice.products]
            self._invoices.append(invoice)
            if invoice.id > self._id_counter:
                self._id_counter = invoice.id
        file.close()

        self._id_counter += 1
        
        logging.log(logging.INFO, "Carregou as faturas ")


    def persist(self, path: str = "./app/data/invoices.jsonl"):
        """
        Persists the data.
        """
        logging.log(logging.INFO, "Armazenar as faturas ")

        file = open(path, "w")
        for invoice in self._invoices:
            file.write(
                json.dumps(invoice, default=lambda o: o.__dict__, skipkeys=True) + "\n"
            )
        file.close()

        logging.log(logging.INFO, "Armazenou as faturas")


    def _calculate_total(self, products: list[Product]):
        """
        Receives a list of products and calculates the total price.
        """
        total = 0.0
        for product in products:
            total += product.price

        return total

    def create_invoice(self, customer_id: int, product_ids: list[int]):
        """
        Receives a customer id and a set of product ids,
        calculates the total cost and saves as an invoice.
        """
        logging.log(logging.INFO, "Criar fatura")


        customer = self.customer_service.find_customer_by_id(customer_id)

        products = []
        for product_id in product_ids:
            product = self.product_service.find_product_by_id(product_id)
            products.append(product)

        total = self._calculate_total(products)

        date = str(datetime.now())

        invoice = Invoice(self._id_counter, customer, products, total, date)
        self._invoices.append(invoice)
        self._id_counter += 1

        logging.log(logging.INFO, "Fatura Criada")

        return invoice

    def list_invoices(self):
        """
        Returns the list of stored invoices.
        """
        logging.log(logging.INFO, "Listar Faturas")

        return self._invoices

    def find_invoice_by_id(self, invoice_id: int):
        """
        Returns the invoice with the given id if on the list.

        Raises Exception() if invoice is not found.
        """

        logging.log(logging.INFO, "Encontrar fatura pelo ID")


        for invoice in self._invoices:
            if invoice.id == invoice_id:
                return invoice
        logging.log(logging.INFO, "Fatura não encontrada!")
        raise Exception("Fatura não encontrada!")

    def find_invoice_by_customer(self, name: str = "", email: str = ""):
        """
        Returns a list of invoices whose customers match the specified parameters.

        Returns an empty list otherwise.
        """

        logging.log(logging.INFO, "Encontrar fatura pelo cliente")

        results = []
        for invoice in self._invoices:
            customer = invoice.customer
            # Skips if a name is given but is not in the customer's name.
            if name and (name.lower() not in customer.name.lower()):
                continue
            # Skips if an email is given but is not in the customer's email.
            if email and (email.lower() not in customer.email.lower()):
                continue
            results.append(invoice)
        return results

    def find_invoice_by_product(
        self,
        name: str = "",
        lower_bound: float = float("-inf"),
        upper_bound: float = float("inf"),
    ):
        """
        Returns a list of invoices whose products match the specified parameters.
        An invoice is returned if it contains at least one product that matches the parameters.

        Returns an empty list otherwise.
        """

        logging.log(logging.INFO, "Encontrar fatura pelo produto")

        results = []
        for invoice in self._invoices:
            for product in invoice.products:
                # Skips if a name is given but is not in the customer's name.
                if name and (name.lower() not in product.name.lower()):
                    continue
                # Skips if bounds are given but the product is not within them.
                if (lower_bound != float("-inf")) and (product.price < lower_bound):
                    continue
                if (upper_bound != float("inf")) and (product.price > upper_bound):
                    continue
                results.append(invoice)
                break
        return results

    def delete_invoice(self, invoice_id: int):
        """
        Returns the deleted invoice if successful.

        Raises Exception() if invoice is not found.
        """

        logging.log(logging.INFO, "Deletar Fatuara")

        for i in range(len(self._invoices)):
            if self._invoices[i].id == invoice_id:
                return self._invoices.pop(i)
        
        logging.log(logging.INFO, "Fatura não encontrada!")
        raise Exception("Fatura não encontrada!")
