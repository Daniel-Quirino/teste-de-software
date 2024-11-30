const CustomerService = require("../app/customerService");

describe("CustomerService", () => {
    let customerService;

    beforeEach(() => {
        customerService = new CustomerService();
    });

    test("should add a customer", () => {
        const customer = customerService.addCustomer("John Doe", "john@example.com");
        expect(customer).toHaveProperty("id");
        expect(customer.name).toBe("John Doe");
        expect(customer.email).toBe("john@example.com");
    });

    test("should list all customers", () => {
        customerService.addCustomer("Alice", "alice@example.com");
        customerService.addCustomer("Bob", "bob@example.com");
        const customers = customerService.listCustomers();
        expect(customers).toHaveLength(2);
    });

    test("should find a customer by ID", () => {
        const customer = customerService.addCustomer("Charlie", "charlie@example.com");
        const found = customerService.findCustomerById(customer.id);
        expect(found).toEqual(customer);
    });

    test("should update a customer", () => {
        const customer = customerService.addCustomer("Dave", "dave@example.com");
        const updated = customerService.updateCustomer(customer.id, { name: "David" });
        expect(updated.name).toBe("David");
    });

    test("should delete a customer", () => {
        const customer = customerService.addCustomer("Eve", "eve@example.com");
        const result = customerService.deleteCustomer(customer.id);
        expect(result).toBe(true);
        expect(customerService.listCustomers()).toHaveLength(0);
    });

    test("should throw an error when updating a non-existent customer", () => {
        expect(() => customerService.updateCustomer(999, { name: "Non-existent" })).toThrow(
            "Customer with ID 999 not found."
        );
    });

    test("should throw an error when deleting a non-existent customer", () => {
        expect(() => customerService.deleteCustomer(999)).toThrow("Customer with ID 999 not found.");
    });
});
