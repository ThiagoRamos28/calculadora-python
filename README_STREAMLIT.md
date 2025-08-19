# 🧮 Calculadora Python - Interface Web Streamlit

Uma versão web moderna da sua calculadora Python, criada com **Streamlit** para oferecer uma experiência visual elegante e interativa.

## ✨ Características da Versão Web

### 🎯 **Funcionalidades Principais**

- **Interface gráfica moderna** com gradientes e animações
- **Todas as operações** da calculadora Python original
- **Histórico interativo** com as últimas 50 operações
- **Sistema de memória** (MS, MR, MC)
- **Estatísticas em tempo real** com gráficos
- **Design responsivo** para desktop e mobile

### 🔬 **Operações Disponíveis**

- **Básicas**: Adição (+), Subtração (-), Multiplicação (×), Divisão (÷)
- **Avançadas**: Potência (^), Módulo (mod), Divisão inteira (//), Raiz quadrada (√)
- **Utilitárias**: Porcentagem (%), Mudar sinal (±), Limpar (AC)

### 💾 **Recursos Adicionais**

- **Histórico expandível** com detalhes de cada operação
- **Reutilização de resultados** com um clique
- **Gráfico de pizza** mostrando distribuição de operações
- **Métricas em tempo real** (total de operações, tipos únicos)
- **Sistema de memória** para armazenar valores importantes

## 🚀 Como Executar

### **Opção 1: Script Automático (Recomendado)**

```bash
# Execute o script de inicialização
python run_calculadora_web.py
```

### **Opção 2: Comando Manual**

```bash
# 1. Instalar dependências
pip install -r requirements_streamlit.txt

# 2. Executar aplicação
streamlit run calculadora_streamlit.py
```

### **Opção 3: Comando Direto**

```bash
# Instalar e executar em uma linha
pip install streamlit pandas plotly && streamlit run calculadora_streamlit.py
```

## 📋 Pré-requisitos

- **Python 3.8+**
- **pip** (gerenciador de pacotes Python)
- **Navegador web** moderno

## 🎨 Interface e Design

### **Layout Principal**

- **Header elegante** com gradiente azul-roxo
- **Display da calculadora** com fundo escuro e fonte monospace
- **Botões organizados** em grid responsivo
- **Painel lateral** com histórico e estatísticas

### **Estilos Visuais**

- **Gradientes modernos** para botões e elementos
- **Animações suaves** nos botões (hover, active)
- **Cores consistentes** para diferentes tipos de operação
- **Sombras e bordas** arredondadas para profundidade

### **Responsividade**

- **Layout adaptativo** que funciona em qualquer tela
- **Colunas flexíveis** que se reorganizam automaticamente
- **Botões otimizados** para touch e mouse

## 🔧 Arquivos da Versão Web

```
calculadora-python/
├── calculadora_streamlit.py      # Aplicação principal Streamlit
├── run_calculadora_web.py        # Script de inicialização automática
├── requirements_streamlit.txt     # Dependências Python
├── .streamlit/
│   └── config.toml              # Configurações do Streamlit
└── README_STREAMLIT.md          # Esta documentação
```

## 📊 Funcionalidades Avançadas

### **Sistema de Histórico**

- Armazena as últimas 50 operações
- Mostra expressão, resultado e horário
- Botão para reutilizar qualquer resultado
- Opção para limpar histórico completo

### **Estatísticas e Gráficos**

- **Contador de operações** em tempo real
- **Tipos de operação** utilizados
- **Gráfico de pizza** interativo com Plotly
- **Métricas visuais** em cards coloridos

### **Sistema de Memória**

- **MS (Memory Store)**: Armazena valor atual
- **MR (Memory Recall)**: Recupera valor armazenado
- **MC (Memory Clear)**: Limpa memória
- **Feedback visual** para todas as operações

## 🌐 Acesso e Navegação

### **URLs de Acesso**

- **Local**: `http://localhost:8501`
- **Rede**: `http://[SEU_IP]:8501` (para outros dispositivos)

### **Navegação**

- **Sidebar**: Informações sobre a calculadora
- **Área principal**: Interface da calculadora
- **Painel direito**: Histórico e estatísticas
- **Responsivo**: Se adapta automaticamente ao tamanho da tela

## 🛠️ Personalização

### **Cores e Temas**

- Edite o arquivo `.streamlit/config.toml`
- Modifique as variáveis CSS no arquivo principal
- Personalize gradientes e paletas de cores

### **Funcionalidades**

- Adicione novas operações matemáticas
- Modifique o sistema de histórico
- Personalize as estatísticas e gráficos

## 🔍 Solução de Problemas

### **Erro: "ModuleNotFoundError"**

```bash
# Instale as dependências
pip install -r requirements_streamlit.txt
```

### **Erro: "Port already in use"**

```bash
# Use uma porta diferente
streamlit run calculadora_streamlit.py --server.port 8502
```

### **Erro: "Python version"**

- Certifique-se de usar Python 3.8+
- Verifique com `python --version`

### **Problemas de Performance**

- Feche outras abas do navegador
- Reinicie o servidor Streamlit
- Verifique o uso de memória do sistema

## 🚀 Deploy e Distribuição

### **Deploy Local**

```bash
# Construir aplicação
streamlit run calculadora_streamlit.py --server.headless true
```

### **Deploy na Nuvem**

- **Streamlit Cloud**: Deploy automático do GitHub
- **Heroku**: Com Procfile e requirements
- **Docker**: Containerização da aplicação

### **Distribuição**

- Compartilhe o repositório completo
- Inclua o script de inicialização
- Documente as dependências

## 🤝 Contribuições

### **Como Contribuir**

1. **Fork** do repositório
2. **Crie uma branch** para sua feature
3. **Implemente** as melhorias
4. **Teste** a aplicação
5. **Envie um Pull Request**

### **Áreas para Melhorias**

- Novas operações matemáticas
- Temas visuais adicionais
- Exportação de histórico
- Integração com APIs externas
- Testes automatizados

## 📱 Compatibilidade

### **Navegadores Suportados**

- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

### **Dispositivos**

- ✅ Desktop (Windows, macOS, Linux)
- ✅ Tablet (iOS, Android)
- ✅ Mobile (iOS, Android)

### **Sistemas Operacionais**

- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Ubuntu 18.04+
- ✅ CentOS 7+

## 📄 Licença

Este projeto mantém a mesma licença MIT da calculadora Python original.

---

## 🎯 **Resumo da Transformação**

✅ **Calculadora Python original** → **Interface web moderna**  
✅ **Linha de comando** → **Interface gráfica interativa**  
✅ **Funcionalidades básicas** → **Recursos avançados + visualização**  
✅ **Uso local** → **Acesso web + responsivo**  
✅ **Histórico simples** → **Sistema completo + gráficos**

A calculadora agora oferece o **melhor dos dois mundos**: toda a funcionalidade Python original com uma **interface web moderna e elegante**! 🚀✨
