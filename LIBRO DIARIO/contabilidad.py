from cuentas import validar_cuenta, PLAN_CONTABLE
from db import insertar_asiento

def registrar_asiento():
    from datetime import datetime
    fecha = input("Fecha (YYYY-MM-DD): ")
    glosa = input("Glosa (descripción general): ")

    detalles = []
    total_debe = 0
    total_haber = 0

    while True:
        cuenta = input("Cuenta contable (código): ")
        if not validar_cuenta(cuenta):
            print("⚠️  Cuenta no válida según el plan contable.")
            continue
        descripcion = PLAN_CONTABLE[cuenta]

        debe = input("Monto al DEBE (deja vacío si no aplica): ")
        haber = input("Monto al HABER (deja vacío si no aplica): ")

        debe_val = float(debe) if debe else 0.0
        haber_val = float(haber) if haber else 0.0

        if debe_val > 0 and haber_val > 0:
            print("⚠️  No puedes registrar monto en DEBE y HABER a la vez.")
            continue
        if debe_val == 0 and haber_val == 0:
            print("⚠️  Debe ingresar al menos un monto.")
            continue

        detalles.append({
            "cuenta": cuenta,
            "descripcion": descripcion,
            "debe": debe_val,
            "haber": haber_val
        })

        total_debe += debe_val
        total_haber += haber_val

        otra = input("¿Agregar otra cuenta al asiento? (s/n): ").lower()
        if otra != 's':
            break

    if total_debe != total_haber:
        print(f"❌ Asiento desequilibrado: DEBE = {total_debe}, HABER = {total_haber}")
    else:
        insertar_asiento(fecha, glosa, detalles)
        print("✅ Asiento registrado correctamente.")
