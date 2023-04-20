while True: 
    try:
        numero = int(input('Entre com um numero'))
        print(numero/2)
        
    except:
        print('O numero que voce entrou nao e valido. Tente novamente')