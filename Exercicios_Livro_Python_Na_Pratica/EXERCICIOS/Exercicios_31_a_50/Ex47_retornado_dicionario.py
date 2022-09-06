aluno = [{'Nome': 'Carlos','Notas':[62, 73, 90]}]

def calcular_medias(aluno):
    notas = []
    for media in aluno:
        if len(media['Notas']) > 0:
            temp = round(sum(media['Notas'])/len(media['Notas']))
        else:
            temp = 0
        notas.append({'Nomes': media['Nome'],'Media das notas': temp})
    print(notas)
media_estudante = calcular_medias(aluno)