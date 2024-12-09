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
        """
        # Checks if product parameters are valid.
        if price <= 0 or name == "":
            return None

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
        Returns a None object otherwise.
        """
        for product in self._products:
            if product.id == product_id:
                return product
        return None

    def update_product(self, product_id: int, name: str, price: float):
        """
        Returns the new product if successfull.
        Returns a None object otherwise.
        """
        for i in range(len(self._products)):
            if self._products[i].id == product_id:
                # Checks if product parameters are valid.
                if price <= 0 or name == "":
                    return None

                self._products[i] = Product(product_id, name, price)
                return self._products[i]
        return None

    def delete_product(self, product_id: int):
        """
        Returns the deleted product if successful.
        Returns a None object otherwise.
        """
        for i in range(len(self._products)):
            if self._products[i].id == product_id:
                return self._products.pop(i)
        return None
