class Item:
    """O molde para criar qualquer item do jogo."""
    def __init__(self, nome, tipo, raridade, efeito, valor_efeito):
        self.nome = nome
        self.tipo = tipo         # ex: "Arma", "Consumível"
        self.raridade = raridade # comum, incomum, raro, épico, mítico, lendário
        self.efeito = efeito     # ex: "Ataque", "Cura"
        self.valor_efeito = valor_efeito  # ex: 15 (pontos de dano ou cura)

    def __str__(self):
        return f"{self.nome} [{self.tipo}] -> Dá +{self.valor_efeito} de {self.efeito}"


class Inventario:
    """O gerenciador da mochila do jogador."""
    def __init__(self):
        self.itens = []  # Lista que armazena os objetos do tipo Item

    def adicionar_item(self, item):
        """Adiciona o item na mochila."""
        self.itens.append(item)
        print(f"Você guardou: {item.nome}")

    def mostrar_inventario(self):
        """Mostra o que o jogador está carregando."""
        print("\n=== SEU INVENTÁRIO ===")
        if not self.itens:
            print("Sua mochila está vazia.")
        else:
            for i, item in enumerate(self.itens, 1):
                print(f"{i}. {item}")
        print("======================\n")

    def usar_item(self, nome_do_item):
        """Procura o item pelo nome, aplica o efeito e o remove se for consumível."""
        for item in self.itens:
            if item.nome.lower() == nome_do_item.lower():
                print(f"Você usou {item.nome}!")
                print(f"Efeito aplicado: +{item.valor_efeito} de {self.efeito_texto(item.efeito)}")
                
                # Se for consumível (como uma poção), ele some após o uso
                if item.tipo == "Consumível":
                    self.itens.remove(item)
                    print(f"{item.nome} foi consumido e sumiu do inventário.")
                return
        
        print(f"❌ Você não tem o item '{nome_do_item}' no inventário.")

    def efeito_texto(self, efeito):
        """Apenas uma função auxiliar para deixar o texto bonito."""
        substituicoes = {"Ataque": "Dano no próximo golpe", "Cura": "Vida recuperada"}
        return substituicoes.get(efeito, efeito)


# ==========================================
# TESTANDO O SISTEMA NO TERMINAL
# ==========================================

# 1. Iniciamos a mochila
mochila = Inventario()

# 2. Criamos os itens do jogo (sem peso e sem durabilidade)
espada = Item("Espada de Bronze", "Arma", "Comum", efeito="Ataque", valor_efeito=10)
pocao_vida = Item("Poção de Vida", "Consumível", "Comum", efeito="Cura", valor_efeito=25)

# 3. Jogador encontra os itens no mapa
mochila.adicionar_item(espada)
mochila.adicionar_item(pocao_vida)

# 4. Olhando a mochila
mochila.mostrar_inventario()

# 5. Jogador decide usar a Poção de Vida
mochila.usar_item("Poção de Vida")

# 6. Olhando a mochila de novo (a poção sumiu, a espada continua)
mochila.mostrar_inventario()
