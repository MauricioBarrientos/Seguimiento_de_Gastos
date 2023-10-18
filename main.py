import matplotlib.pyplot as plt

class SeguimientoGastos:
    def __init__(self):
        self.gastos = {}

    def agregar_gasto(self, categoria, monto):
        if categoria in self.gastos:
            self.gastos[categoria] += monto
        else:
            self.gastos[categoria] = monto

    def mostrar_gastos(self):
        if len(self.gastos) == 0:
            print("No hay gastos registrados.")
        else:
            print("Gastos:")
            for categoria, monto in self.gastos.items():
                print(f"{categoria}: ${monto}")

    def generar_grafico(self):
        categorias = list(self.gastos.keys())
        montos = list(self.gastos.values())

        plt.bar(categorias, montos)
        plt.xlabel("Categorías")
        plt.ylabel("Monto")
        plt.title("Seguimiento de Gastos")
        plt.show()

# Crear una instancia del sistema de seguimiento de gastos
seguimiento = SeguimientoGastos()

while True:
    print("Sistema de Seguimiento de Gastos")
    print("1. Agregar gasto")
    print("2. Mostrar gastos")
    print("3. Generar gráfico")
    print("4. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        categoria = input("Ingrese la categoría del gasto: ")
        monto = float(input("Ingrese el monto del gasto: "))
        seguimiento.agregar_gasto(categoria, monto)
        print("Gasto agregado exitosamente.")

    elif opcion == 2:
        seguimiento.mostrar_gastos()

    elif opcion == 3:
        seguimiento.generar_grafico()

    elif opcion == 4:
        print("Gracias por usar el sistema de seguimiento de gastos.")
        break

    else:
        print("Opción incorrecta. Por favor, seleccione una opción válida.")

    print()