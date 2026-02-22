# sistema_inventario.py

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")
        self.cantidad = int(nueva_cantidad)

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (f"Producto: {self.nombre} | "
                f"Precio: ${self.precio:.2f} | "
                f"Cantidad: {self.cantidad} | "
                f"Valor Total: ${self.calcular_valor_total():.2f}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n=== LISTA DE PRODUCTOS ===")
            for producto in self.productos:
                print(producto)


def menu_principal(inventario):
    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre_buscar)
                if producto:
                    print("Producto encontrado:")
                    print(producto)
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: ${total:.2f}")

            elif opcion == "5":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except TypeError as te:
            print(f"Error de tipo: {te}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
