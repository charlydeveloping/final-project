"""
Aplicación de Finanzas Personales
Aplicación simple de escritorio para gestionar ingresos y gastos
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
from pathlib import Path


class FinanzasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Finanzas Personales")
        self.ventana.geometry("700x500")
        
        self.archivo_datos = Path("transacciones.json")
        self.transacciones = self.cargar_datos()
        
        self.crear_interfaz()
        self.actualizar_lista()
        self.actualizar_balance()
    
    def cargar_datos(self):
        """Carga las transacciones desde archivo JSON"""
        if self.archivo_datos.exists():
            with open(self.archivo_datos, 'r') as f:
                return json.load(f)
        return []
    
    def guardar_datos(self):
        """Guarda las transacciones en archivo JSON"""
        with open(self.archivo_datos, 'w') as f:
            json.dump(self.transacciones, f, indent=2)
    
    def crear_interfaz(self):
        """Crea los elementos de la interfaz gráfica"""
        # Frame superior para el balance
        frame_balance = tk.Frame(self.ventana, bg="#2c3e50", padx=10, pady=15)
        frame_balance.pack(fill="x")
        
        tk.Label(frame_balance, text="Balance Total:", 
                font=("Arial", 14, "bold"), bg="#2c3e50", fg="white").pack()
        
        self.label_balance = tk.Label(frame_balance, text="$0.00", 
                                      font=("Arial", 24, "bold"), bg="#2c3e50", fg="#2ecc71")
        self.label_balance.pack()
        
        # Frame para agregar transacciones
        frame_agregar = tk.LabelFrame(self.ventana, text="Nueva Transacción", 
                                      padx=15, pady=10)
        frame_agregar.pack(fill="x", padx=10, pady=10)
        
        # Descripción
        tk.Label(frame_agregar, text="Descripción:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_descripcion = tk.Entry(frame_agregar, width=30)
        self.entry_descripcion.grid(row=0, column=1, padx=5, pady=5)
        
        # Monto
        tk.Label(frame_agregar, text="Monto:").grid(row=0, column=2, sticky="w", pady=5)
        self.entry_monto = tk.Entry(frame_agregar, width=15)
        self.entry_monto.grid(row=0, column=3, padx=5, pady=5)
        
        # Tipo (Ingreso/Gasto)
        tk.Label(frame_agregar, text="Tipo:").grid(row=1, column=0, sticky="w", pady=5)
        self.combo_tipo = ttk.Combobox(frame_agregar, values=["Ingreso", "Gasto"], 
                                       state="readonly", width=27)
        self.combo_tipo.set("Gasto")
        self.combo_tipo.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón agregar
        btn_agregar = tk.Button(frame_agregar, text="Agregar", 
                               command=self.agregar_transaccion,
                               bg="#3498db", fg="white", padx=20)
        btn_agregar.grid(row=1, column=2, columnspan=2, pady=5)
        
        # Frame para lista de transacciones
        frame_lista = tk.LabelFrame(self.ventana, text="Transacciones", 
                                   padx=10, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")
        
        # Lista de transacciones
        self.lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, 
                               font=("Courier", 10))
        self.lista.pack(fill="both", expand=True)
        scrollbar.config(command=self.lista.yview)
        
        # Botón eliminar
        btn_eliminar = tk.Button(self.ventana, text="Eliminar Seleccionada", 
                                command=self.eliminar_transaccion,
                                bg="#e74c3c", fg="white", padx=20, pady=5)
        btn_eliminar.pack(pady=5)
    
    def agregar_transaccion(self):
        """Agrega una nueva transacción"""
        descripcion = self.entry_descripcion.get().strip()
        monto_texto = self.entry_monto.get().strip()
        tipo = self.combo_tipo.get()
        
        if not descripcion or not monto_texto:
            messagebox.showwarning("Advertencia", "Complete todos los campos")
            return
        
        try:
            monto = float(monto_texto)
            if monto <= 0:
                messagebox.showwarning("Advertencia", "El monto debe ser mayor a 0")
                return
        except ValueError:
            messagebox.showwarning("Advertencia", "El monto debe ser un número válido")
            return
        
        # Ajustar signo según tipo
        if tipo == "Gasto":
            monto = -abs(monto)
        else:
            monto = abs(monto)
        
        transaccion = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        }
        
        self.transacciones.append(transaccion)
        self.guardar_datos()
        self.actualizar_lista()
        self.actualizar_balance()
        
        # Limpiar campos
        self.entry_descripcion.delete(0, tk.END)
        self.entry_monto.delete(0, tk.END)
        self.combo_tipo.set("Gasto")
    
    def eliminar_transaccion(self):
        """Elimina la transacción seleccionada"""
        seleccion = self.lista.curselection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una transacción")
            return
        
        indice = seleccion[0]
        transaccion = self.transacciones[indice]
        
        confirmar = messagebox.askyesno("Confirmar", 
                                        f"¿Eliminar '{transaccion['descripcion']}'?")
        
        if confirmar:
            self.transacciones.pop(indice)
            self.guardar_datos()
            self.actualizar_lista()
            self.actualizar_balance()
    
    def actualizar_lista(self):
        """Actualiza la lista de transacciones en pantalla"""
        self.lista.delete(0, tk.END)
        
        for t in self.transacciones:
            monto_formato = f"${abs(t['monto']):,.2f}"
            linea = f"{t['fecha']} | {t['descripcion']:<25} | {monto_formato:>12} | {t['tipo']}"
            self.lista.insert(tk.END, linea)
    
    def actualizar_balance(self):
        """Actualiza el balance total"""
        balance = sum(t['monto'] for t in self.transacciones)
        
        color = "#2ecc71" if balance >= 0 else "#e74c3c"
        self.label_balance.config(text=f"${balance:,.2f}", fg=color)
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()


if __name__ == "__main__":
    app = FinanzasApp()
    app.ejecutar()
