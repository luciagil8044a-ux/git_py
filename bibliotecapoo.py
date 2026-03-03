class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, genero, unidades):
        super().__init__(titulo, autor)
        self.genero = genero
        self.unidades = unidades

    def mostrar_info(self):
        print("LIBRO")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Género:", self.genero)
        print("Unidades:", self.unidades)

    def prestar(self):
        if self.unidades > 0:
            self.unidades -= 1
            print("Libro prestado")
        else:
            print("No hay unidades disponibles")

    def devolver(self):
        self.unidades += 1
        print("Libro devuelto")
class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, categoria):
        super().__init__(titulo, autor)
        self.categoria = categoria

    def mostrar_info(self):
        print("REVISTA")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Categoría:", self.categoria)

    def prestar(self):
        print("Revista prestada")

    def devolver(self):
        print("Revista devuelta")
libro1 = Libro("El Quijote", "Cervantes", "Novela", 1)
revista1 = Revista("Muy Interesante", "Varios", "Ciencia")
libro1.mostrar_info()
libro1.prestar()
libro1.prestar()  
libro1.devolver()
print()
revista1.mostrar_info()
revista1.prestar()
revista1.devolver()
