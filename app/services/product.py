class Product:
    """
    Defines a product.
    """

    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price


class ProductService:
    """
    Class for manipulating the available products.
    """

    def __init__(self):
        self._products = []
        self._id_counter = 0

    def add_product(self, name: str, price: float):
        """
        Appens a new product to the list of products.

        Raises Exception() if parameters are invalid.
        """
        # Checks if product parameters are valid.
        if price <= 0 or name == "":
            raise Exception("Nome e/ou preço inválido(s)!")

        product = Product(self._id_counter, name, price)
        self._products.append(product)
        self._id_counter += 1

        return product

    def list_products(self):
        """
        Returns the stored list of products.
        """
        return self._products

    def find_product_by_id(self, product_id: int):
        """
        Returns the product with the given id if on the list.

        Raises Exception() if product is not found.
        """
        for product in self._products:
            if product.id == product_id:
                return product
        raise Exception("Produto não encontrado!")

    def update_product(self, product_id: int, name: str, price: float):
        """
        Returns the new product if successfull.

        Raises Exception() if parameters are invalid or product is not found.
        """
        for i in range(len(self._products)):
            if self._products[i].id == product_id:
                # Checks if product parameters are valid.
                if price <= 0 or name == "":
                    raise Exception("Nome e/ou preço inválido(s)!")

                self._products[i] = Product(product_id, name, price)
                return self._products[i]
        raise Exception("Produto não encontrado!")

    def delete_product(self, product_id: int):
        """
        Returns the deleted product if successful.

        Raises Exception() if product is not found.
        """
        for i in range(len(self._products)):
            if self._products[i].id == product_id:
                return self._products.pop(i)
        raise Exception("Produto não encontrado!")
