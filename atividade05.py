#condicionais
numero_atrasos = 2
if numero_atrasos >= 3:
    print('Você ultrapassou a quantidade permitida de atrasos! \nVá para a diretoria!')
elif numero_atrasos == 2:
    print('Esta é a sua segunda falta, na próxima você vai para a diretoria!')
elif numero_atrasos == 1:
    print('Essa é a sua primeira falta')
else:
    print('Pode entrar!')