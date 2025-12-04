"""
Sistema Simple de Finanzas Personales
Permite registrar ingresos y gastos
"""

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("   FINANZAS PERSONALES")
    print("="*40)
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver resumen")
    print("4. Ver historial")
    print("5. Salir")
    print("="*40)


def registrar_ingreso(transacciones):
    """Registra un nuevo ingreso"""
    try:
        monto = float(input("Ingrese el monto: $"))
        descripcion = input("Descripción: ")
        
        transaccion = {
            'tipo': 'ingreso',
            'monto': monto,
            'descripcion': descripcion
        }
        transacciones.append(transaccion)
        print(f"✓ Ingreso de ${monto:.2f} registrado correctamente")
    except ValueError:
        print("✗ Error: Ingrese un monto válido")


def registrar_gasto(transacciones):
    """Registra un nuevo gasto"""
    try:
        monto = float(input("Ingrese el monto: $"))
        descripcion = input("Descripción: ")
        
        transaccion = {
            'tipo': 'gasto',
            'monto': monto,
            'descripcion': descripcion
        }
        transacciones.append(transaccion)
        print(f"✓ Gasto de ${monto:.2f} registrado correctamente")
    except ValueError:
        print("✗ Error: Ingrese un monto válido")


def calcular_totales(transacciones):
    """Calcula el total de ingresos, gastos y balance"""
    total_ingresos = sum(t['monto'] for t in transacciones if t['tipo'] == 'ingreso')
    total_gastos = sum(t['monto'] for t in transacciones if t['tipo'] == 'gasto')
    balance = total_ingresos - total_gastos
    
    return total_ingresos, total_gastos, balance


def ver_resumen(transacciones):
    """Muestra un resumen financiero"""
    if not transacciones:
        print("\nNo hay transacciones registradas")
        return
    
    total_ingresos, total_gastos, balance = calcular_totales(transacciones)
    
    print("\n" + "="*40)
    print("   RESUMEN FINANCIERO")
    print("="*40)
    print(f"Total Ingresos:  ${total_ingresos:>10.2f}")
    print(f"Total Gastos:    ${total_gastos:>10.2f}")
    print("-"*40)
    print(f"Balance:         ${balance:>10.2f}")
    print("="*40)


def ver_historial(transacciones):
    """Muestra el historial de todas las transacciones"""
    if not transacciones:
        print("\nNo hay transacciones registradas")
        return
    
    print("\n" + "="*40)
    print("   HISTORIAL DE TRANSACCIONES")
    print("="*40)
    
    for i, t in enumerate(transacciones, 1):
        tipo_simbolo = "+" if t['tipo'] == 'ingreso' else "-"
        print(f"{i}. [{t['tipo'].upper()}] {tipo_simbolo}${t['monto']:.2f} - {t['descripcion']}")
    
    print("="*40)


def main():
    """Función principal del programa"""
    transacciones = []
    
    print("\n¡Bienvenido al Sistema de Finanzas Personales!")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == '1':
            registrar_ingreso(transacciones)
        elif opcion == '2':
            registrar_gasto(transacciones)
        elif opcion == '3':
            ver_resumen(transacciones)
        elif opcion == '4':
            ver_historial(transacciones)
        elif opcion == '5':
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("✗ Opción inválida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
