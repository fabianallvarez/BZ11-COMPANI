"""

 Modelo <=> Controlador <=> Vista

 Modelo </////> Vista   (NUNCA hay comunicación entre el modelo y la vista directamente)

"""


from tkinter import ttk


class CriptoView:

    def pedir_monedas(self):
        origen = input("¿Qué moneda quieres cambiar? ")
        destino = input("¿Qué moneda deseas obtener? ")
        return (origen, destino)

    def mostrar_cambio(self, origen, destino, cambio):
        print("Un {} vale como {:,.2f} {}".format(
            origen, cambio, destino,
        ))

    def quieres_seguir(self):
        seguir = input("¿Quieres cambiar algo más? (s/n) ")
        return seguir.upper()

class CriptoViewTK(ttk.Frame):

    def __init__(self, padre):
        super().__init__(padre, width=400, height=400)
        self.grid()
        self.crear_controles()

    def crear_controles(self):
        ejemplo = ttk.Label(self, text="CriptoCambio")
        ejemplo.grid(row=0, column=0)