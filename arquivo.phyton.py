def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) e retorna o valor.

    Argumentos:
    peso (float): O peso da pessoa em quilogramas.
    altura (float): A altura da pessoa em metros.

    Retorna:
    float: O valor do IMC.
    """
    if altura <= 0:
        raise ValueError("A altura deve ser um valor positivo e maior que zero.")
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com as categorias da OMS.

    Argumentos:
    imc (float): O valor do IMC.

    Retorna:
    str: A categoria de classificação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3 (Mórbida)"

# --- Programa principal ---
if __name__ == "__main__":
    print("--- Calculadora de Índice de Massa Corporal (IMC) ---")

    try:
        # Solicita o peso e a altura ao usuário
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))

        # Calcula o IMC
        imc_calculado = calcular_imc(peso, altura)
        print(f"\nSeu IMC é: {imc_calculado:.2f}") # .2f formata para duas casas decimais

        # Classifica o IMC
        classificacao = classificar_imc(imc_calculado)
        print(f"Classificação: {classificacao}")

    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite valores numéricos válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    print("\n--- Fim do programa ---")