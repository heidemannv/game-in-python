import random

# criando as condicionais
number_created = random.randint(1, 101)
guess = None

while guess != number_created:
    guess = int(
        input("Um número entre 1 e 100 foi gerado aleatóriamente, tente acerta-lo:"))

    if guess > number_created:
        print("O número é menor")

    elif guess < number_created:
        print("O número é maior")

    else:
        print("Parabéns ! Você acertou.")

        # Desenvolvido por Vinicius Heidemann
        # meu github = heidemanndev
