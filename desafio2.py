def maior_letra():
    frase = input("Digite uma frase: ").lower()
    maximo = ''
    for i in frase:
        if i.isalpha():
            if i > maximo:
                maximo = i
        else:
            return f"Digite somente letras"
            
    return maximo

print(maior_letra())