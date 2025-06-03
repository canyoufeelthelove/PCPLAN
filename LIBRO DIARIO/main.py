from db import crear_db, obtener_asientos
from contabilidad import registrar_asiento
from rich.console import Console
from rich.table import Table

crear_db()
console = Console()

def mostrar_menu():
    while True:
        console.print("\n[bold cyan]--- LIBRO DIARIO ---[/bold cyan]")
        console.print("1. Registrar asiento contable")
        console.print("2. Ver libro diario")
        console.print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            registrar_asiento()
        elif opcion == '2':
            mostrar_libro_diario()
        elif opcion == '3':
            break
        else:
            console.print("[red]Opción no válida[/red]")

def mostrar_libro_diario():
    asientos = obtener_asientos()
    for a in asientos:
        console.print(f"\n[bold]Asiento #{a['id']} - Fecha: {a['fecha']}[/bold]")
        console.print(f"Glosa: {a['glosa']}")
        tabla = Table(show_header=True, header_style="bold magenta")
        tabla.add_column("Cuenta")
        tabla.add_column("Descripción")
        tabla.add_column("Debe", justify="right")
        tabla.add_column("Haber", justify="right")

        for det in a['detalles']:
            tabla.add_row(det[0], det[1], f"{det[2]:.2f}", f"{det[3]:.2f}")
        console.print(tabla)

if __name__ == '__main__':
    mostrar_menu()
