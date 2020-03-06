class Carro():
    def __init__(self, modelo, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel):
        self.modelo = modelo
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = False
        self.is_andando = False
        self.is_esporro = False
        self.esporro = ''

    def status(self):
        self.is_esporro = False
        if self.is_ligado == True and self.is_andando == True:
            if self.qtd_combustivel <= 0:
                self.is_esporro = True
                self.esporro = 'mais que Porra é essa Eu Te Avisei pra Reabastecer'.upper()
                self.is_andando = False
                self.is_ligado = False
            else:
                if self.qtd_combustivel <= 15:
                    self.is_esporro = True
                    self.esporro = 'Fica de Olho Nessa Merda ta Acabando a Gazoza'.upper()
                self.qtd_combustivel -= 5

    def abastecer(self, qtde):
        self.is_esporro = False
        if qtde <= 0:
            self.is_esporro = True
            self.esporro = 'Como Ainda te Aguento Animal já viu Reabastercer 0'.upper()
        else:
            self.qtd_combustivel += qtde

    def ligar(self):
        self.is_esporro = False
        if self.qtd_combustivel <= 0:
            self.is_esporro = True
            self.esporro = 'Seu Energumeno tem que Colocar a Porra da Gasolina pra Ligar o Carro!'.upper()
        elif self.is_andando == True:
            self.is_esporro = True
            self.esporro = 'Seu Merdinha o carro já ta Andando pra que Você quer Ligar!'.upper()
        elif self.is_ligado == False:
            self.is_ligado = True
        else:
            self.is_esporro = True
            self.esporro = 'Seu Bosta o Carro já ta Ligado Porra!'.upper()

    def desligar(self):
        self.is_esporro = False
        if self.is_andando:
            self.is_esporro = True
            self.esporro = 'Seu Bosta Você vai Desligar o carro em Movimento!'.upper()
        elif self.is_ligado:
            self.is_ligado = False
        else:
            self.is_esporro = True
            self.esporro = 'Seu Bosta o Carro já ta Desligado Porra!'.upper()

    def andar(self):
        self.is_esporro = False
        if self.qtd_combustivel <= 0:
            self.is_esporro = True
            self.esporro = 'Você é uma Anta seu Porra tem que Abastecer!'.upper()
        elif not self.is_ligado:
            self.is_esporro = True
            self.esporro = 'Mais tu e Burro Mesmo o Carro ta Desligado!'.upper()
        elif self.is_andando:
            self.is_esporro = True
            self.esporro = 'Seu Merdinha o carro já ta Andando!'.upper()
        else:
            self.is_andando = True

    def parar(self):
        self.is_esporro = False
        if not self.is_ligado:
            self.is_esporro = True
            self.esporro = 'Se nem Ligo essa Merda como Quer Parar Imbecil!'.upper()
        elif not self.is_andando:
            self.is_esporro = True
            self.esporro = 'Seu Jumento o carro já ta Parado'.upper()
        else:
            self.is_andando = False
