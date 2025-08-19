# 📚 Exemplos de Uso da Calculadora

Este arquivo contém exemplos práticos de como usar a calculadora Python.

## 🚀 Executando a Calculadora

```bash
python calculadora.py
```

## 📖 Exemplos de Operações

### 1. Menu Tradicional

```
=== Calculadora ===
1) Soma (+)
2) Subtração (-)
3) Multiplicação (*)
4) Divisão (/)
5) Potência (**)
6) Módulo (%)
7) Divisão inteira (//)
h) Histórico | c) Limpar resultado | 0/q) Sair

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 10 + 5 = 15
```

### 2. Expressões Rápidas

```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 2+3
Resultado: 2 + 3 = 5

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 10*5
Resultado: 10 * 5 = 50

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 100/4
Resultado: 100 / 4 = 25.0
```

### 3. Usando o Último Resultado (_)

```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 5+3
Resultado: 5 + 3 = 8

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): _*2
Resultado: 8 * 2 = 16

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): _/4
Resultado: 16 / 4 = 4
```

### 4. Operações com Potência e Módulo

```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 2**8
Resultado: 2 ** 8 = 256

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 17%5
Resultado: 17 % 5 = 2

Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 20//3
Resultado: 20 // 3 = 6
```

### 5. Comandos Utilitários

#### Ver Histórico
```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): h
— Histórico —
5 + 3 = 8
8 * 2 = 16
16 / 4 = 4
2 ** 8 = 256
17 % 5 = 2
20 // 3 = 6
```

#### Limpar Último Resultado
```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): c
Último resultado limpo.
```

#### Sair da Calculadora
```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): q
Até mais!
```

## 💡 Dicas de Uso

1. **Números Decimais**: Use vírgula ou ponto (ex.: 3,5 ou 3.5)
2. **Números Negativos**: Use o sinal de menos (ex.: -5)
3. **Expressões Rápidas**: Digite diretamente como "2+3" em vez de usar o menu
4. **Reutilização**: Use "_" para referenciar o último resultado
5. **Enter**: Pressione Enter para usar o último resultado como primeiro número
6. **Histórico**: Mantém as últimas 20 operações automaticamente

## ⚠️ Tratamento de Erros

### Divisão por Zero
```
Digite o segundo número: 0
Erro: divisão por zero não é permitida.
```

### Entrada Inválida
```
Digite o primeiro número: abc
Entrada inválida. Digite um número válido (ex.: 10, 3.5, -2) ou 'q' para sair.
Digite o primeiro número: 
```

### Expressão Inválida
```
Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): 2++3
Opção inválida. Tente novamente.
```

## 🔄 Fluxo de Trabalho Típico

1. **Inicie a calculadora**: `python calculadora.py`
2. **Faça operações**: Use o menu ou expressões rápidas
3. **Reutilize resultados**: Use "_" para continuar calculando
4. **Verifique histórico**: Digite 'h' para revisar operações
5. **Saia**: Digite 'q' quando terminar

## 🎯 Casos de Uso Comuns

- **Cálculos rápidos**: "2+3", "10*5", "100/4"
- **Cálculos em sequência**: Use "_" para continuar operações
- **Verificação de resultados**: Use o histórico para revisar
- **Aprendizado**: Ideal para estudantes de matemática
- **Prototipagem**: Teste rápido de fórmulas matemáticas