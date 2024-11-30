class ProductService {
    constructor() {
        this.products = [];
        this.productIdCounter = 1;
    }

    addProduct(name, price) {
        const product = {
            id: this.productIdCounter++,
            name,
            price,
        };
        this.products.push(product);
        return product;
    }

    listProducts() {
        return this.products;
    }

    findProductById(productId) {
        return this.products.find((product) => product.id === productId);
    }

    updateProduct(productId, updates) {
        const product = this.findProductById(productId);
        if (!product) throw new Error(`Product with ID ${productId} not found.`);
        Object.assign(product, updates);
        return product;
    }

    deleteProduct(productId) {
        const index = this.products.findIndex((product) => product.id === productId);
        if (index === -1) throw new Error(`Product with ID ${productId} not found.`);
        this.products.splice(index, 1);
        return true;
    }
}

module.exports = ProductService;
