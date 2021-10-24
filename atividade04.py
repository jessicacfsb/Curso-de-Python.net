#datas atuais:

from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#criar uma data:
lancamento_app = datetime(2022, 11, 22)
print(lancamento_app)

#usuário digita a data no sistema
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'), '%d%m%Y')
print(data_de_lancamento)

#calcular o intervalo entre datas
data_atual = datetime.now()
prazo = lancamento_app - data_atual
print(prazo.days)
