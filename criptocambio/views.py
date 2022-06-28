class CriptoView:

    def __init__(self):
        pass

    def pedir_moneda(self):
        origen = input("¿Que moneda quieres cambiar?")
        destino = input("¿Que moneda deseas obtener?")
        return(origen, destino)

    def mostrar_cambio(self, origen, destino, cambio):
        print("Un {} vale como {:,.2f} {}".format(
            origen, destino, cambio,
            ))