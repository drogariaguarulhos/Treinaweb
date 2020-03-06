from carro import *

auto = Carro('Calhanbeque','Ferrugem', 1, 'Gosolina', 30, 40)
numero = 0
print('Simulador de Pilotagem do Away')
letra = ''
erro = False
while letra != 'S':
    situacao = 'DESLIGADO'
    if auto.is_ligado and not auto.is_andando:
        situacao = 'LIGADO MAIS PARADO'
    elif auto.is_ligado and auto.is_andando:
        situacao = 'LIGADO ANDANDO'
    if not erro and auto.is_esporro:
        print(auto.esporro)
        auto.is_esporro = False
    elif erro:
        print('Escolha uma Opção Badernista:\n(L)igar\n(D)esligar\n(A)ndar\n(R)eabastecer\n(C)ontinuar\n(S)air')
        erro = False
    else:
        auto.status()
        print(f'Modelo: {auto.modelo} Cor: {auto.cor} Combustivel: {auto.tipo_combustivel}')
        print(f'Portas: {auto.qtd_portas} Potencia do Motor: {auto.potencia:6.2f} ')
        print(f'Situação do Carro: {situacao} Nivel de combustivel: {auto.qtd_combustivel:6.2f}')
        print('Escolha uma Opção Badernista:\n(L)igar\n(D)esligar\n(A)ndar\n(P)arar\n(R)eabastecer\n(C)ontinuar\n(S)air')
        if auto.is_esporro:
            print(auto.esporro)
            auto.is_esporro = False

    letra = input('Opção: ').upper()
    if letra == 'L':
        auto.ligar()
    elif letra == 'D':
        auto.desligar()
    elif letra == 'A':
        auto.andar()
    elif letra == 'P':
        auto.parar()
    elif letra == 'R':
        erro = True
        while erro:
            try:
                qtde = float(input('Quantidade de Gasolina Animal: '))
                auto.abastecer(qtde)
                erro = False
            except ValueError:
                erro = True
                print('Seu faz direiro essa Merda!'.upper())
    elif letra == 'S':
        if auto.is_andando:
            erro = True
            print('Que Merda é Essa Vai Sair com carro Andando?'.upper())
            letra = ''
        elif auto.is_ligado:
            erro = True
            print('Jumento o carro Ainda ta ligado!'.upper())
            letra = ''
    elif letra == 'C':
        if not auto.is_ligado and not auto.is_andando:
            erro = True
            print('Liga o Carro Primeiro energumeno!'.upper())
        elif auto.is_ligado and not auto.is_andando:
            erro = True
            print('Bota essa porra pra andar ne filah da puta!'.upper())
        elif not auto.is_esporro:
            for y in range(0, 200):
                print('\n')
    else:
        if numero > 2:
            for y in range(0, 200):
                print('\n')
            print('FILAH DA PUTA!!!\nPARA COM ESSA PORRA AI\nUM BANDO DE BADERNISTA')
            print('TUDO CRIADO COM LEITE DE PERA, OVOMALTINO\nVIM PRA CA PENSANDO QUE IA ME DA BEM')
            print('ESSES FILHA DA PUTA DE MOTORISTA NUM GUENTA 10 MINUTO DE PORRADA COMIGO!')
            break
        else:
            if numero == 0:
                erro = True
                print('Presta Atenção Le Direiro esss Merda!'.upper())
            elif numero == 1:
                erro = True
                print('Seu Jumento Le Direito essa Merda!'.upper())
            elif numero == 2:
                erro = True
                print('Mais que Porra ate Quando vai Fazer Merda!'.upper())
            numero += 1
else:
    for y in range(0, 200):
        print('\n')
    print('Ate que Enfim Terminou essa Porra!\n\n'.upper())

