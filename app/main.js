const readline = require("readline");
const CustomerService = require("./customerService");
const ProductService = require("./productService");
const InvoiceService = require("./invoiceService");

const customerService = new CustomerService();
const productService = new ProductService();
const invoiceService = new InvoiceService(customerService, productService);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function showMenu() {
    console.log("\n=== Gerenciador de Faturas ===");
    console.log("1. Adicionar Cliente");
    console.log("2. Listar Clientes");
    console.log("3. Adicionar Produto");
    console.log("4. Listar Produtos");
    console.log("5. Criar Fatura");
    console.log("6. Listar Faturas");
    console.log("7. Sair");
    rl.question("Escolha uma opção: ", handleMenu);
}

function handleMenu(option) {
    switch (option) {
        case "1":
            rl.question("Nome do cliente: ", (name) => {
                rl.question("E-mail do cliente: ", (email) => {
                    const customer = customerService.addCustomer(name, email);
                    console.log(`Cliente adicionado: ${JSON.stringify(customer)}`);
                    showMenu();
                });
            });
            break;

        case "2":
            console.log("Clientes:");
            console.log(customerService.listCustomers());
            showMenu();
            break;

        case "3":
            rl.question("Nome do produto: ", (name) => {
                rl.question("Preço do produto: ", (price) => {
                    const product = productService.addProduct(name, parseFloat(price));
                    console.log(`Produto adicionado: ${JSON.stringify(product)}`);
                    showMenu();
                });
            });
            break;

        case "4":
            console.log("Produtos:");
            console.log(productService.listProducts());
            showMenu();
            break;

        case "5":
            rl.question("ID do cliente: ", (customerId) => {
                rl.question("IDs dos produtos (separados por vírgula): ", (productIds) => {
                    const productIdArray = productIds.split(",").map((id) => parseInt(id.trim(), 10));
                    try {
                        const invoice = invoiceService.createInvoice(parseInt(customerId, 10), productIdArray);
                        console.log(`Fatura criada: ${JSON.stringify(invoice)}`);
                    } catch (error) {
                        console.error(error.message);
                    }
                    showMenu();
                });
            });
            break;

        case "6": // Listar Faturas
            const invoices = invoiceService.listInvoices();
            if (invoices.length === 0) {
                console.log("Nenhuma fatura encontrada.");
            } else {
                console.log("Faturas:");
                invoices.forEach((invoice, index) => {
                    console.log(`Fatura ${index + 1}:`);
                    console.log(`Cliente: ${invoice.customerName}`);
                    console.log("Produtos:");
                    invoice.products.forEach((product) => {
                        console.log(`- ${product.name} (R$${product.price})`);
                    });
                });
            }
            showMenu();
            break;

        case "7":
            console.log("Saindo...");
            rl.close();
            break;

        default:
            console.log("Opção inválida.");
            showMenu();
            break;
    }
}

showMenu();
