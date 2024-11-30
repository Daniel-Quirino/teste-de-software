const CustomerService = require("../app/customerService");
const ProductService = require("../app/productService");
const InvoiceService = require("../app/invoiceService");

describe("InvoiceService", () => {
    let customerService, productService, invoiceService;

    beforeEach(() => {
        customerService = new CustomerService();
        productService = new ProductService();
        invoiceService = new InvoiceService(customerService, productService);
    });

    test("should create an invoice", () => {
        const customer = customerService.addCustomer("John Doe", "john@example.com");
        const product1 = productService.addProduct("Laptop", 1500);
        const product2 = productService.addProduct("Mouse", 25);

        const invoice = invoiceService.createInvoice(customer.id, [product1.id, product2.id]);

        expect(invoice).toHaveProperty("id");
        expect(invoice.customer).toEqual(customer);
        expect(invoice.products).toEqual([product1, product2]);
        expect(invoice.total).toBe(1525);
    });

    test("should list all invoices with customer name and products", () => {
        const customer = customerService.addCustomer("Alice", "alice@example.com");
        const product1 = productService.addProduct("Phone", 800);
        const product2 = productService.addProduct("Charger", 50);

        invoiceService.createInvoice(customer.id, [product1.id, product2.id]);
        const invoices = invoiceService.listInvoices();

        expect(invoices).toHaveLength(1);
        expect(invoices[0]).toEqual({
            customerName: "Alice",
            products: [
                { name: "Phone", price: 800 },
                { name: "Charger", price: 50 },
            ],
        });
    });

    test("should find an invoice by ID", () => {
        const customer = customerService.addCustomer("Bob", "bob@example.com");
        const product = productService.addProduct("Tablet", 400);

        const invoice = invoiceService.createInvoice(customer.id, [product.id]);
        const found = invoiceService.findInvoiceById(invoice.id);

        expect(found).toEqual(invoice);
    });

    test("should delete an invoice", () => {
        const customer = customerService.addCustomer("Charlie", "charlie@example.com");
        const product = productService.addProduct("Monitor", 300);

        const invoice = invoiceService.createInvoice(customer.id, [product.id]);
        const result = invoiceService.deleteInvoice(invoice.id);

        expect(result).toBe(true);
        expect(invoiceService.listInvoices()).toHaveLength(0);
    });

    test("should throw an error when creating an invoice with a non-existent customer", () => {
        const product = productService.addProduct("Keyboard", 50);
        expect(() => invoiceService.createInvoice(999, [product.id])).toThrow(
            "Customer with ID 999 not found."
        );
    });

    test("should throw an error when creating an invoice with a non-existent product", () => {
        const customer = customerService.addCustomer("Dave", "dave@example.com");
        expect(() => invoiceService.createInvoice(customer.id, [999])).toThrow(
            "Product with ID 999 not found."
        );
    });

    test("should throw an error when deleting a non-existent invoice", () => {
        expect(() => invoiceService.deleteInvoice(999)).toThrow("Invoice with ID 999 not found.");
    });
});
