class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy un {self.__class__.__name__} y mi nombre es {self.nombre}.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase base (Animal)
        self.raza = raza

    def saludar(self):
        super().saludar()  # Llama al método saludar de la clase base (Animal)
        print(f"Soy un perro de raza {self.raza}.")

# Crear una instancia de la clase Perro
mi_perro = Perro("Bobby", "Golden Retriever")
mi_perro.saludar()