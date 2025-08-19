"""
Calculadora Streamlit - Interface Web Moderna

Uma calculadora web moderna criada com Streamlit, mantendo todas as funcionalidades
da calculadora Python original mas com uma interface gráfica elegante.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Optional
import math

# Configuração da página
st.set_page_config(
    page_title="🧮 Calculadora Python",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .calculator-display {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: right;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .operation-history {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #dee2e6;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .stButton > button {
        width: 100%;
        height: 3rem;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .number-btn > button {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        color: #495057;
    }
    
    .operator-btn > button {
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        color: white;
    }
    
    .equals-btn > button {
        background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
        color: white;
    }
    
    .clear-btn > button {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        color: white;
    }
    
    .special-btn > button {
        background: linear-gradient(135deg, #6c757d 0%, #545b62 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

class CalculadoraStreamlit:
    def __init__(self):
        self.initialize_session_state()
    
    def initialize_session_state(self):
        """Inicializa o estado da sessão Streamlit"""
        if 'display' not in st.session_state:
            st.session_state.display = '0'
        if 'previous_value' not in st.session_state:
            st.session_state.previous_value = None
        if 'operation' not in st.session_state:
            st.session_state.operation = None
        if 'waiting_for_operand' not in st.session_state:
            st.session_state.waiting_for_operand = False
        if 'history' not in st.session_state:
            st.session_state.history = []
        if 'memory' not in st.session_state:
            st.session_state.memory = 0
    
    def format_number(self, value: float) -> str:
        """Formata números para exibição amigável"""
        try:
            # Converte para float primeiro para garantir que é um número
            float_value = float(value)
            
            # Se o valor é um número inteiro, remove o .0
            if float_value.is_integer():
                return str(int(float_value))
            
            # Para números decimais, remove zeros desnecessários no final
            formatted = f"{float_value:.10g}"
            
            # Remove .0 se o resultado terminar com isso
            if formatted.endswith('.0'):
                formatted = formatted[:-2]
            
            return formatted
        except (ValueError, TypeError):
            # Se não conseguir converter, retorna o valor original como string
            return str(value)
    
    def input_number(self, num: str):
        """Processa entrada de números"""
        if st.session_state.waiting_for_operand:
            st.session_state.display = num
            st.session_state.waiting_for_operand = False
        else:
            if st.session_state.display == '0':
                st.session_state.display = num
            else:
                st.session_state.display += num
    
    def input_decimal(self):
        """Processa entrada de ponto decimal"""
        if st.session_state.waiting_for_operand:
            st.session_state.display = '0.'
            st.session_state.waiting_for_operand = False
        elif '.' not in st.session_state.display:
            st.session_state.display += '.'
    
    def clear(self):
        """Limpa a calculadora"""
        st.session_state.display = '0'
        st.session_state.previous_value = None
        st.session_state.operation = None
        st.session_state.waiting_for_operand = False
    
    def clear_history(self):
        """Limpa o histórico"""
        st.session_state.history = []
    
    def perform_operation(self, next_operation: str):
        """Executa operações matemáticas"""
        input_value = float(st.session_state.display)
        
        if st.session_state.previous_value is None:
            st.session_state.previous_value = input_value
        elif st.session_state.operation:
            current_value = st.session_state.previous_value
            result = self.calculate_result(current_value, input_value, st.session_state.operation)
            
            if result is not None:
                # Adiciona ao histórico
                history_item = {
                    'timestamp': datetime.now(),
                    'expression': f"{self.format_number(current_value)} {st.session_state.operation} {self.format_number(input_value)}",
                    'result': self.format_number(result),
                    'operation': st.session_state.operation
                }
                st.session_state.history.append(history_item)
                
                # Limita o histórico a 50 itens
                if len(st.session_state.history) > 50:
                    st.session_state.history.pop(0)
                
                formatted_result = self.format_number(result)
                st.session_state.display = formatted_result
                st.session_state.previous_value = result
        
        st.session_state.waiting_for_operand = True
        st.session_state.operation = next_operation
    
    def calculate_result(self, a: float, b: float, operation: str) -> Optional[float]:
        """Calcula o resultado de uma operação"""
        try:
            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '×':
                return a * b
            elif operation == '÷':
                if b == 0:
                    st.error("❌ Erro: Divisão por zero não é permitida!")
                    return None
                return a / b
            elif operation == '^':
                return a ** b
            elif operation == 'mod':
                if b == 0:
                    st.error("❌ Erro: Módulo por zero não é permitido!")
                    return None
                return a % b
            elif operation == '//':
                if b == 0:
                    st.error("❌ Erro: Divisão inteira por zero não é permitida!")
                    return None
                return a // b
            else:
                return None
        except Exception as e:
            st.error(f"❌ Erro na operação: {str(e)}")
            return None
    
    def calculate(self):
        """Executa o cálculo final"""
        if st.session_state.operation and st.session_state.previous_value is not None:
            self.perform_operation('')
            st.session_state.operation = None
            st.session_state.previous_value = None
            st.session_state.waiting_for_operand = True
    
    def percentage(self):
        """Calcula porcentagem"""
        try:
            value = float(st.session_state.display) / 100
            st.session_state.display = self.format_number(value)
        except:
            st.error("❌ Erro ao calcular porcentagem")
    
    def toggle_sign(self):
        """Muda o sinal do número"""
        if st.session_state.display != '0':
            try:
                # Converte para float, muda o sinal e formata de volta
                value = float(st.session_state.display)
                value = -value
                st.session_state.display = self.format_number(value)
            except ValueError:
                # Se não conseguir converter, faz a mudança manual
                if st.session_state.display.startswith('-'):
                    st.session_state.display = st.session_state.display[1:]
                else:
                    st.session_state.display = '-' + st.session_state.display
    
    def memory_store(self):
        """Armazena valor na memória"""
        try:
            st.session_state.memory = float(st.session_state.display)
            formatted_value = self.format_number(st.session_state.memory)
            st.success(f"💾 Valor {formatted_value} armazenado na memória")
        except:
            st.error("❌ Erro ao armazenar na memória")
    
    def memory_recall(self):
        """Recupera valor da memória"""
        st.session_state.display = self.format_number(st.session_state.memory)
        st.session_state.waiting_for_operand = False
    
    def memory_clear(self):
        """Limpa a memória"""
        st.session_state.memory = 0
        st.success("🗑️ Memória limpa")
    
    def create_calculator_interface(self):
        """Cria a interface principal da calculadora"""
        # Header principal
        st.markdown("""
        <div class="main-header">
            <h1>🧮 Calculadora Python</h1>
            <p>Calculadora interativa com interface moderna e funcionalidades avançadas</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Layout em colunas
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Display da calculadora
            st.markdown(f"""
            <div class="calculator-display">
                <div style="font-size: 1.2rem; margin-bottom: 1rem; opacity: 0.8;">
                    {f"{st.session_state.previous_value} {st.session_state.operation}" if st.session_state.operation and st.session_state.previous_value else ""}
                </div>
                <div style="font-size: 3rem; font-family: 'Courier New', monospace;">
                    {st.session_state.display}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Botões da calculadora
            self.create_calculator_buttons()
            
        with col2:
            # Painel lateral com histórico e estatísticas
            self.create_sidebar_panel()
    
    def create_calculator_buttons(self):
        """Cria os botões da calculadora"""
        # Primeira linha - Botões especiais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("AC", key="clear", help="Limpar tudo"):
                self.clear()
        
        with col2:
            if st.button("±", key="toggle_sign", help="Mudar sinal"):
                self.toggle_sign()
        
        with col3:
            if st.button("%", key="percentage", help="Porcentagem"):
                self.percentage()
        
        with col4:
            if st.button("÷", key="divide", help="Divisão"):
                self.perform_operation('÷')
        
        # Segunda linha
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("7", key="7"):
                self.input_number('7')
        
        with col2:
            if st.button("8", key="8"):
                self.input_number('8')
        
        with col3:
            if st.button("9", key="9"):
                self.input_number('9')
        
        with col4:
            if st.button("×", key="multiply", help="Multiplicação"):
                self.perform_operation('×')
        
        # Terceira linha
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("4", key="4"):
                self.input_number('4')
        
        with col2:
            if st.button("5", key="5"):
                self.input_number('5')
        
        with col3:
            if st.button("6", key="6"):
                self.input_number('6')
        
        with col4:
            if st.button("-", key="subtract", help="Subtração"):
                self.perform_operation('-')
        
        # Quarta linha
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("1", key="1"):
                self.input_number('1')
        
        with col2:
            if st.button("2", key="2"):
                self.input_number('2')
        
        with col3:
            if st.button("3", key="3"):
                self.input_number('3')
        
        with col4:
            if st.button("+", key="add", help="Adição"):
                self.perform_operation('+')
        
        # Quinta linha
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("0", key="0", help="Zero"):
                self.input_number('0')
        
        with col2:
            if st.button(".", key="decimal", help="Ponto decimal"):
                self.input_decimal()
        
        with col3:
            if st.button("=", key="equals", help="Calcular"):
                self.calculate()
        
        with col4:
            if st.button("^", key="power", help="Potência"):
                self.perform_operation('^')
        
        # Operações avançadas
        st.markdown("---")
        st.markdown("### 🔬 Operações Avançadas")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("mod", key="modulo", help="Módulo"):
                self.perform_operation('mod')
        
        with col2:
            if st.button("//", key="floor_divide", help="Divisão inteira"):
                self.perform_operation('//')
        
        with col3:
            if st.button("√", key="sqrt", help="Raiz quadrada"):
                try:
                    value = float(st.session_state.display)
                    if value >= 0:
                        result = math.sqrt(value)
                        st.session_state.display = self.format_number(result)
                        st.session_state.waiting_for_operand = True
                    else:
                        st.error("❌ Não é possível calcular raiz de número negativo")
                except:
                    st.error("❌ Erro ao calcular raiz quadrada")
        
        # Controles de memória
        st.markdown("---")
        st.markdown("### 💾 Memória")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("MS", key="memory_store", help="Armazenar na memória"):
                self.memory_store()
        
        with col2:
            if st.button("MR", key="memory_recall", help="Recuperar da memória"):
                self.memory_recall()
        
        with col3:
            if st.button("MC", key="memory_clear", help="Limpar memória"):
                self.memory_clear()
    
    def create_sidebar_panel(self):
        """Cria o painel lateral com histórico e estatísticas"""
        st.markdown("### 📊 Estatísticas")
        
        # Métricas principais
        total_operations = len(st.session_state.history)
        unique_operations = len(set(item['operation'] for item in st.session_state.history if item['operation']))
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total de Operações</h3>
                <h2>{total_operations}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Tipos de Operação</h3>
                <h2>{unique_operations}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Histórico
        st.markdown("### 📝 Histórico")
        
        if st.session_state.history:
            # Botão para limpar histórico
            if st.button("🗑️ Limpar Histórico", key="clear_history"):
                self.clear_history()
                st.rerun()
            
            # Exibir histórico
            for i, item in enumerate(reversed(st.session_state.history[-10:])):  # Últimas 10 operações
                with st.expander(f"{item['expression']} = {item['result']}", expanded=False):
                    st.write(f"**Operação:** {item['operation']}")
                    st.write(f"**Resultado:** {item['result']}")
                    st.write(f"**Horário:** {item['timestamp'].strftime('%H:%M:%S')}")
                    
                    # Botão para reutilizar resultado
                    if st.button(f"Reutilizar {item['result']}", key=f"reuse_{i}"):
                        st.session_state.display = item['result']
                        st.session_state.waiting_for_operand = False
                        st.rerun()
        else:
            st.info("📝 Nenhuma operação realizada ainda. Faça alguns cálculos para ver o histórico aqui!")
        
        # Gráfico de operações
        if len(st.session_state.history) > 0:
            st.markdown("### 📈 Gráfico de Operações")
            
            # Preparar dados para o gráfico
            df = pd.DataFrame(st.session_state.history)
            operation_counts = df['operation'].value_counts()
            
            # Criar gráfico de pizza
            fig = px.pie(
                values=operation_counts.values,
                names=operation_counts.index,
                title="Distribuição de Operações",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def run(self):
        """Executa a aplicação"""
        self.create_calculator_interface()

def main():
    """Função principal"""
    # Sidebar com informações
    with st.sidebar:
        st.markdown("## 🧮 Calculadora Python")
        st.markdown("---")
        st.markdown("### 📚 Sobre")
        st.markdown("""
        Esta é uma calculadora interativa criada com **Streamlit** que mantém todas as funcionalidades da versão Python original.
        
        **Funcionalidades:**
        - ✅ Operações básicas (+, -, ×, ÷)
        - ✅ Operações avançadas (^, mod, //, √)
        - ✅ Histórico de operações
        - ✅ Memória (MS, MR, MC)
        - ✅ Interface responsiva
        - ✅ Estatísticas e gráficos
        """)
        
        st.markdown("---")
        st.markdown("### 🚀 Como usar")
        st.markdown("""
        1. **Digite números** clicando nos botões
        2. **Escolha operações** clicando nos botões de operação
        3. **Pressione =** para calcular
        4. **Veja o histórico** no painel direito
        5. **Use a memória** para armazenar valores
        """)
        
        st.markdown("---")
        st.markdown("### 🔧 Desenvolvido com")
        st.markdown("- **Streamlit** - Interface web")
        st.markdown("- **Python** - Lógica da calculadora")
        st.markdown("- **Plotly** - Gráficos interativos")
        st.markdown("- **Pandas** - Manipulação de dados")
    
    # Executar calculadora
    calculadora = CalculadoraStreamlit()
    calculadora.run()

if __name__ == "__main__":
    main()
