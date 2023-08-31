import time
autorizado = 1
rejeitado = 201
cancelado = 401
analise = 601

pedido = int(input('Informe o pedido :'))
#codigo = int(input('Informe o código de 1/5 : '))

def api():
    print('----------------------------------------')
    print('|--------------API---------------------|')
    if pedido > 1 and pedido < 200 and autorizado == 1:
        print('Pedido Autorizado !')
    elif pedido > 201 and pedido < 400 and rejeitado == 201:
        print('Pedido em Rejeitado')
    elif pedido > 401 and pedido < 600 and cancelado == 401:
        print('Pedido Cancelado')
    elif pedido > 601 and pedido < 800 and analise == 601:
        print('Pedido em Analise ')
    else:
        print(f'Pedido : {pedido} não existe !')    
api()

print('|--------------------------------------|')
print('|--------------HUB---------------------|')
def hub():
    if pedido > 1 and pedido < 200:
        print(f'Atualizando Pedido : {pedido}')
        time.sleep(2)
        print(f'Atualizando o pedido : {pedido} em Venda ')
        time.sleep(1)
        print(f'Vendo {pedido} Gravada com Sucesso !')
    elif pedido > 201 and pedido < 400:
        print(f'Atualizando Pedido : {pedido}')
        time.sleep(2)
        print(f'Corrija o pedido : {pedido} e tente novamente !')
    
    elif pedido >= 401 and pedido < 600:
        print(f'Atualizando Pedido: {pedido}')
        time.sleep(2)
        print(f'O pedido : {pedido} esta cancelado !')
    elif pedido >= 601 and pedido < 800:
        print(f'Atualizando :{pedido}')
        time.sleep(2)
        print(f'O pedido : {pedido} esta em analise no Hub !')
hub()

"""""
while pedido < 1000:
    print('|--------------------------------------|')
    print('|--------------Venda-------------------|')
    #pedido = int(input('Informe o pedido :'))
    api()
    time.sleep(1.5)
    hub()
    time.sleep(1.5)
    break
"""""
def venda():
    print('|--------Painel de Vendas----------|')
    print('|-----Gerenciamento de Vendas------|')
    time.sleep(1)
    print(f'Status da Venda : {pedido}')
    time.sleep(0.5)
    print(f'Granvado a Venda : {pedido}')
    n = 0
    for n in range(0 , 3):
        print(f'{n+1} : Atualizando')
        time.sleep(1)
        
    print(f'Venda : {pedido} Gravada!')
    time.sleep(1.5)
    print('|------------Emissão---------------|')
    print(f'Deseja Emitir a Venda : {pedido} ?')
    sim = 1
    sim = int(input('Digite 1 para SIM ou 2 para NÃO : '))
    print('|-----------Processanto------------|')
    if sim == 1:
        time.sleep(2)
        print(f'Emitindo a Venda : {pedido}')
        time.sleep(1)
    else:
        print(f'Emissão da Venda {pedido} Cancelada !')            
        time.sleep(3)
    if sim == 1:       
        print(f'Venda : {pedido} Autorizada !')
        time.sleep(1)
    elif sim ==2:
        print(f'Venda {pedido} Não Enviado !')
        time.sleep(1)
    print('|----------Finalizando------------|')
    time.sleep(0.5)
venda()
time.sleep(0.8)
print('')
print('|-------------Resumo---------------|')
print(f'Código da  Venda : {pedido}')

while pedido == pedido:
    print('|--------------------------------------|')
    print('|--------------Venda-------------------|')
    pedido = int(input('Informe o pedido :'))
    api()
    time.sleep(1.5)
    hub()
    time.sleep(1.5)
    venda()
