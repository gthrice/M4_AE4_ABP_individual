class Tamagochi:
    def __init__(self, nombre, salud, felicidad, energia):
        self.nombre = nombre
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def actualizar(self):
        self.salud = max(0, min(120, self.salud)) # Asegurarse de que la salud esté entre 0 y 100
        self.felicidad = max(0, min(120, self.felicidad)) # Asegurarse de que la felicidad esté entre 0 y 100
        self.energia = max(0, min(120, self.energia)) # Asegurarse de que la energia esté entre 0 y 100
    def mostrar_estado(self):
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"❤️ Salud: {self.salud}")
        print(f"😊 Felicidad: {self.felicidad}")
        print(f"⚡ Energía: {self.energia}")
        print("------------------------")
    def jugar(self):
        self.felicidad += 10
        self.energia -= 5
        self.salud -= 5
        print(f"{self.nombre} está jugando, ha subido su felcidad en 20")
        self.mostrar_estado()
        return self

    def comer(self):
        self.felicidad += 5
        self.energia -= 5
        self.salud += 10
        print(f"{self.nombre} está comiendo, su salud ha subido en 10 y su felicidad en 5")
        self.actualizar()
        self.mostrar_estado()
        return self
    def curar(self):
        self.felicidad -= 5
        self.energia -= 5
        self.salud += 20
        print(f"{self.nombre} está curandose, su salud ha subido en 20 y su felicidad en 5. Pero ha perdido 5 de energia")
        self.actualizar()
        self.mostrar_estado()
        return self
    def descansar(self):
        self.felicidad -= 5
        self.energia += 10
        self.salud -= 5
        print(f"{self.nombre} está descansando, su salud ha bajado en 5 y su felicidad en 5. Pero ha ganado 10 de energia")
        self.actualizar()
        self.mostrar_estado()
        return self


class agua(Tamagochi):
    def __init__(self, nombre, salud = 120, felicidad = 100, energia = 100):
        super().__init__(nombre, salud, felicidad, energia)
    def actualizar(self):
        self.salud = max(0, min(120, self.salud)) # Asegurarse de que la salud esté entre 0 y 100
        self.felicidad = max(0, min(100, self.felicidad)) # Asegurarse de que la felicidad esté entre 0 y 100
        self.energia = max(0, min(100, self.energia)) # Asegurarse de que la energia esté entre 0 y 100

class fuego(Tamagochi):
    def __init__(self, nombre, salud = 100, felicidad = 120, energia = 100):
        super().__init__(nombre, salud, felicidad, energia)
    def actualizar(self):
        self.salud = max(0, min(100, self.salud)) # Asegurarse de que la salud esté entre 0 y 100
        self.felicidad = max(0, min(120, self.felicidad)) # Asegurarse de que la felicidad esté entre 0 y 100
        self.energia = max(0, min(100, self.energia)) # Asegurarse de que la energia esté entre 0 y 100

class electrico(Tamagochi):
    def __init__(self, nombre, salud = 100, felicidad = 100, energia = 120):
        super().__init__(nombre, salud, felicidad, energia)
    def actualizar(self):
        self.salud = max(0, min(100, self.salud)) # Asegurarse de que la salud esté entre 0 y 100
        self.felicidad = max(0, min(100, self.felicidad)) # Asegurarse de que la felicidad esté entre 0 y 100
        self.energia = max(0, min(120, self.energia)) # Asegurarse de que la energia esté entre 0 y 100