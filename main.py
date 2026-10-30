import time
from combate import rolar_combate
from inimigos import FASES_JOGO
from personagem import criar_personagem
from personagem import exibir_ficha
from utils import limpar_tela

# 1. Criação do Herói
heroi = criar_personagem()

limpar_tela()
exibir_ficha(heroi)
time.sleep(2)

input("Pressione ENTER para entrar na masmorra...")

# 2. Loop pelas Fases do Jogo
for inimigo_atual in FASES_JOGO:
  vitoria = rolar_combate(heroi, inimigo_atual)

  if not vitoria:
    limpar_tela()
    print(
        f"\n[FIM DE JOGO] {heroi['nome']} caiu em combate na Fase"
        f" {inimigo_atual['fase']}... A masmorra venceu."
    )
    break
  else:
    limpar_tela()
    if inimigo_atual["fase"] < len(FASES_JOGO):
      print(
          f"\n[AVENTURA] Com o {inimigo_atual['nome']} derrotado, {heroi['nome']}"
          " avança para o próximo nível da masmorra..."
      )
      print("🎁 Recompensa: Você encontrou mais 1 Poção de Cura!")
      heroi["pocoes"] += 1
      exibir_ficha(heroi)
      time.sleep(3)
    else:
      print(
          f"\n[VITÓRIA LENDÁRIA!] {heroi['nome']} desferiu o golpe final no"
          f" {inimigo_atual['nome']}!"
      )
      print(
          f"Com a escuridão dissipada, {heroi['nome']} conquista o grande"
          " tesouro da masmorra e se torna uma lenda viva!"
      )