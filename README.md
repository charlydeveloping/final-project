# Finanzas Personales

Aplicación simple de escritorio para gestionar finanzas personales, desarrollada en Python con tkinter.

## Características

- ✅ Agregar ingresos y gastos
- ✅ Ver balance total en tiempo real
- ✅ Lista de todas las transacciones
- ✅ Eliminar transacciones
- ✅ Persistencia de datos en JSON
- ✅ Interfaz gráfica intuitiva

## Requisitos

- Python 3.6 o superior
- tkinter (incluido por defecto en Python)

## Instalación y Uso

1. Clona o descarga este proyecto
2. Ejecuta la aplicación:

```bash
python finanzas.py
```

## Cómo usar

1. **Agregar transacción**: Ingresa la descripción, monto y selecciona si es ingreso o gasto
2. **Ver balance**: El balance total se actualiza automáticamente en la parte superior
3. **Eliminar transacción**: Selecciona una transacción de la lista y haz clic en "Eliminar"
4. **Datos persistentes**: Todas las transacciones se guardan automáticamente en `transacciones.json`

## Estructura del Proyecto

```
final-project/
├── finanzas.py           # Aplicación principal
├── transacciones.json    # Datos (se crea automáticamente)
└── README.md            # Este archivo
```

## Principios de Diseño

El código sigue los principios **KISS**, **DRY** y **YAGNI**:
- **KISS** (Keep It Simple): Código simple y directo, sin complejidad innecesaria
- **DRY** (Don't Repeat Yourself): Funciones reutilizables, sin duplicación de código
- **YAGNI** (You Aren't Gonna Need It): Solo implementa lo necesario, sin funcionalidades extras