class CustomerService {
    constructor() {
        this.customers = [];
        this.customerIdCounter = 1;
    }

    addCustomer(name, email) {
        const customer = {
            id: this.customerIdCounter++,
            name,
            email,
        };
        this.customers.push(customer);
        return customer;
    }

    listCustomers() {
        return this.customers;
    }

    findCustomerById(customerId) {
        return this.customers.find((customer) => customer.id === customerId);
    }

    updateCustomer(customerId, updates) {
        const customer = this.findCustomerById(customerId);
        if (!customer) throw new Error(`Customer with ID ${customerId} not found.`);
        Object.assign(customer, updates);
        return customer;
    }

    deleteCustomer(customerId) {
        const index = this.customers.findIndex((customer) => customer.id === customerId);
        if (index === -1) throw new Error(`Customer with ID ${customerId} not found.`);
        this.customers.splice(index, 1);
        return true;
    }
}

module.exports = CustomerService;
