import time
from utils import limpar_tela

def pontos_atributos(personagem, pontos_disponiveis):
    """
    Distribui pontos para o personagem. 
    Pode ser chamada na criação ou em um Level Up futuro.
    """
    # Lista dos atributos que podem receber pontos
    atributos_para_distribuir = ["hp", "forca", "defesa", "velocidade", "destreza", "sorte"]
    
    while pontos_disponiveis > 0:
        for atributo in atributos_para_distribuir:
            if pontos_disponiveis <= 0:
                break
                
            while True:
                print(f"\n--- Pontos Disponíveis: {pontos_disponiveis} ---")
                try:
                    pts = int(input(f"Quantos pontos para {atributo.upper()}? : "))
                    
                    if 0 <= pts <= pontos_disponiveis:
                        personagem[atributo] += pts
                        pontos_disponiveis -= pts
                        break  # Sai do loop de validação e vai para o próximo atributo
                    else:
                        print(f"Quantidade inválida! Escolha um valor entre 0 e {pontos_disponiveis}.")
                        time.sleep(1)
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")
                    time.sleep(1)
                    
        # Se após passar por todos os atributos ainda sobrarem pontos, avisa o jogador
        if pontos_disponiveis > 0:
            print("\nVocê ainda possui pontos restantes! Vamos redistribuir o que sobrou.")
            time.sleep(1.5)
                
    # Atualiza o HP Máximo caso o HP base tenha subido
    personagem["hp_maximo"] = personagem["hp"]
    return personagem


def criar_personagem():
    print("--- CRIAÇÃO DE PERSONAGEM ---")
    
    # Validação do nome
    while True:
        nome = input("Digite o nome do seu herói: ").strip()
        if nome:
            break
        print("O nome do herói não pode ficar em branco! Tente novamente.\n")
    
    # Estrutura base do personagem
    personagem = {
        "nome": nome,
        "classe": "",
        "hp": 20,
        "hp_maximo": 20,
        "forca": 0,
        "defesa": 0,
        "velocidade": 0,
        "destreza": 0,
        "sorte": 0,
        "pocoes": 1
    }
    
    pontos_iniciais = 20
    print(f"\nVocê tem {pontos_iniciais} pontos extras para distribuir (Você já possui 20 de HP).")
    time.sleep(1)
    
    # Chama a função separada passando o dicionário criado
    personagem = pontos_atributos(personagem, pontos_iniciais)
    
    limpar_tela()
    print("\nAgora escolha sua classe...")
    time.sleep(0.5)
    print("Você pode ser um Guerreiro")
    time.sleep(0.5)
    print("Você pode ser um Mago")
    time.sleep(0.5)
    print("Ou...")
    time.sleep(1)
    print("......")
    time.sleep(1.5)
    print("Você pode ser um Bardo...\n")
    time.sleep(1)
    
    # Escolha de Classe
    while True:
        classe = input("Eai, qual vai ser? \n \n [1] Guerreiro \n [2] Mago \n [3] Bardo \n \n").strip()
        
        if "1" in classe:
            print("\nÓtimo, você herdou uma espada do seu pai e agora você possui mais 3 pontos de força\n e mais 2 pontos de defesa!")
            personagem["classe"] = "Guerreiro"
            personagem["forca"] += 3
            personagem["defesa"] += 2
            time.sleep(1)
            break
        elif "2" in classe:
            print("\nMaravilha, sua mãe fez um feitiço e agora você possui mais 3 pontos de defesa\n e mais 2 pontos de velocidade!")
            personagem["classe"] = "Mago"
            personagem["defesa"] += 3
            personagem["velocidade"] += 2
            time.sleep(1)
            break
        elif "3" in classe:
            print("\nQue escolha estranha...")
            time.sleep(1)
            print("\nPois bem toma mais 3 pontos de sorte e 2 pontos de destreza\n haja o que houver!")
            personagem["classe"] = "Bardo"
            personagem["sorte"] += 3
            personagem["destreza"] += 2
            time.sleep(1)
            break
        else:
            print("Classe inválida, escolha uma das opções disponíveis.\n")
            time.sleep(1)
            
    input("\nPressione ENTER para avançar...")
    limpar_tela()
    
    return personagem

def exibir_ficha(heroi):
    ficha = f"""
=============================
       {heroi['nome']}
=============================
Classe:     {heroi['classe']}
HP:         {heroi['hp']}/{heroi['hp_maximo']}
Força:      {heroi['forca']}
Defesa:     {heroi['defesa']}
Velocidade: {heroi['velocidade']}
Destreza:   {heroi['destreza']}
Sorte:      {heroi['sorte']}
Poções:     {heroi['pocoes']}
=============================
"""
    print(ficha)