# 🧮 Calculadora Python

Uma calculadora interativa em Python com interface de linha de comando, desenvolvida para oferecer uma experiência de usuário intuitiva e funcional.

## ✨ Características

- **Operações Básicas**: Soma, subtração, multiplicação, divisão
- **Operações Avançadas**: Potência, módulo, divisão inteira
- **Interface Intuitiva**: Menu numérico tradicional ou entrada de expressões
- **Histórico**: Mantém as últimas 20 operações realizadas
- **Atalhos**: Suporte para expressões rápidas como "2+3" ou "_*4"
- **Reutilização**: Use "_" ou Enter para reutilizar o último resultado
- **Tratamento de Erros**: Validação de entrada e tratamento de divisão por zero

## 🚀 Como Usar

### Instalação
```bash
# Clone o repositório
git clone https://github.com/ThiagoRamos28/calculadora-python.git

# Navegue para o diretório
cd calculadora-python

# Execute a calculadora
python calculadora.py
```

### Uso Interativo
1. **Menu Tradicional**: Escolha uma opção de 1 a 7
2. **Expressões Rápidas**: Digite diretamente como "2+3", "10*5", "_/2"
3. **Histórico**: Digite 'h' para ver as últimas operações
4. **Limpar**: Digite 'c' para limpar o último resultado
5. **Sair**: Digite 'q', '0' ou 'sair'

### Exemplos de Uso
```
=== Calculadora ===
Último resultado: 15 (use '_' ou Enter para reutilizar)
1) Soma (+)
2) Subtração (-)
3) Multiplicação (*)
4) Divisão (/)
5) Potência (**)
6) Módulo (%)
7) Divisão inteira (//)
h) Histórico | c) Limpar resultado | 0/q) Sair

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 2+3
Resultado: 2 + 3 = 5

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): _*4
Resultado: 5 * 4 = 20
```

## 🛠️ Funcionalidades Técnicas

- **Validação de Entrada**: Aceita números com vírgula ou ponto decimal
- **Tratamento de Erros**: Mensagens claras para entradas inválidas
- **Formatação Inteligente**: Remove .0 desnecessários para números inteiros
- **Expressões Regulares**: Parser robusto para expressões matemáticas
- **Histórico Circular**: Mantém as últimas operações com limite configurável

## 📋 Requisitos

- Python 3.6+
- Nenhuma dependência externa (apenas bibliotecas padrão)

## 🔧 Estrutura do Código

- `main()`: Função principal e loop do programa
- `parse_number()`: Validação e leitura de números
- `try_parse_expression()`: Parser de expressões matemáticas
- Funções de operações: `add_numbers()`, `subtract_numbers()`, etc.
- `format_number()`: Formatação amigável de números
- `print_menu()`: Interface do usuário

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Thiago Ramos** - [GitHub](https://github.com/ThiagoRamos28)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!