module.exports = {
  collectCoverage: true,
  collectCoverageFrom: [
    "app/*.js", // Inclui todos os arquivos .js
    "!node_modules/**", // Exclui dependências
  ],
};