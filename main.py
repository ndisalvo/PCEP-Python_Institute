import random

while True:
    jugada_usuario = input("\nIngresa una opcion (piedra, papel, tijera): ")
    acciones_posibles = ["piedra", "papel", "tijera"]
    jugada_computadora = random.choice(acciones_posibles)
    print(f"\nHas elegido {jugada_usuario}, la computadora eligio {jugada_computadora}.\n")

    if jugada_usuario == jugada_computadora:
        print(f"\nAmbos jugadores gan elegido {jugada_usuario}. Es un empate!")
    elif jugada_usuario == "piedra":
        if jugada_computadora == "tijera":
            print("\nPiedra rompe tijera! Tu ganas!")
        else:
            print("\nPapel cubre piedra! Tu pierdes.")
    elif jugada_usuario == "papel":
        if jugada_computadora == "piedra":
            print("\nPapel cubre piedra! Tu ganas!")
        else:
            print("\nLa Tijera corta el papel! Tu pierdes.")
    elif jugada_usuario == "tijera":
        if jugada_computadora == "papel":
            print("\nLa Tijera corta el papel! Tu ganas!")
        else:
            print("\nPiedra rompe tijera! Tu pierdes.")

    jugar_otra_vez = input("\nJugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() != "s":
        break