#!/usr/bin/env python3
"""
Script de inicialização para a Calculadora Streamlit

Este script facilita a execução da calculadora web, verificando dependências
e iniciando o servidor Streamlit automaticamente.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    if sys.version_info < (3, 8):
        print("❌ Erro: Python 3.8+ é necessário!")
        print(f"Versão atual: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
    return True

def install_requirements():
    """Instala as dependências necessárias"""
    requirements_file = "requirements_streamlit.txt"
    
    if not os.path.exists(requirements_file):
        print(f"❌ Arquivo {requirements_file} não encontrado!")
        return False
    
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def run_streamlit():
    """Executa a aplicação Streamlit"""
    app_file = "calculadora_streamlit.py"
    
    if not os.path.exists(app_file):
        print(f"❌ Arquivo {app_file} não encontrado!")
        return False
    
    print("🚀 Iniciando Calculadora Streamlit...")
    print("🌐 A aplicação será aberta no seu navegador automaticamente")
    print("📱 Para acessar de outros dispositivos, use o endereço local mostrado")
    print("⏹️  Para parar, pressione Ctrl+C no terminal")
    print("-" * 50)
    
    try:
        # Executa o Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", app_file,
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Calculadora encerrada pelo usuário")
    except Exception as e:
        print(f"❌ Erro ao executar Streamlit: {e}")
        return False
    
    return True

def main():
    """Função principal"""
    print("🧮 Calculadora Python - Interface Web")
    print("=" * 40)
    
    # Verifica versão do Python
    if not check_python_version():
        return 1
    
    # Instala dependências
    if not install_requirements():
        return 1
    
    # Executa a aplicação
    if not run_streamlit():
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
