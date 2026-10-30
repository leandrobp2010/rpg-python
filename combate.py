import random
import time
from utils import limpar_tela


def rolar_combate(heroi, inimigo):
  regeneracao_disponivel = True
  inimigo_hp = inimigo["hp"]
  inimigo_hp_max = inimigo_hp

  limpar_tela()
  print(f"\n--- UM ENCONTRO DE COMBATE (Fase {inimigo['fase']})! ---")
  time.sleep(1.5)

  limpar_tela()
  print(
      f"Um {inimigo['nome']} surge das sombras barulhentas da masmorra!"
  )
  time.sleep(1.5)

  limpar_tela()
  print("\n=============================")
  print(f"{inimigo['nome']}")
  print("=============================")
  time.sleep(1)
  print(f"HP:         {inimigo_hp}/{inimigo_hp_max}")
  print(f"Força:      {inimigo['forca']}")
  print(f"Defesa:     {inimigo['defesa']}")
  print(f"Sorte:      {inimigo['sorte']}")
  print("=============================\n")
  time.sleep(2)

  input("Pressione ENTER para iniciar a batalha...")
  limpar_tela()

  # Loop de Batalha por Turnos
  while heroi["hp"] > 0 and inimigo_hp > 0:
    limpar_tela()

    # Menu de Escolha de Ações do Jogador
    turno_ativo = True
    while turno_ativo:
      print(f"\n--- SEU TURNO ({heroi['nome']}) ---")
      print(
          f"HP: {heroi['hp']}/{heroi['hp_maximo']} | Poções:"
          f" {heroi['pocoes']} | Regeneração Disponível:"
          f" {'Sim' if regeneracao_disponivel else 'Não'}"
      )
      print(f"Inimigo: {inimigo['nome']} (HP: {inimigo_hp}/{inimigo_hp_max})")
      print("-" * 35)
      print("Escolha sua ação:")
      print("[1] Lutar")
      print("[2] Se curar")
      print("[3] Usar item")
      print("[4] Passar a rodada")

      acao = input("Digite o número da ação desejada: ").strip()

      if acao == "1":
        # 1. LUTAR
        dado_jogador = random.randint(1, 20)
        poder_ataque_jogador = (
            dado_jogador + heroi["sorte"] + heroi["forca"]
        )
        print(f"\n[SEU TURNO] Você rolou um D20 e tirou: {dado_jogador}")
        time.sleep(1)
        print(
            f">> Total do seu Ataque ({dado_jogador} + {heroi['sorte']} Sorte +"
            f" {heroi['forca']} Força): {poder_ataque_jogador}"
        )

        time.sleep(1)
        if poder_ataque_jogador > inimigo["defesa"]:
          dano_no_hp = poder_ataque_jogador - inimigo["defesa"]
          inimigo_hp -= dano_no_hp
          print(
              f">> O ataque quebrou a Defesa do inimigo e causou {dano_no_hp} de"
              " dano direto no HP!"
          )
        else:
          print(">> O inimigo conseguiu defender seu ataque com os escudos!")

        turno_ativo = False
        break

      elif acao == "2":
        # 2. SE CURAR (REGENERAÇÃO)
        if not regeneracao_disponivel:
          print("\n[AVISO] Você já utilizou a regeneração nesta batalha!")
          time.sleep(1.5)
          limpar_tela()
          continue

        if heroi["hp"] >= heroi["hp_maximo"]:
          print("\n[AVISO] Seu HP já está no máximo!")
          time.sleep(1.5)
          limpar_tela()
          continue

        dado_cura = random.randint(1, 6)
        cura_total = (heroi["velocidade"] + heroi["destreza"] + dado_cura) // 2
        heroi["hp"] += cura_total

        if heroi["hp"] > heroi["hp_maximo"]:
          heroi["hp"] = heroi["hp_maximo"]

        regeneracao_disponivel = False
        print(
            "\n[RECUPERAÇÃO] Fôlego em combate! (Vel:"
            f" {heroi['velocidade']} + Des: {heroi['destreza']} + D6:"
            f" {dado_cura}) / 2"
        )
        print(
            f">> Você recuperou +{cura_total} de HP! (HP"
            f" atual: {heroi['hp']}/{heroi['hp_maximo']})"
        )

        turno_ativo = False
        break

      elif acao == "3":
        # 3. USAR ITEM (POÇÃO)
        if heroi["pocoes"] <= 0:
          print("\n[AVISO] Você não possui poções em seu inventário!")
          time.sleep(1.5)
          limpar_tela()
          continue

        if heroi["hp"] >= heroi["hp_maximo"]:
          print("\n[AVISO] Seu HP já está no máximo!")
          time.sleep(1.5)
          limpar_tela()
          continue

        heroi["pocoes"] -= 1
        cura_pocao = 15
        heroi["hp"] += cura_pocao
        if heroi["hp"] > heroi["hp_maximo"]:
          heroi["hp"] = heroi["hp_maximo"]

        print(
            f"\n[ITEM] Você bebeu uma Poção de Cura e recuperou +{cura_pocao} de"
            f" HP! (HP atual: {heroi['hp']}/{heroi['hp_maximo']})"
        )
        turno_ativo = False
        break

      elif acao == "4":
        # 4. PASSAR A RODADA
        print(
            f"\n[ESPERA] {heroi['nome']} adota uma postura defensiva e passa o"
            " turno..."
        )
        turno_ativo = False
        break

      else:
        print("\n[ERRO] Opção inválida! Escolha um número entre 1 e 4.")
        time.sleep(1.5)
        limpar_tela()

    time.sleep(1.5)

    # Verifica se o inimigo morreu
    if inimigo_hp <= 0:
      print(f"\n[VITÓRIA] O {inimigo['nome']} foi derrotado por {heroi['nome']}!")
      input("\nPressione ENTER para avançar...")
      return True

    print(f"Vida restante do {inimigo['nome']}: {max(0, inimigo_hp)}")
    time.sleep(1)

    input("\nPressione ENTER para aguentar o turno do inimigo...")
    limpar_tela()

    # TURNO DO INIMIGO ATACAR
    dado_inimigo = random.randint(1, 20)
    poder_ataque_inimigo = (
        dado_inimigo + inimigo["sorte"] + inimigo["forca"]
    )
    print(
        f"\n[{inimigo['nome']} ATACA] O inimigo rolou um D20 e tirou:"
        f" {dado_inimigo}"
    )
    time.sleep(1)
    print(
        f">> Total do Ataque do Inimigo ({dado_inimigo} + {inimigo['sorte']}"
        f" Sorte + {inimigo['forca']} Força): {poder_ataque_inimigo}"
    )

    time.sleep(1)
    if poder_ataque_inimigo > heroi["defesa"]:
      dano_no_jogador = poder_ataque_inimigo - heroi["defesa"]
      heroi["hp"] -= dano_no_jogador
      print(
          f">> O inimigo superou sua Defesa ({heroi['defesa']}) e tirou"
          f" {dano_no_jogador} do seu HP!"
      )
    else:
      print(
          f">> Sua robusta Defesa ({heroi['defesa']}) bloqueou completamente"
          " o golpe do monstro!"
      )

    print(f"Seu HP restante: {max(0, heroi['hp'])}")
    time.sleep(1.5)

    if heroi["hp"] <= 0:
      return False

  return heroi["hp"] > 0