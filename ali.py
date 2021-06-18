import pyautogui
from pyautogui import locateOnScreen as LoS
from time import sleep
import numpy
import random
import winsound
from datetime import datetime

cupons = numpy.array([
    'superdicas20', 'chinacupon20', 'alitec20', 'importchina20', '2021ali20',
    'sav20', 'alipay20', 'awintop20', 'cupomvalido20'
])

# dados para emitir o beep quando aplicar o cumpom. 
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

pyautogui.FAILSAFE = 0

sleep(2)
# capturando coordenadas do campo codigo promocional
x, y = pyautogui.locateCenterOnScreen('codigo_promo.png')

# capturando coordenadas do campo botão utilizar
a, b = pyautogui.locateCenterOnScreen('utilizar.png')

c, d = pyautogui.locateCenterOnScreen('fazer.png')

while True:
    # enquanto valor total não mudar
    TOTAL = LoS('total.png', confidence=0.8)
    print('Coordenadas do Total: ', TOTAL)

    if TOTAL:
        print(datetime.now(),'clicar no campo do codigo promocional')
        pyautogui.click(x, y)
        # pyautogui.click('capture.png')

        pyautogui.write(cupons[random.randint(1, len(cupons)-1)])

        print(datetime.now(),'clicar no botao utilizar')
        pyautogui.click(a, b)
        sleep(1)
    else:
        # se o total mudar e por que consiguiu aplicar o cupon, clicar em fazer o pedido
        print(datetime.now(),'valor total mudou, fazer o pedido')
        winsound.Beep(frequency, duration)
        pyautogui.click(c, d)
        print(datetime.now(),'pedido finalizado')
        winsound.Beep(frequency, duration)
        break
