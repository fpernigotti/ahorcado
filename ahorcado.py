import random

def ahorcado(palabra):
    mal = 0
    niveles = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    letras = list(palabra)
    tablero = ["_"]*len(palabra)
    gano = False
    print ("Bienvenido al ahorcado")
    while mal < len(niveles)-1:
        print("\n")
        msg = "Adivina una letra: "
        caracter =  input(msg)

        if caracter in letras:
            lind = letras.index(caracter)
            tablero[lind] = caracter
            letras[lind] = "$"
        else:
            mal += 1
        print((" ".join(tablero)))
        e = mal +1
        print("\n".join(niveles[0:e]))

        if "_" not in tablero:
            print ("Felicitaciones!!")
            print (" ".join(tablero))
            gano = True
            break
    
    if not gano:
        print("\n".join(tablero[o:mal]))
        print("Perdiste, la palabra era {}".format(palabra))

palabras = ["perro","gato", "loro", "cocodrilo", "tiranosaurio"]

palabra_juego = random.choice(palabras)

ahorcado(palabra_juego)