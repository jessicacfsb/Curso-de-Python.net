velocidade_do_carro = 70

if velocidade_do_carro >= 75:
    print(f'Sua velocidade é de: {velocidade_do_carro}Km/h, levou uma multa e 7 pontos na carteira!')
elif velocidade_do_carro >= 61 and velocidade_do_carro < 75:
    print(f'Sua velocidade é de: {velocidade_do_carro}Km/h, levou uma multa e 3 pontos na carteira!')
elif velocidade_do_carro >= 51 and velocidade_do_carro <= 60:
    print(f'Sua velocidade é de: {velocidade_do_carro}Km/h, levou uma multa e 2 pontos na carteira!')
else:
    print(f'Você está dentro da velocidade ´permitida!')