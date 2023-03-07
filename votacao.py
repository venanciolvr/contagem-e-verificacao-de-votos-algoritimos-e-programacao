print('Escolha uma das seguintes opções: Candidato 1, 2, 3 ou 4. Ou selecione 5 para voto nulo ou 6 para voto branco.')

stephanie = 0
ryan = 0
levi = 0
rafael = 0

nulo = 0
branco = 0

contador = 0

while(contador <= 4):

    voto = int(input('Qual o seu voto? '))

    if(voto == 1):
        print('Você votou em Stephanie.')
        stephanie += 1
    elif(voto == 2):
        print('Você voteu em Ryan.')
        ryan += 1
    elif(voto == 3):
        print('Você votou em Levi.')
        levi += 1
    elif(voto == 4):
        print('Você votou em Rafael.')
        rafael += 1
    elif(voto == 5):
        print('Você votou nulo.')
        nulo += 1
    elif(voto == 6):
        print('Você votou branco.')
        branco += 1
    else:
        print('Opção não existe! Digite novamente.')

    contador += 1

finalizar = ''

while(finalizar != 0):

    finalizar = int(input('Finalizar votação? (Digite 0 para finalizar) '))

    if(finalizar == 0):
        print('Votação finalizada')
    else:
        print('Votação não finalizada.')

if(stephanie == 0):
    print(f'Stephanie tem {stephanie} votos.')
elif(stephanie == 1):
    print(f'Stephanie tem {stephanie} voto.')
elif(stephanie >=2):
    print(f'Stephanie tem {stephanie} votos.')

if(ryan == 0):
    print(f'Ryan tem {ryan} votos.')
elif(ryan <= 1):
    print(f'Ryan tem {ryan} voto.')
elif(ryan >= 2):
    print(f'Ryan tem {ryan} votos')

if(levi == 0):
    print(f'Levi tem {levi} votos.')    
elif(levi == 1):
    print(f'Levi tem {levi} voto.')
elif(levi >= 2):
    print(f'Levi tem {levi} votos.')

if(rafael == 0):
    print(f'Rafael tem {rafael} votos.')
elif(rafael == 1):
    print(f'Rafael tem {rafael} voto.')
elif(rafael >= 2):
    print(f'Rafael tem {rafael} votos.')

if(nulo == 0):
    print(f'{nulo} votos nulo.')
elif(nulo == 1):
    print(f'{nulo} voto nulo.')
elif(nulo >= 2):
    print(f'{nulo} votos nulo.')

if(branco == 0):
    print(f'{branco} votos em branco.')
elif(branco == 1):
    print(f'{branco} voto em branco.')
elif(branco >= 2):
    print(f'{branco} votos em branco.')

if(stephanie > ryan) or (stephanie > levi) or (stephanie > rafael):
    print('Stephanie é a nova presidente!')
elif(ryan > stephanie) and (ryan > levi) and (ryan > rafael):
    print('Ryan é o novo presidente!')
elif(levi > stephanie) and (levi > ryan) and (levi > rafael):
    print('Levi é o novo presidente!')
elif(rafael > stephanie) and (rafael > ryan) and (rafael > levi):
    print('Rafael é o novo presidente!')
elif(nulo == 5):
    print('Todos os votos foram nulos.')
else:
    print('Será necessário um 2º turno de votações.')