total_alunos = int(input("Quantidade de alunos: "))
soma_media = 0

for i in range(total_alunos):
    nome_aluno = input("Digite o nome do aluno: ")
    
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    
    media_nota = (n1 + n2 + n3) / 3
    soma_media += media_nota

    if media_nota >= 7:
        print(f"\nNome do aluno: {nome_aluno} \nPrimeira nota: {n1}\nSegunda nota: {n2}\nTerceira nota: {n3}\nMédia do aluno: {media_nota:.2f}\nSituação do aluno: APROVADO\n")
    else:
        print(f"\nNome do aluno: {nome_aluno} \nPrimeira nota: {n1}\nSegunda nota: {n2}\nTerceira nota: {n3}\nMédia do aluno: {media_nota:.2f}\nSituação do aluno: REPROVADO\n")

media_geral = soma_media / total_alunos

print(f"Média geral da turma: {media_geral:.2f}")