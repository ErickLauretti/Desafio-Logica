def formata_nome():
    nome = input("Digite um nome: ").split()
    ultimo_nome = nome[-1].upper()
    primeira_letra = [nomes[0].upper() for nomes in nome[:-1]]
    return f"{ultimo_nome}, " + ". ".join(primeira_letra) + "."
print(formata_nome())
