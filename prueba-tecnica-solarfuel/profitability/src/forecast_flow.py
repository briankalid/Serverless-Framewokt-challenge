from .constants import TIPO_CAMBIO_USD_MXN, INFLACION_ANUAL

def flujo_retorno(propiedad:dict, anios: int) -> list:
    inversion_inicial_mxn = propiedad.get("Inversion_Inicial") * TIPO_CAMBIO_USD_MXN
    flujo = []

    Ultimo_mantenimiento = propiedad.get("Mantenimiento_Anual")
    Ultimo_ingreso = propiedad.get("Ingreso_Renta_Anual")
    flujo_acumulado = -inversion_inicial_mxn

    for i in range(anios):
        flujo_actual = {}
        flujo_actual["Anio"] = 2024 + i+1
        flujo_actual["Inversion"] = inversion_inicial_mxn
        ultimo_mantenimiento = Ultimo_mantenimiento * (INFLACION_ANUAL)
        flujo_actual["Egreso"] = ultimo_mantenimiento
        Ultimo_ingreso = Ultimo_ingreso * (INFLACION_ANUAL)
        flujo_actual["Ingreso"] = Ultimo_ingreso
        flujo_actual["Flujo Anual"] = flujo_actual["Ingreso"] - flujo_actual["Egreso"]
        flujo_acumulado = flujo_acumulado + flujo_actual["Flujo Anual"]
        flujo_actual["Flujo Acumulado"] = flujo_acumulado

        flujo.append(flujo_actual)

    return flujo