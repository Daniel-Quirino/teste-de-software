const ProductService = require("../app/productService");

describe("ProductService", () => {
    let productService;

    beforeEach(() => {
        productService = new ProductService();
    });

    test("should add a product", () => {
        const product = productService.addProduct("Laptop", 1500);
        expect(product).toHaveProperty("id");
        expect(product.name).toBe("Laptop");
        expect(product.price).toBe(1500);
    });

    test("should list all products", () => {
        productService.addProduct("Phone", 800);
        productService.addProduct("Tablet", 400);
        const products = productService.listProducts();
        expect(products).toHaveLength(2);
    });

    test("should find a product by ID", () => {
        const product = productService.addProduct("Monitor", 300);
        const found = productService.findProductById(product.id);
        expect(found).toEqual(product);
    });

    test("should update a product", () => {
        const product = productService.addProduct("Keyboard", 50);
        const updated = productService.updateProduct(product.id, { price: 60 });
        expect(updated.price).toBe(60);
    });

    test("should delete a product", () => {
        const product = productService.addProduct("Mouse", 25);
        const result = productService.deleteProduct(product.id);
        expect(result).toBe(true);
        expect(productService.listProducts()).toHaveLength(0);
    });

    test("should throw an error when updating a non-existent product", () => {
        expect(() => productService.updateProduct(999, { price: 100 })).toThrow(
            "Product with ID 999 not found."
        );
    });

    test("should throw an error when deleting a non-existent product", () => {
        expect(() => productService.deleteProduct(999)).toThrow("Product with ID 999 not found.");
    });
});
