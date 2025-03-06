class Cajero:
    def __init__(self, nombre: str, sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo
        self.ventas = 0

    def vender(self, monto: float):
        self.ventas += 1
        self.sueldo += monto * 0.6

    def get_ventas(self) -> int:
        return self.ventas

class Tienda:
    def __init__(self, nombre: str, id: int, ingresos: float, cajero: Cajero):
        self.nombre = nombre
        self.id = id
        self.ingresos = ingresos
        self.cajero = cajero

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        return self.nombre

    def calcular_ventas(self) -> int:
        return self.cajero.get_ventas()

if __name__ == "__main__":
    print("Bienvenido a la tienda")
    cajero = Cajero("Juan", 1000.0)
    cajero.vender(100.0)
    print("Ventas del cajero:", cajero.get_ventas())
    tienda = Tienda("Tienda", 1, 0.0, cajero)
    print("Nombre de la tienda:", tienda.get_nombre())
