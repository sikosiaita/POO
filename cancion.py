class Cancion:
    def __init__(self, titulo, artista, duracion_sec: int):
        self.titulo = titulo
        self.artista = artista
        self.duracion_sec = duracion_sec

    def milisegundos(self):
        m, s = divmod(max(self.duracion_sec(), 0), 60)
        return f"{m}:{s}"
    
    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.duracion_sec}"

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        return sum(c.duracion_sec for c in self.canciones)
    
    def milisegundos_total(self):
        total = self.duracion_total()
        m, s = divmod(max(total(), 0), 60)
        return f"{m}:{s}"
    
    def __len__(self):
        return len(self.canciones)
    
    def __add__(self, otra):
        nueva = Playlist(f"{self.nombre} + {otra.nombre}")

        nueva.canciones = self.canciones + otra.canciones
        return nueva
    
    def __str__(self):
        encabezado = f"Playlist: {self.nombre} | {len(self.canciones)} | {self.milisegundos_total}"    

        if not self.canciones:
            return encabezado, f"Lista vacia"
        
        lineas = [encabezado]
        for i, c in enumerate(self.canciones):
            lineas.append(f"{i}:{c}")
            return "\n".join (lineas)