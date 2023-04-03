class Veiculo:
    def __init__(self, placa, modelo, ano, cor):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


class TabelaHash:
    def __init__(self):
        self.tamanho = 29
        self.tabela = [None] * self.tamanho

    def funcao_hash(self, placa):
        soma = 0
        for letra in placa:
            soma += ord(letra)
        return soma % self.tamanho

    def inserir(self, veiculo):
        indice = self.funcao_hash(veiculo.placa)
        while self.tabela[indice] is not None and self.tabela[indice].placa != veiculo.placa:
            indice = (indice + 1) % self.tamanho
        if self.tabela[indice] is None or self.tabela[indice].placa == veiculo.placa:
            self.tabela[indice] = veiculo

    def buscar(self, placa):
        indice = self.funcao_hash(placa)
        while self.tabela[indice] is not None:
            if self.tabela[indice].placa == placa:
                return self.tabela[indice]
            indice = (indice + 1) % self.tamanho
        return None

    def excluir(self, placa):
        indice = self.funcao_hash(placa)
        while self.tabela[indice] is not None:
            if self.tabela[indice].placa == placa:
                self.tabela[indice] = Veiculo(None, None, None, None)  # lazy deletion
                return
            indice = (indice + 1) % self.tamanho

    def exibir(self):
        for i in range(self.tamanho):
            if self.tabela[i] is not None and self.tabela[i].placa is not None:
                print(f"Posição {i}: {self.tabela[i].placa} - {self.tabela[i].modelo} {self.tabela[i].cor} ({self.tabela[i].ano})")


# Exemplo de uso
tabela = TabelaHash()

while True:
    print("\nEscolha uma opção:\n")
    print("1 - Inserir veículo")
    print("2 - Buscar veículo")
    print("3 - Excluir veículo")
    print("4 - Exibir tabela hash")
    print("0 - Sair")
    opcao = int(input("\nOpção escolhida: "))

    if opcao == 1:
        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        ano = int(input("Digite o ano do veículo: "))
        veiculo = Veiculo(placa, modelo, ano, cor)
        
        veiculo_encontrado = tabela.buscar(placa)
        if veiculo_encontrado is not None and veiculo_encontrado.placa == placa:
            print("Placa já existente na tabela!")
        else:
            tabela.inserir(veiculo)
            print("Veículo inserido com sucesso!")

    elif opcao == 2:
        placa = input("Digite a placa do veículo: ")
        veiculo = tabela.buscar(placa)
        if veiculo is not None:
            print(f"Placa: {veiculo.placa}")
            print(f"Modelo: {veiculo.modelo}")
            print(f"Cor: {veiculo.cor}")
            print(f"Ano: {veiculo.ano}")
        else:
            print("Veículo não encontrado na tabela!")

    elif opcao == 3:
        placa = input("Digite a placa do veículo a ser excluído: ")
        tabela.excluir(placa)

    elif opcao == 4:
        tabela.exibir()

    elif opcao == 0:
        break

    else:
        print("Opção inválida!")