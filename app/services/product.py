import json


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

    def load_persisted(self):
        """
        Reads persisted data.
        """
        self._id_counter = -1

        file = open("./app/data/products.jsonl", "r")
        for line in file:
            product = Product(**json.loads(line))
            self._products.append(product)
            if product.id > self._id_counter:
                self._id_counter = product.id
        file.close()

        self._id_counter += 1

    def persist(self):
        """
        Persists the data.
        """
        file = open("./app/data/products.jsonl", "w")
        for product in self._products:
            file.write(
                json.dumps(product, default=lambda o: o.__dict__, skipkeys=True) + "\n"
            )
        file.close()

    def add_product(self, name: str, price: float):
        """
        Appends a new product to the list of products.

        Raises ValueError if parameters are invalid.
        """

        if name == "":
            raise ValueError("O nome do produto não pode ser vazio.")

        if price <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")

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

    def find_product_by_name(self, search_string: str):
        """
        Receive a 'search string' and returns products whose names match it.

        Returns an empty list if there are no matches.
        """
        results = []
        for product in self._products:
            if search_string.lower() in product.name.lower():
                results.append(product)
        return results

    def find_product_by_price(self, lower_bound: float, upper_bound: float):
        """
        Receives lower and upper bounds and returns all products whose prices fall in between (inclusive on both ends).

        Returns an empty list if there are no matches.
        """
        if not isinstance(lower_bound, (float, int)) or not isinstance(
            upper_bound, (float, int)
        ):
            raise ValueError("Os limites de preço devem ser números (float ou int).")

        # Validation for negative values
        if lower_bound < 0 or upper_bound < 0:
            raise ValueError("Os limites de preço não podem ser negativos.")

        # Validation for logical order of bounds
        if lower_bound > upper_bound:
            raise ValueError(
                "O limite inferior não pode ser maior que o limite superior."
            )

        results = []
        for product in self._products:
            if lower_bound <= product.price <= upper_bound:
                results.append(product)
        return results

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
