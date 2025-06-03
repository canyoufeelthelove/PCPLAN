# Diccionario de cuentas contables simplificado
PLAN_CONTABLE = {
    "10": "Efectivo y equivalente de efectivo",
    "12": "Cuentas por cobrar comerciales - Terceros",
    "40": "Tributos por pagar",
    "60": "Compras",
    "70": "Ventas",
    "42": "Remuneraciones por pagar",
    "50": "Mercaderías",
    "94": "Costos indirectos",
    "46": "Cuentas por pagar diversas",
    "79": "Cargas imputables a cuentas de costos",
}

def validar_cuenta(codigo):
    return codigo in PLAN_CONTABLE
