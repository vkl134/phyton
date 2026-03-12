palavra_secreta = "jogo da forca"
letras_corretas = []
letras_erradas = []
tentativas = 0
max_tentativas = 6

while tentativas < max_tentativas:
    print("\n--- JOGO DA FORCA ---")

    palavra_mostrada = ""
    for letra in palavra_secreta:
        if letra in letras_corretas or letra == " ":
            palavra_mostrada += letra
        else:
            palavra_mostrada += "."

    print("Palavra: ", palavra_mostrada)
    print("Letras erradas: ", letras_erradas)
    print("Tentativas restantes: ", max_tentativas - tentativas)

    if "." not in palavra_mostrada:
        print("Parabéns! Você descobriu a palavra.", palavra_secreta)
        break

    chute = input("Digite uma letra: ").lower()

    if chute in letras_corretas or chute in letras_erradas:
        print("Você já tentou essa letra! Tente outra.")
    elif chute in palavra_secreta:
        letras_corretas.append(chute)
        print("Boa! A letra", chute, "está na palavra!")
    else:
        letras_erradas.append(chute)
        tentativas += 1
        print("Errado! A letra", chute, "não está na palavra.")

if tentativas == max_tentativas:
    print("Fim de jogo! Você foi enforcado!")
    print("A palavra era:", palavra_secreta)

























