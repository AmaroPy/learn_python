# Vamos a enunciar el laberinto
print("Bienvenido al laberinto, ¿Podrás salir?")
camino_list = []

# Primera intersección
print("Llegas a la primera intersección, ¿Qué eliges? A o B")
camino = input("si quieres ir por el camino oscuro escribe: A. Si prefieres el puente cochambroso elige: B > ")

# Elección del jugador
if camino == "A":
    print("El camino es muy oscuro pero puedes ver dos caminos mas")
    camino_list.append("A")
    camino_c = input("Ves una casa sospechosa pero quieres dormir: C. Señales de un pueblo cercano, decides seguirlas: D > ")

    if camino_c == "C":
        print("Era la casa de la bruja. Game Over.")
        camino_list.append("C")
        
    else:
        print("El camino acaba en terraplén, no lo ves y te caes por él. Game Over.")
        camino_list.append("D")
        
# Si elige B
else:
    print("Buena elección, sigues progresando")
    camino_g = input("Encuentras una puerta con un acertijo. ¿Cuanto es 5 al cuadrado? > ")
    camino_list.append("B")

    if not camino_g == "25":
        print("Caes en arenas movedizas. Game Over")
        camino_list.append("No acertaste el acertijo")

    else:
        print("Has elegido bien. Puedes continuar.")
        camino_e = input("Animo solo una elección mas. G o H > ")
        camino_list.append("Acertaster el acertijo")

# Si eliges H
        if camino_e == "G":
            print("No has sorteado a la muerte. Game Over")
            camino_list.append("G")
        else:
            print("Era broma aún no has salido pero puedes continuar.")
            camino = input("Ahora sí, última opción. I, J, K o L > ")
            camino_list.append("H")

            if camino == "I":
                print("Una pena, estabas taaaan cerca... Game Over.")
                camino_list.append("I")
            
            elif camino == "J":
                print("Enhorabuena, has salido sano y salvo.")
                camino_list.append("J")
            
            elif camino == "K":
                print("Felicidades, te has roto la pierna pero has salido. Casi perfecto.")
                camino_list.append("K")

            else:
                print("Vaya pensaba que lo conseguirías, la proxima ves será. Si te atreves a repetir")
                camino_list.append("L")

# El juego acaba ahí

camino_final = "Éste es tu recorrido." + str(camino_list)
print(camino_final)