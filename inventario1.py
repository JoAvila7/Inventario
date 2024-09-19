class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def ver_productos(self):
        for producto in self.productos.values():
            print(producto)

    def editar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            if nombre is not None:
                self.productos[id_producto].nombre = nombre
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def guardar_datos(self, archivo):
        with open(archivo, 'w') as f:
            for producto in self.productos.values():
                f.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print("El archivo no se encuentra.")



def menu():
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Guardar datos")
    print("6. Cargar datos")
    print("7. Salir")

def main():
    inventario = Inventario()
    inventario.cargar_datos('inventario.txt')

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            inventario.ver_productos()

        elif opcion == '3':
            id_producto = input("ID del producto a editar: ")
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.editar_producto(
                id_producto,
                nombre if nombre else None,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == '4':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '5':
            inventario.guardar_datos('inventario.txt')

        elif opcion == '6':
            inventario.cargar_datos('inventario.txt')

        elif opcion == '7':
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
