from .constants import TIPO_CAMBIO_USD_MXN, INFLACION_ANUAL

def retorno_inversion(propiedad:dict) -> float:
    inversion_inicial_mxn = propiedad.get("Inversion_Inicial") * TIPO_CAMBIO_USD_MXN
    tiempo_retorno = 0
    retorno = 0

    while retorno < inversion_inicial_mxn:
        ingreso_anual = propiedad.get("Ingreso_Renta_Anual") * INFLACION_ANUAL ** tiempo_retorno
        mantenimiento_anual = propiedad.get("Mantenimiento_Anual") * INFLACION_ANUAL ** tiempo_retorno
        ingreso_anual_neto = ingreso_anual - mantenimiento_anual
        
        retorno += ingreso_anual_neto
        tiempo_retorno += 1


    return tiempo_retorno