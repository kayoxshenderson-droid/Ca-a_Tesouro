print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print(r'''
        Há um misterioso baú à sua frente...

         _________________________
        |  _____________________  |
        | |                     | |
        | |    TESOURO???       | |
        | |_____________________| |
        |_________________________|
        |  _____________________  |
        | |  O            O    | |
        | |       ( )          | |
        | |___________________| |
        |_________________________|
''')

print("Bem Vindo ao Caça Tesouro.")
print("Sua Missão é achar o tesouro.")

escolha_1 = input("Você está está Perdido. Para onde quer ir? "
                  "Digite \"esquerda\" ou \"direita\".: ").lower()

if escolha_1 == "esquerda":
    escolha_2 = input("Você chegou a um Lago"
                      ", há uma ilha no meio do lago"
                      ". Digite \"Esperar\" para esperar um barco"
                      " ""Digite \"Nadar\" para atravessar a Margem.: ").lower()
    if escolha_2 == "nadar":
        escolha_3 = input(
            "Você chega à ilha ileso. Há uma casa com 3 portas: uma vermelha, uma amarela e uma azul. Quais cores você escolhe?: ").lower()
        if escolha_3 == "vermelha":
            print("Este quarto esta pegando fogo. Fim de jogo")
        elif escolha_3 == "amarela":
            print(r'''
        A porta amarela se abre... e lá está o baú!

              $   $   $   $   $
           $                     $
          __________________________
         /  $  $  $  $  $  $  $   /|
        /  $   TESOURO ACHADO!  $ / |
       /  $  $  $  $  $  $  $  $ /  |
      |"""""""""""""""""""""""""|   |
      | $  $$$$   $$$$   $$$$  $|   |
      | $ $    $ $    $ $    $ $|   /
      | $  $$$$   $$$$   $$$$  $|  /
      | $        $$$$$         $| /
      |_________________________|/
           $   $   $   $   $

      Voce encontrou o Tesouro. Voce GANHOU! 
''')
        elif escolha_3 == "azul":
            print("Este quarto esta cheio de animais selvagens. Você Morreu")
        else:
            print("Voce não escolheu nenhuma porta, voce morreu. Fim de jogo")
    else:
        print("Voce foi atacado por Tubarôes. Fim de jogo")


else:
    print("Você caiu no buraco. Fim de Jogo")