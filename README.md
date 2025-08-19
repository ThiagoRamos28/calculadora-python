# 🧮 Calculadora Python

Uma calculadora interativa em Python com interface de linha de comando, desenvolvida para oferecer uma experiência de usuário intuitiva e funcional.

## ✨ Características

- **Operações Básicas**: Soma, subtração, multiplicação, divisão
- **Operações Avançadas**: Potência, módulo, divisão inteira
- **Interface Intuitiva**: Menu numérico tradicional ou entrada de expressões
- **Histórico**: Mantém as últimas 20 operações realizadas
- **Atalhos**: Suporte para expressões rápidas como "2+3" ou "\_\*4"
- **Reutilização**: Use "\_" ou Enter para reutilizar o último resultado
- **Tratamento de Erros**: Validação de entrada e tratamento de divisão por zero

## 🚀 Como Usar

### Instalação

# Clone o repositório

git clone https://github.com/ThiagoRamos28/calculadora-python.git

# Navegue para o diretório

cd calculadora-python

# Execute a calculadora

python calculadora.py

### Uso Interativo

1. **Menu Tradicional**: Escolha uma opção de 1 a 7
2. **Expressões Rápidas**: Digite diretamente como "2+3", "10\*5", "\_/2"
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

## 🌐 **Versão Web com Streamlit**

Agora também temos uma **versão web moderna** criada com Streamlit!

### ✨ **Interface Web**

- **Design elegante** com gradientes e animações
- **Interface responsiva** para desktop e mobile
- **Histórico interativo** com gráficos
- **Sistema de memória** avançado
- **Estatísticas em tempo real**

### 🚀 **Como Executar a Versão Web**

```bash
# Opção 1: Script automático (Recomendado)
python run_calculadora_web.py

# Opção 2: Comando manual
pip install -r requirements_streamlit.txt
streamlit run calculadora_streamlit.py

# Opção 3: Comando direto
pip install streamlit pandas plotly && streamlit run calculadora_streamlit.py
```

### 📱 **Acesso Web**

- **Local**: `http://localhost:8501`
- **Rede**: `http://[SEU_IP]:8501`

### 📚 **Documentação Completa**

Veja o arquivo `README_STREAMLIT.md` para informações detalhadas sobre a versão web.

## 🛠️ Funcionalidades Técnicas

- **Validação de Entrada**: Aceita números com vírgula ou ponto decimal
- **Tratamento de Erros**: Mensagens claras para entradas inválidas
- **Formatação Inteligente**: Remove .0 desnecessários para números inteiros
- **Expressões Regulares**: Parser robusto para expressões matemáticas
- **Histórico Circular**: Mantém as últimas operações com limite configurável

## 📋 Requisitos

- Python 3.6+
- Nenhuma dependência externa (apenas bibliotecas padrão)

**Para a versão web:**

- Python 3.8+
- Streamlit, Pandas, Plotly

## 🔧 Estrutura do Código

- `main()`: Função principal e loop do programa
- `parse_number()`: Validação e leitura de números
- `try_parse_expression()`: Parser de expressões matemáticas
- Funções de operações: `add_numbers()`, `subtract_numbers()`, etc.
- `format_number()`: Formatação amigável de números
- `print_menu()`: Interface do usuário

## 🌐 **Arquivos da Versão Web**

```
calculadora-python/
├── calculadora.py                 # Calculadora original (CLI)
├── calculadora_streamlit.py       # Versão web com Streamlit
├── run_calculadora_web.py         # Script de inicialização automática
├── requirements_streamlit.txt      # Dependências para versão web
├── .streamlit/
│   └── config.toml               # Configurações do Streamlit
├── README.md                      # Esta documentação
└── README_STREAMLIT.md           # Documentação da versão web
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

**Thiago Ramos** \- GitHub

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!

## 🎯 **Resumo das Versões**

| Versão  | Tipo              | Interface | Funcionalidades                  |
| ------- | ----------------- | --------- | -------------------------------- |
| **CLI** | Linha de comando  | Terminal  | Operações básicas + histórico    |
| **Web** | Interface gráfica | Navegador | Tudo da CLI + gráficos + memória |

**Escolha a versão que melhor atende suas necessidades!** 🚀
