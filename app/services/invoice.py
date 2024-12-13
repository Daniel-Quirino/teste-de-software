from .product import *
from .customer import *
from datetime import datetime


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
        """ self._base_id = -1

        # Reads persisted data.
        file = open("./app/data/invoices.jsonl", "r")
        for line in file:
            invoice = Invoice(**json.loads(line))
            self._invoices.append(invoice)
            if invoice.id > self._base_id:
                self._base_id = invoice.id
                self._id_counter = self._base_id + 1
        file.close()

    def __del__(self):
        # Persists the data.
        file = open("./app/data/invoices.jsonl", "a")
        for invoice in self._invoices:
            if invoice.id > self._base_id:
                file.write(
                    json.dumps(invoice, default=lambda o: o.__dict__, skipkeys=True)
                    + "\n"
                )
        file.close() """

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

        return invoice

    def list_invoices(self):
        """
        Returns the list of stored invoices.
        """
        return self._invoices

    def find_invoice_by_id(self, invoice_id: int):
        """
        Returns the invoice with the given id if on the list.

        Raises Exception() if invoice is not found.
        """
        for invoice in self._invoices:
            if invoice.id == invoice_id:
                return invoice
        raise Exception("Fatura não encontrada!")

    def delete_invoice(self, invoice_id: int):
        """
        Returns the deleted invoice if successful.

        Raises Exception() if invoice is not found.
        """
        for i in range(len(self._invoices)):
            if self._invoices[i].id == invoice_id:
                return self._invoices.pop(i)
        raise Exception("Fatura não encontrada!")
