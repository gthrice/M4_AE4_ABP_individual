# Importaciones
from tamagochi import Tamagochi, fuego, electrico, agua
from persona import Persona

def pedir_nombre(mensaje):
    """Solicita un nombre y valida que no esté vacío."""
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío. Inténtalo de nuevo.")

def pedir_opcion(mensaje, opciones):
    """Solicita una opción y valida que esté en el rango de opciones."""
    while True:
        opcion = input(mensaje)
        if opcion in opciones:
            return opcion
        print(f"Opción no válida. Elige entre: {', '.join(opciones)}.")


def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Adoptar un nuevo Tamagotchi")
    print("2. Interactuar con un Tamagotchi")
    print("3. Ver el estado de todas mis mascotas")
    print("4. Salir")

def mostrar_menu_tipo():
    print("\n--- Elige un tipo de Tamagotchi ---")
    print("1. Agua (Más salud)")
    print("2. Fuego (Más felicidad)")
    print("3. Eléctrico (Más energía)")

def mostrar_menu_acciones(nombre):
    print(f"\n--- ¿Qué quieres hacer con {nombre}? ---")
    print("1. Jugar")
    print("2. Alimentar")
    print("3. Curar")
    print("4. Descansar")
    print("5. Volver al menú principal")

def main():
    print("¡Bienvenido al Centro de Adopción de Tamagotchis!")
    nombre_dueño = input("Para empezar, ¿cuál es tu nombre? ")
    apellido_dueño = input("¿Y tu apellido? ")
    dueño = Persona(nombre=nombre_dueño, apellido=apellido_dueño)
    print(f"\n¡Hola, {dueño.nombre}! Prepárate para cuidar de tus mascotas.")

    while True:
        mostrar_menu_principal()
        opcion = pedir_opcion("Elige una opción: ", ["1", "2", "3", "4"])

        if opcion == "1":
            mostrar_menu_tipo()
            tipo_opcion = pedir_opcion("Elige un tipo: ", ["1", "2", "3"])
            nombre_mascota = pedir_nombre("¿Qué nombre le quieres poner? ")
            nueva_mascota = None
            if tipo_opcion == "1":
                nueva_mascota = agua(nombre=nombre_mascota)
            elif tipo_opcion == "2":
                nueva_mascota = fuego(nombre=nombre_mascota)
            elif tipo_opcion == "3":
                nueva_mascota = electrico(nombre=nombre_mascota)
            dueño.adoptar_tamagotchi(nueva_mascota)

        elif opcion == "2":
            if not dueño.tamagotchis:
                print("\nPrimero necesitas adoptar una mascota.")
                continue
            print("\n--- ¿Con qué mascota quieres interactuar? ---")
            for i, mascota in enumerate(dueño.tamagotchis):
                print(f"{i + 1}. {mascota.nombre}")
            mascota_elegida = None
            while True:
                eleccion_str = input("Elige el número del Tamagotchi: ")
                if eleccion_str.isdigit():
                    eleccion_idx = int(eleccion_str) - 1
                    if 0 <= eleccion_idx < len(dueño.tamagotchis):
                        mascota_elegida = dueño.tamagotchis[eleccion_idx]
                        break
                    else:
                        print("\nError: Ese número no está en la lista.")
                else:
                    print("\nError: Debes introducir un número.")
            while True:
                mostrar_menu_acciones(mascota_elegida.nombre)
                accion_opcion = pedir_opcion("Elige una acción: ", ["1", "2", "3", "4", "5"])
                if accion_opcion == "1":
                    dueño.jugar_con(mascota_elegida)
                elif accion_opcion == "2":
                    dueño.alimentar_a(mascota_elegida)
                elif accion_opcion == "3":
                    dueño.curar_a(mascota_elegida)
                elif accion_opcion == "4":
                    dueño.hacer_descansar_a(mascota_elegida)
                elif accion_opcion == "5":
                    break


        elif opcion == "3":
            dueño.mostrar_mascotas()

        elif opcion == "4":
            print("\n¡Gracias por jugar! Vuelve pronto.")
            break
        
        else:
            print("\nOpción no válida. Por favor, elige un número del menú.")


if __name__ == "__main__":
    main()