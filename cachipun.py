import random
jugador = int(input("Elige: 1.Piedra; 2.Papel; 3.Tijeras.. "))
pc = random.randint(1,3)
pc_elige = ""

if jugador == pc:
    resultado = "Empate"
elif jugador == 1 and pc == 2:
    resultado = "Perdiste"
elif jugador == 2 and pc == 3:
    resultado = "Perdiste"
elif jugador == 3 and pc == 1:
    resultado = "Perdiste"
else:
    resultado = "Ganaste!"

if pc == 1:
    pc_elige = "PIEDRA"
elif pc == 2:
    pc_elige = "PAPEL"
elif pc == 3:
    pc_elige = "TIJERAS"
else:
    print("dafuc?")


print ("El pc eligió", pc_elige, resultado)
