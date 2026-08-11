class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco

    def exibir(self):
        print(self.codigo, self.descricao, f"R$ {self.preco:.2f}")


class Restaurante:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cardapio = []

    def adicionar_produto(self, produto):
        self.cardapio.append(produto)

    def listar_cardapio(self):
        print("Cardápio")
        for produto in self.cardapio:
            produto.exibir()


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def exibir(self):
        print(self.nome, self.telefone, self.endereco)


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.situacao = "Aberto"

    def adicionar_item(self, produto, quantidade):
        if self.situacao == "Aberto":
            self.itens.append(ItemPedido(produto, quantidade))
        else:
            print("Não é possível adicionar itens.")

    def remover_item(self, codigo):
        if self.situacao == "Aberto":
            for item in self.itens:
                if item.produto.codigo == codigo:
                    self.itens.remove(item)
                    break

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.calcular_subtotal()
        return total

    def alterar_situacao(self, situacao):
        self.situacao = situacao

    def exibir_resumo(self):
        print("\nCliente:", self.cliente.nome)
        print("Situação:", self.situacao)
        for item in self.itens:
            print(
                item.produto.descricao,
                item.quantidade,
                f"Subtotal: R$ {item.calcular_subtotal():.2f}"
            )
        print(f"Total: R$ {self.calcular_total():.2f}")


restaurante = Restaurante("Sabor Caseiro", "Rua A")

p1 = Produto(1, "Hambúrguer", 25)
p2 = Produto(2, "Batata", 12)
p3 = Produto(3, "Refrigerante", 8)

restaurante.adicionar_produto(p1)
restaurante.adicionar_produto(p2)
restaurante.adicionar_produto(p3)

cliente1 = Cliente("João", "99999-1111", "Rua X")
cliente2 = Cliente("Maria", "99999-2222", "Rua Y")

pedido1 = Pedido(cliente1)
pedido1.adicionar_item(p1, 2)
pedido1.adicionar_item(p2, 1)
pedido1.alterar_situacao("Confirmado")
pedido1.adicionar_item(p3, 1)

pedido2 = Pedido(cliente2)
pedido2.adicionar_item(p3, 3)
pedido2.adicionar_item(p2, 2)
pedido2.alterar_situacao("Em preparação")

pedido1.exibir_resumo()
pedido2.exibir_resumo()