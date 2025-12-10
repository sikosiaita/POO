class Contenido:
    def __init__(self, titulo: str, anio: int):
        self.titulo = titulo
        self.anio = anio

    def mostrar_detalle(self):
        print(f"Titulo: {self.titulo} | Año: {self.anio}")
class Reproducible:
    def reproducir(self):
        raise NotImplementedError(
            "Las subclases que hereden de Reproducible deben implementar reproducir()."
        )

class Calificable:
    def __init__(self):
        self.rating = 0.0

    def calificar(self, puntuacion: float):
        self.rating = puntuacion
        print(f"Nuevo rating asignado: {self.rating}") 

class Pelicula(Contenido, Reproducible):
    def __init__(self, titulo, anio, duracion_minutos):
        Contenido.__init__(self, titulo, anio)
        self.duracion_minutos = duracion_minutos

    def reproducir(self):
        print(f"Reproduciendo pelicula '{self.titulo}' ({self.duracion_minutos} min")


class Documental(Contenido):
    def __init__(self, titulo, anio, tema):
        super().__init__(titulo, anio)
        self.tema = tema

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Tema: {self.tema}")

class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(self, titulo, anio, num_episodios):
        Contenido.__init__(self, titulo, anio)
        Calificable.__init__(self)
        self.num_episodios = num_episodios

    def reproducir(self):
        print(f"Reproduciendo miniserie '{self.titulo}' "
              f"({self.num_episodios} episodios)")


if __name__ == "__main__":
    peli = Pelicula("Inception", 2010, 148)
    docu = Documental("Nuestro Planeta", 2019, "Naturaleza")
    mini = Miniserie("Gambito de dama", 2017, 10)

    print("\n--- Miniserie ---")
    mini.mostrar_detalle()
    mini.reproducir()
    mini.calificar(4.8)

    print("\n--- Pelicula ---" )
    peli.mostrar_detalle()
    peli.reproducir()

    print("\n--- Documental ---")
    docu.mostrar_detalle()
    