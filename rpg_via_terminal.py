import os
import random
import time

def tela_inicial():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("#" * 40)
    print("#          RPG via Terminal            #")
    print("#" * 40)
    print("\nCaro Aventureiro! Seja bem-vindo ao RPG via Terminal!")
    print("Selecione uma opção abaixo:")
    print("\n1. Jogar")
    print("2. Sair")

def menu_selecao_personagem():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 40)
    print("#          RPG via Terminal            #")
    print("#" * 40)
    print("\nMenu de Seleção de Personagem")
    print("\nEscolha seu personagem:")
    print("1. Rodolf, Guerreiro")
    print("2. Sypha, Feiticeira")
    print("3. Astarion, Ladino")
    print("\n0. Voltar ao Menu")

class Personagem:
    def __init__(self, nome, classe, hp, ataque, stamina_mp, historia):
        self.nome = nome
        self.classe = classe
        self.hp_original = hp
        self.hp = hp
        self.ataque = ataque
        self.stamina_mp_original = stamina_mp
        self.stamina_mp = stamina_mp
        self.historia = historia
        
    def exibir_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#" * 40)
        print("#          RPG via Terminal            #")
        print("#" * 40)
        print(f"\nStatus de {self.nome}:")
        print(f"\nClasse: {self.classe}")
        print(f"HP: {self.hp}")
        print(f"Ataque Base: {self.ataque}")
        print(f"Stamina/MP: {self.stamina_mp}")
        print(f"\nHistória:\n{self.historia}")
        
def epilogo(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 40)
    print("#          RPG via Terminal            #")
    print("#" * 40)
    print(f"\nNa cidade de Eldoria, rumores ecoam sobre uma masmorra perdida cheia de perigos e tesouros inimagináveis.")
    time.sleep(3)
    print(f"{personagem.nome} ouve falar sobre a masmorra e decide aceitar o desafio.")
    time.sleep(3)
    print(f"Equipado com sua coragem, {personagem.nome} parte em direção à entrada da masmorra, conhecida como 'O Abismo Sombrio'.")
    time.sleep(3)
    print(f"A atmosfera ao redor da entrada é gélida e o ar está impregnado com uma sensação de desespero.")
    time.sleep(3)
    print(f"As sombras se estendem pelo solo enquanto {personagem.nome} adentra as profundezas do Abismo Sombrio, onde apenas os corajosos ou tolos ousam entrar.")
    time.sleep(3)
    input("\nPressione Enter para começar a sua jornada...\n")

class Monstro:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
    
    def introducao_goblin_verde(cls, personagem):
        print(f"{personagem.nome} avança por um corredor úmido e escuro, iluminado apenas pela luz tênue de sua tocha.")
        time.sleep(3)
        print(f"O cheiro de mofo paira no ar, e {personagem.nome} ouve sons furtivos à medida que se aproxima.")
        time.sleep(3)
        print(f"Ao virar a esquina, {personagem.nome} se depara com uma figura pequena, mas ameaçadora:")
        time.sleep(3)
        print("um Goblin Verde, com olhos ardilosos e presas afiadas, pronto para o confronto!")
        time.sleep(3)
        input("\nPressione Enter para começar a batalha!\n")
    
    def introducao_cavaleiro_esqueleto(cls, personagem):
        print(f"{personagem.nome} avança pelo corredor escuro, o som dos seus passos ecoando nas paredes úmidas da masmorra.")
        time.sleep(3)
        print("A luz fraca de sua tocha ilumina o caminho à frente, revelando antigas inscrições nas paredes de pedra.")
        time.sleep(3)
        print(f"Ao virar a esquina, {personagem.nome} é surpreendido por um arrepio na espinha.")
        time.sleep(3)
        print(f"Um gélido vento passa por {personagem.nome}, trazendo consigo o som metálico de correntes arrastando-se pelo chão de pedra.")
        time.sleep(3)
        print(f"Diante de {personagem.nome}, emerge das sombras um Cavaleiro Esqueleto, vestindo o que resta de sua armadura, com uma espada enferrujada em mãos.")
        time.sleep(3)
        print(f"Seus olhos vazios fixam-se em {personagem.nome}, revelando uma fome insaciável por batalha e almas perdidas.")  
        time.sleep(3)
        input("\nPressione Enter para enfrentar o Cavaleiro Esqueleto!\n")

    def introducao_ogro_sedento(cls, personagem):
        print(f"A medida que {personagem.nome} adentra neste pesadelo, uma presença maligna enche o corredor da masmorra.")
        time.sleep(3)
        print(f"Um ar pesado paira no ar, e as sombras ao redor se unem com a sua presença...")
        time.sleep(3)
        print(f"De repente, emerge das trevas um ser colossal, coberto de sujeira e sangue, um verdadeiro terror conhecido como Ogro Sedento!")
        time.sleep(3)
        print(f"Seus olhos brilham com uma sede insaciável por destruição, e um rosnado gutural ressoa pela masmorra, ecoando o terror que está prestes a se desencadear.")
        time.sleep(3)
        input("\nPressione Enter para enfrentar o Ogro Sedento...\n")

    def introducao_mimico(cls, personagem):
        print(f"Após atravessar os corredores sinuosos da masmorra, {personagem.nome} finalmente chega a uma sala iluminada por uma luz tênue.")
        time.sleep(3)
        print("A sala parece ser o coração da masmorra, e no centro dela, um brilho dourado chama a sua atenção.")
        time.sleep(3)
        print(f"O coração acelera, pois {personagem.nome} acreditava ter finalmente encontrado o tesouro perdido!")
        time.sleep(3)
        print("No entanto, aquele brilho revela-se uma armadilha mortal. O tesouro se transforma diante de seus olhos!")
        time.sleep(3)
        print(f"Um Mimico, ser metamórfico faminto por carne, revela sua verdadeira forma e avança em sua direção!.")
        input("\nPressione Enter para enfrentar o terrível Mimico...\n")

    def introducao_dragao_negro(cls, personagem):
        print(f"{personagem.nome} avança ainda mais nas profundezas da masmorra, onde a escuridão é quase palpável.")
        time.sleep(3)
        print("A temperatura parece cair drasticamente. Uma presença sombria se faz presente.")
        time.sleep(3)
        print(f"De repente, o céu negro da masmorra se ilumina com raios negros, e uma figura colossal emerge das sombras.")
        time.sleep(3)
        print(f"Diante de {personagem.nome}, o Dragão Negro, uma criatura de pura escuridão e mal, estende suas asas enormes.")
        time.sleep(3)
        print(f"Uma sensação de desespero se instala, pois {personagem.nome} percebe que enfrentará uma das mais terríveis criaturas da masmorra.")
        input("\nPressione Enter para enfrentar o temível Dragão Negro...\n")

    def introducao_rei_do_abismo(cls, personagem):
        print(f"{personagem.nome} chega ao coração da masmorra, onde a escuridão é mais profunda e opressiva.")
        time.sleep(3)
        print(f"Um silêncio mortal preenche o ar, enquanto {personagem.nome} se depara com um trono macabro.")
        time.sleep(3)
        print("No trono, está sentado o Rei do Abismo, uma entidade sombria e poderosa que governa as trevas desta masmorra.")
        time.sleep(3)
        print(f"Seus olhos brilham com uma malícia antiga, e seu poder é palpável no ar ao redor.")
        time.sleep(3)
        print(f"{personagem.nome} enfrentará o maior desafio de sua jornada na masmorra. A batalha final se inicia!")
        time.sleep(3)
        input("\nPressione Enter para iniciar a batalha contra o temível Rei do Abismo...\n")
       
def masmorra(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 40)
    print("#          RPG via Terminal            #")
    print("#" * 40)

    for nivel in range(1, 7):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#" * 40)
        print("#          RPG via Terminal            #")
        print("#" * 40)
        print(f"\nNível {nivel} da Masmorra:")
        
        #Cada nível, um monstro
        if nivel == 1:
            monstro = Monstro("Goblin Verde", 50, 10)
            monstro.introducao_goblin_verde(personagem)
        elif nivel == 2:
            monstro = Monstro("Cavaleiro Esqueleto", 67, 14)
            monstro.introducao_cavaleiro_esqueleto(personagem)
        elif nivel == 3:
            monstro = Monstro("Ogro Sedento", 84, 16)
            monstro.introducao_ogro_sedento(personagem)
        elif nivel == 4:
            monstro = Monstro("Mimico", 92, 18)
            monstro.introducao_mimico(personagem)
        elif nivel == 5:
            monstro = Monstro("Dragão Negro", 150, 20)
            monstro.introducao_dragao_negro(personagem)
        else:
            monstro = Monstro("Rei do Abismo", 170, 20)
            monstro.introducao_rei_do_abismo(personagem)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nUm {monstro.nome} aparece!")
        print(f"\nIniciando batalha: {personagem.nome} vs {monstro.nome}")

        #Inicia a batalha usando cada istância da masmorra
        vitoria = batalha(personagem, monstro)

        #Jogador foi derrotado
        if not vitoria:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#" * 40)
            print("#          RPG via Terminal            #")
            print("#" * 40)

            print(f"\nVocê sucumbiu aos desafios da masmorra. Sua aventura chegou ao fim.")
            input("\nPressione Enter para sair...\n")
            return

    #Se o loop terminar, significa que o jogador passou por todos os níveis da masmorra
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#" * 40)
    print("#          RPG via Terminal            #")
    print("#" * 40)
    print("\nParabéns! Após uma jornada repleta de desafios e perigos, você finalmente alcançou a sala do tesouro.")
    time.sleep(2)
    print("A sala é iluminada por uma luz mística, revelando pilhas de ouro, relíquias antigas e artefatos poderosos.")
    time.sleep(2)
    print("Você se aproxima do tesouro, sentindo a energia mágica que emana dele.")
    time.sleep(2)
    print("Seu coração se enche de triunfo ao saber que superou todos os desafios da masmorra.")
    time.sleep(2)

    print("\nCriador: Gabriel Nicolas | Linkedin: https://www.linkedin.com/in/gabrielnikolax | Github: https://github.com/Nik0lax ")
    input("\nPressione Enter para finalizar sua jornada e retornar ao menu inicial...\n")
    tela_inicial()

def batalha(personagem, monstro):
    exibir_hp_mp_batalha(personagem, monstro)

    while personagem.hp > 0 and monstro.hp > 0:
        print("\nOpções de Batalha:")
        print("1. Atacar")
        print("2. Usar Habilidade")
        print("3. Defender")

        escolha_batalha = input("Escolha uma opção: ")

        if escolha_batalha == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            dano_personagem = calcular_dano(personagem.ataque, 0.7, 1.5)
            dano_monstro = calcular_dano(monstro.ataque, 0.7, 1.0)

            monstro.hp -= dano_personagem
            personagem.hp -= dano_monstro

            print(f"\nVocê realiza um Ataque Básico e causa {dano_personagem} de dano.")
            print(f"O {monstro.nome} contra-ataca e causa {dano_monstro} de dano.")

        elif escolha_batalha == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            if personagem.stamina_mp >= 4:  #Verifica se há stamina/MP suficiente para o Ataque Especial
                dano_personagem = calcular_dano(personagem.ataque, 1.2, 1.5)
                dano_monstro = calcular_dano(monstro.ataque, 0.7, 1.2)

                monstro.hp -= dano_personagem
                personagem.hp -= dano_monstro
                gasto_stamina_mp = random.randint(4, 7)
                personagem.stamina_mp -= gasto_stamina_mp 

                print(f"\nVocê realiza um Ataque Especial, gastou {gasto_stamina_mp} de Stamina/MP e causou {dano_personagem} de dano.")
                print(f"O {monstro.nome} se recupera do seu ataque e causa {dano_monstro} de dano.")
            else:
                print("\nStamina/MP insuficiente para Ataque Especial. Realize outro movimento.")

        elif escolha_batalha == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nVocê assume uma postura defensiva.")

            dano_monstro = calcular_dano(monstro.ataque, 0.3, 0.5)

            personagem.hp -= dano_monstro

            print(f"Você consegue defender e recebe {dano_monstro} de dano do {monstro.nome}.")

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nOpção inválida. Tente novamente.")

        exibir_hp_mp_batalha(personagem, monstro)

        #Verifica se a batalha terminou
        if personagem.hp <= 0:
            return False

        elif monstro.hp <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#" * 40)
            print("#          RPG via Terminal            #")
            print("#" * 40)
            print(f"\nVocê derrotou o {monstro.nome}!")
            time.sleep(2)
            print("Você encontra uma fogueira e descansa para recuperar o folego...")
            time.sleep(2)
            
            # Restaura o HP ao valor original após a derrota do monstro
            personagem.hp = personagem.hp_original
            personagem.stamina_mp = personagem.stamina_mp_original
            input("\nPressione Enter para avançar para o próximo nível...")
            os.system('cls' if os.name == 'nt' else 'clear')

            return True
    return True  #Se sair do loop, consideramos a batalha como vencida

def calcular_dano(ataque, min_percent, max_percent):
    #Calcula o dano baseado no ataque e em uma porcentagem aleatória entre min_percent e max_percent.
    damage_percent = random.uniform(min_percent, max_percent)
    return int(ataque * damage_percent)

def exibir_hp_mp_batalha(personagem, monstro):
    print(f"\nHP de {personagem.nome}: {personagem.hp}            HP de {monstro.nome}: {monstro.hp} ")
    print(f"MP de {personagem.nome}: {personagem.stamina_mp}")



def main():
    while True:
        tela_inicial()
        opcao = input("\nEscolha uma opção: ")
        

        if opcao == '1':
            while True:
                menu_selecao_personagem()
                escolha_personagem = input("\nEscolha seu personagem: ")

                if escolha_personagem == '0':
                    break  # Voltar para o menu inicial
                
                personagem_escolhido = None
                if escolha_personagem == '1':
                    historia_Rodolf = "Rodolf, o Guerreiro, parte em uma jornada para a masmorra em busca de um tesouro perdido. Seu treinamento árduo o preparou para enfrentar monstros terríveis e desafios mortais."
                    personagem_escolhido = Personagem("Rodolf", "Guerreiro", 120, 24, 15, historia_Rodolf)
                elif escolha_personagem == '2':
                    historia_sypha = "Sypha, a Feiticeira, é guiada pela busca do conhecimento. Ao entrar na masmorra, ela espera desvendar os segredos mágicos que cercam o tesouro perdido."
                    personagem_escolhido = Personagem("Sypha", "Feiticeira", 75, 30, 20, historia_sypha)
                elif escolha_personagem == '3':
                    historia_astarion = "Astarion, o Ladino, busca riquezas e glória. Sua habilidade furtiva o ajuda a se infiltrar na masmorra, afim de conseguir o tesouro perdido."
                    personagem_escolhido = Personagem("Astarion", "Ladino", 100, 28, 17, historia_astarion)
                else:
                    print("Escolha inválida. Tente novamente.")

                if personagem_escolhido:
                    personagem_escolhido.exibir_status()
                    confirmacao = input("\nVocê confirma este personagem? (1 para Sim, 2 para Não): ")

                    if confirmacao == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("#" * 40)
                        print("#          RPG via Terminal            #")
                        print("#" * 40)
                        print(f"\nVocê escolheu {personagem_escolhido.nome}, {personagem_escolhido.classe}!")
                        input("\nPressione Enter para continuar...\n")

                        epilogo(personagem_escolhido)

                        masmorra(personagem_escolhido)

                    elif confirmacao == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        # Volta para o menu de seleção de personagem
                        print("\nRetornando ao menu de seleção de personagem...")
                    else:
                        print("Opção inválida. Tente novamente.")
        elif opcao == '2':
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
