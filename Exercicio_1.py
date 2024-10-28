def calcular_peso_ideal_h(altura):
    peso = (72.7 * altura) - 58
    return round(peso, 2)  # Retorna um float arredondado

def calcular_peso_ideal_m(altura):
    peso = (62.1 * altura) - 44.7
    return round(peso, 2)  # Retorna um float arredondado

def main():
    try:
        altura = float(input("Digite a altura em metros: "))
        genero = input("Você é homem ou mulher?: ").strip().lower()

        if genero == 'homem':
            peso = calcular_peso_ideal_h(altura)
            print(f"Seu peso ideal como homem com altura {altura}m é: {peso} kg")
        elif genero == 'mulher':
            peso = calcular_peso_ideal_m(altura)
            print(f"Seu peso ideal como mulher com altura {altura}m é: {peso} kg")
        else:
            print("Gênero inválido. Por favor, insira 'homem' ou 'mulher'.")
    except ValueError:
        print("Erro. Por favor, insira um número válido para a altura.")

if __name__ == "__main__":
    main()