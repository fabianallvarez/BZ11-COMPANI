from .models import CriptoModel
from .views import CriptoView


class CriptoController:
    def __init__(self):
        # instancio la vista y el modelo
        self.modelo = CriptoModel()
        self.vista = CriptoView()

    def consultar(self):
        seguir = "S"
        while seguir == "S":
            desde, hasta = self.vista.pedir_monedas()

            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            self.modelo.consultar_cambio()

            self.vista.mostrar_cambio(desde, hasta, self.modelo.cambio)

            seguir = ""
            while seguir not in ("S", "N"):
                seguir = self.vista.quieres_seguir()