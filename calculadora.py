"""
Calculadora simples em Python (modo interativo)

Operações suportadas:
- Soma (a + b)
- Subtração (a - b)
- Multiplicação (a * b)
- Divisão (a / b)
- Potência (a ** b)
- Módulo (a % b)
- Divisão inteira (a // b)

Melhorias de usabilidade:
- Entrada rápida por expressão: ex. "2 + 3", "7*4", "_ / 2" ("_" usa o último resultado)
- Atalho para sair: "q" ou "0"
- Enter para usar o último resultado como primeiro número (quando existir)
- Histórico das últimas operações
"""

from typing import Optional, List, Tuple
import re


class UserCancelledInput(Exception):
	"""Sinaliza que o usuário cancelou a entrada (ex.: digitou 'q')."""
	pass


def format_number(value: float) -> str:
	"""Formata números para exibição amigável, removendo .0 quando possível."""
	if value == int(value):
		return str(int(value))
	return str(value)


def parse_number(prompt_text: str, default_value: Optional[float] = None) -> float:
	"""Lê um número, aceita vírgula ou ponto. Enter usa default quando fornecido. 'q' sai.

	Args:
		prompt_text: texto base do prompt.
		default_value: se fornecido, Enter retorna esse valor.

	Raises:
		UserCancelledInput: se o usuário digitar 'q' ou 'sair'.
	"""
	while True:
		full_prompt = prompt_text
		if default_value is not None:
			default_formatted = format_number(default_value)
			full_prompt = f"{prompt_text} [Enter usa {default_formatted}]: "
		user_input = input(full_prompt if default_value is not None else prompt_text).strip()
		if user_input.lower() in {"q", "sair"}:
			raise UserCancelledInput()
		if user_input == "" and default_value is not None:
			return float(default_value)
		user_input = user_input.replace(" ", "")
		user_input = user_input.replace(",", ".")
		try:
			return float(user_input)
		except ValueError:
			print("Entrada inválida. Digite um número válido (ex.: 10, 3.5, -2) ou 'q' para sair.")


def add_numbers(a: float, b: float) -> float:
	return a + b


def subtract_numbers(a: float, b: float) -> float:
	return a - b


def multiply_numbers(a: float, b: float) -> float:
	return a * b


def divide_numbers(a: float, b: float) -> Optional[float]:
	if b == 0:
		print("Erro: divisão por zero não é permitida.")
		return None
	return a / b


def power_numbers(a: float, b: float) -> float:
	return a ** b


def modulo_numbers(a: float, b: float) -> Optional[float]:
	if b == 0:
		print("Erro: módulo por zero não é permitido.")
		return None
	return a % b


def floor_divide_numbers(a: float, b: float) -> Optional[float]:
	if b == 0:
		print("Erro: divisão inteira por zero não é permitida.")
		return None
	return a // b


def print_menu(last_result: Optional[float]) -> None:
	print("\n=== Calculadora ===")
	if last_result is not None:
		print(f"Último resultado: {format_number(last_result)} (use '_' ou Enter para reutilizar)")
	print("1) Soma (+)")
	print("2) Subtração (-)")
	print("3) Multiplicação (*)")
	print("4) Divisão (/)")
	print("5) Potência (**)")
	print("6) Módulo (%)")
	print("7) Divisão inteira (//)")
	print("h) Histórico | c) Limpar resultado | 0/q) Sair")


def try_parse_expression(expression_text: str, last_result: Optional[float]) -> Optional[Tuple[float, str, float]]:
	"""Tenta interpretar uma expressão do tipo 'a op b'. Suporta '_' como último resultado."""
	pattern = r"^\s*([+-]?(?:\d+(?:[.,]\d+)?|_))\s*(\*\*|//|[+\-*/%])\s*([+-]?(?:\d+(?:[.,]\d+)?|_))\s*$"
	match = re.match(pattern, expression_text)
	if not match:
		return None
	left_raw, operator_symbol, right_raw = match.groups()

	def convert_operand(operand_text: str) -> Optional[float]:
		if operand_text == "_":
			return last_result
		operand_text = operand_text.replace(",", ".")
		try:
			return float(operand_text)
		except ValueError:
			return None

	left_value = convert_operand(left_raw)
	right_value = convert_operand(right_raw)
	if left_value is None or right_value is None:
		return None
	return left_value, operator_symbol, right_value


def main() -> None:
	last_result: Optional[float] = None
	history: List[str] = []

	while True:
		print_menu(last_result)
		choice = input("Escolha uma opção ou digite uma expressão (ex.: 2+3, _*4): ").strip()

		# Atalhos de saída
		if choice.lower() in {"0", "q", "sair"}:
			print("Até mais!")
			break

		# Expressão rápida (ex.: 2+3, 4 ** 2, _ / 10)
		expr = try_parse_expression(choice, last_result)
		if expr is not None:
			number_a, operator_label, number_b = expr
			if operator_label == "+":
				result = add_numbers(number_a, number_b)
			elif operator_label == "-":
				result = subtract_numbers(number_a, number_b)
			elif operator_label == "*":
				result = multiply_numbers(number_a, number_b)
			elif operator_label == "/":
				result = divide_numbers(number_a, number_b)
			elif operator_label == "**":
				result = power_numbers(number_a, number_b)
			elif operator_label == "%":
				result = modulo_numbers(number_a, number_b)
			else:  # //
				result = floor_divide_numbers(number_a, number_b)

			if result is not None:
				formatted_a = format_number(number_a)
				formatted_b = format_number(number_b)
				formatted_result = format_number(result)
				print(f"Resultado: {formatted_a} {operator_label} {formatted_b} = {formatted_result}")
				last_result = result
				history.append(f"{formatted_a} {operator_label} {formatted_b} = {formatted_result}")
				if len(history) > 20:
					history.pop(0)
			continue

		# Comandos utilitários
		if choice.lower() == "h":
			if not history:
				print("Histórico vazio.")
			else:
				print("\n— Histórico —")
				for item in history[-10:]:
					print(item)
			continue
		if choice.lower() == "c":
			last_result = None
			print("Último resultado limpo.")
			continue

		# Menu numérico tradicional
		if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
			print("Opção inválida. Tente novamente.")
			continue

		try:
			prompt_a = "Digite o primeiro número"
			number_a = parse_number(prompt_a + ": ", default_value=last_result)
			number_b = parse_number("Digite o segundo número: ")
		except UserCancelledInput:
			print("Operação cancelada.")
			continue

		result: Optional[float]
		operation_label: str

		if choice == "1":
			result = add_numbers(number_a, number_b)
			operation_label = "+"
		elif choice == "2":
			result = subtract_numbers(number_a, number_b)
			operation_label = "-"
		elif choice == "3":
			result = multiply_numbers(number_a, number_b)
			operation_label = "*"
		elif choice == "4":
			result = divide_numbers(number_a, number_b)
			operation_label = "/"
		elif choice == "5":
			result = power_numbers(number_a, number_b)
			operation_label = "**"
		elif choice == "6":
			result = modulo_numbers(number_a, number_b)
			operation_label = "%"
		else:  # choice == "7"
			result = floor_divide_numbers(number_a, number_b)
			operation_label = "//"

		if result is not None:
			formatted_a = format_number(number_a)
			formatted_b = format_number(number_b)
			formatted_result = format_number(result)
			print(f"Resultado: {formatted_a} {operation_label} {formatted_b} = {formatted_result}")
			last_result = result
			history.append(f"{formatted_a} {operation_label} {formatted_b} = {formatted_result}")
			if len(history) > 20:
				history.pop(0)


if __name__ == "__main__":
	main()