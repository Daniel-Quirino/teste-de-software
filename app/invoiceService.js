class InvoiceService {
    constructor(customerService, productService) {
        this.customerService = customerService;
        this.productService = productService;
        this.invoices = [];
        this.invoiceIdCounter = 1;
    }

    createInvoice(customerId, productIds, date) {
        const customer = this.customerService.findCustomerById(customerId);
        if (!customer) throw new Error(`Customer with ID ${customerId} not found.`);

        const products = productIds.map((productId) => {
            const product = this.productService.findProductById(productId);
            if (!product) throw new Error(`Product with ID ${productId} not found.`);
            return product;
        });

        const total = products.reduce((sum, product) => sum + product.price, 0);

        const invoice = {
            id: this.invoiceIdCounter++,
            customer,
            products,
            date: date || new Date(),
            total,
        };
        this.invoices.push(invoice);
        return invoice;
    }

    listInvoices() {
        return this.invoices.map((invoice) => ({
            customerName: invoice.customer.name,
            products: invoice.products.map((product) => ({
                name: product.name,
                price: product.price,
            })),
        }));
    }

    findInvoiceById(invoiceId) {
        return this.invoices.find((invoice) => invoice.id === invoiceId);
    }

    deleteInvoice(invoiceId) {
        const index = this.invoices.findIndex((invoice) => invoice.id === invoiceId);
        if (index === -1) throw new Error(`Invoice with ID ${invoiceId} not found.`);
        this.invoices.splice(index, 1);
        return true;
    }
}

module.exports = InvoiceService;
