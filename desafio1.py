def calculo_media():
    nome = input("Escreva seu nome: ")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return f"Aluno = {nome} // Media = {media}"

print(calculo_media())