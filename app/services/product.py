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
        self.products = []
        self.id_counter = 0

    def add_product(self, name: str, price: float):
        """
        Appens a new product to the list of products.
        """
        # Checks if product parameters are valid.
        if price <= 0 or name == "":
            return None

        product = Product(self.id_counter, name, price)
        self.products.append(product)
        self.id_counter += 1

        return product

    def list_products(self):
        """
        Returns the stored list of products.
        """
        return self.products

    def find_product_by_id(self, id: int):
        """
        Returns the product with the given id if on the list.
        Returns a None object otherwise.
        """
        for product in self.products:
            if product.id == id:
                return product
        return None

    def update_product(self, product_id: int, name: str, price: float):
        """
        Returns the new product if successfull.
        Returns a None object otherwise.
        """
        for i in range(len(self.products)):
            if self.products[i].id == product_id:
                # Checks if product parameters are valid.
                if price <= 0 or name == "":
                    return None

                self.products[i] = Product(product_id, name, price)
                return self.products[i]
        return None

    def delete_product(self, product_id: int):
        """
        Returns the deleted product if successful.
        Returns a None object otherwise.
        """
        for i in range(len(self.products)):
            if self.products[i].id == product_id:
                return self.products.pop(i)
        return None
