import pyautogui
from time import sleep
import random
import winsound
from datetime import datetime

print(
    'Iniciando captura dos campos e botões na tela. Após iniciado não oculte, mova ou feche a tela do browser até a finalização da compra.'
)

with open('cupons.txt') as file:
    cupons = [cupons.strip() for cupons in file]

print('Cupons a serem utilizados: ', cupons)

# cupons = numpy.array([
#     'superdicas20', 'chinacupon20', 'alitec20', 'importchina20', '2021ali20',
#     'sav20', 'alipay20', 'awintop20', 'cupomvalido20'
# ])

pyautogui.FAILSAFE = 0

print(pyautogui.locateCenterOnScreen('codigo_promo.png'))

print('Capturando as coordenadas do campo "Código Promocional" na tela...')
try:
    # capturando coordenadas do campo codigo promocional
    x, y = pyautogui.locateCenterOnScreen('codigo_promo.png')
except:
    print(
        'ERRO: Não foi possível localizar o campo "Código Promocional" na tela.'
    )
    exit()

print('Capturando as coordenadas do botão "Utilizar" na tela...')
try:
    a, b = pyautogui.locateCenterOnScreen('utilizar.png')
except:
    print('ERRO: Não foi possível localizar o botão "Utilizar" na tela.')
    exit()

print('Capturando as coordenadas do botão "Fazer Pedido" na tela...')
try:
    c, d = pyautogui.locateCenterOnScreen('fazer.png')
except:
    print('ERRO: Não foi possível localizar o botão "Fazer Pedido" na tela.')
    exit()

while True:
    print(
        datetime.now(),
        'Verificando se houve mudança no valor total, ou seja, se o cupom foi aplicado'
    )
    # enquanto valor total não mudar
    try:
        TOTAL = pyautogui.locateOnScreen('total.png')
    except:
        print(
            'ERRO: Não foi possível localizar a informação do total do pedido na tela'
        )
        exit()

    if TOTAL:
        print(datetime.now(), 'Valor do total não mudou, aplicar o cupom')

        print(datetime.now(), 'Clicar no campo do codigo promocional')
        try:
            pyautogui.click(x, y)
        except:
            print(
                'ERRO: Não foi possível localizar o campo "Código Promocional" na tela'
            )
            exit()

        print(datetime.now(), 'Sorteando um dos cupons a ser utilizado')
        cupom = cupons[random.randint(0, len(cupons) - 1)]
        try:
            pyautogui.write(cupom)
            print(datetime.now(), 'Cupom utilizado: ', cupom)
        except:
            print('ERRO: Erro ao informar o cupom no campo código promocional')
            exit()

        print(datetime.now(), 'Clicar no botao "Utilizar"')
        try:
            pyautogui.click(a, b)
        except:
            print(
                'ERRO: Não foi possível localizar o botão "Utilizar" na tela')
            exit()

        sleep(1.5)
    else:
        # se o total mudar e por que consiguiu aplicar o cupon, clicar em fazer o pedido
        print(datetime.now(), 'Valor total do pedido mudou, fazer o pedido')
        winsound.Beep(2500, 1000)
        # pyautogui.click(c, d)
        print(datetime.now(), 'Pedido finalizado')
        winsound.Beep(2500, 1000)
        break
