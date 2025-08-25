class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchis = []

    def adoptar_tamagotchi(self, nueva_mascota):
        self.tamagotchis.append(nueva_mascota)
        print(f"\n¡{self.nombre} ha adoptado a {nueva_mascota.nombre}!")

    def mostrar_mascotas(self):
        print(f"\n--- Mascotas de {self.nombre} ---")
        if not self.tamagotchis:
            print("Todavía no tienes ninguna mascota.")
        else:
            for mascota in self.tamagotchis:
                mascota.mostrar_estado()
    
    
    def jugar_con(self, mascota):
        if mascota:
            mascota.jugar()

    def alimentar_a(self, mascota):
        if mascota:
            mascota.comer()

    def curar_a(self, mascota):
        if mascota:
            mascota.curar()
            
    def hacer_descansar_a(self, mascota):
        if mascota:
            mascota.descansar()