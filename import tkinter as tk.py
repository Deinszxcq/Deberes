import tkinter as tk
from tkinter import messagebox


historial = []


def convertir():
    numero = entrada_numero.get().strip()
    sistema = opcion.get()

    try:
        
        if sistema == "Decimal":
            decimal = int(numero)
        elif sistema == "Binario":
            decimal = int(numero, 2)
        elif sistema == "Octal":
            decimal = int(numero, 8)
        elif sistema == "Hexadecimal":
            decimal = int(numero, 16)
        else:
            messagebox.showerror("Error", "Selecciona un sistema numérico")
            return

        
        binario = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:].upper()

        
        resultado_decimal.config(text=str(decimal))
        resultado_binario.config(text=binario)
        resultado_octal.config(text=octal)
        resultado_hexadecimal.config(text=hexadecimal)

        
        conversion = f"Número: {numero} ({sistema}) → Decimal: {decimal} | Binario: {binario} | Octal: {octal} | Hexadecimal: {hexadecimal}"
        historial.append(conversion)

    except ValueError:
        messagebox.showerror("Error", "Número inválido para el sistema seleccionado")


def mostrar_historial():
    if not historial:
        messagebox.showinfo("Historial", "No hay conversiones registradas todavía.")
        return

    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de Conversiones")
    ventana_historial.geometry("500x300")

    tk.Label(ventana_historial, text="Historial de Conversiones", font=("Arial", 14, "bold")).pack(pady=10)

    
    texto_historial = tk.Text(ventana_historial, wrap=tk.WORD, width=60, height=10)
    texto_historial.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    
    scroll = tk.Scrollbar(ventana_historial, command=texto_historial.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    texto_historial.config(yscrollcommand=scroll.set)

   
    for linea in historial:
        texto_historial.insert(tk.END, linea + "\n\n")

    texto_historial.config(state=tk.DISABLED)


ventana = tk.Tk()
ventana.title("Convertidor de Sistemas Numéricos")
ventana.geometry("420x400")


tk.Label(ventana, text="Convertidor de Sistemas Numéricos", font=("Arial", 14, "bold")).pack(pady=10)


frame_input = tk.Frame(ventana)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Ingresa el número:").grid(row=0, column=0, padx=5, pady=5)
entrada_numero = tk.Entry(frame_input, width=15)
entrada_numero.grid(row=0, column=1, padx=5, pady=5)


opcion = tk.StringVar()
opcion.set("Decimal")

frame_opciones = tk.Frame(ventana)
frame_opciones.pack(pady=5)

tk.Label(frame_opciones, text="Sistema del número ingresado:").pack()
tk.Radiobutton(frame_opciones, text="Decimal", variable=opcion, value="Decimal").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_opciones, text="Binario", variable=opcion, value="Binario").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_opciones, text="Octal", variable=opcion, value="Octal").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_opciones, text="Hexadecimal", variable=opcion, value="Hexadecimal").pack(side=tk.LEFT, padx=5)


tk.Button(ventana, text="Convertir", command=convertir, bg="blue", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
tk.Button(ventana, text="Ver Historial", command=mostrar_historial, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=5)


frame_resultados = tk.Frame(ventana)
frame_resultados.pack(pady=10)

tk.Label(frame_resultados, text="Resultados:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(frame_resultados, text="Decimal:").grid(row=1, column=0, sticky="e", padx=5)
resultado_decimal = tk.Label(frame_resultados, text="", fg="red")
resultado_decimal.grid(row=1, column=1, sticky="w")

tk.Label(frame_resultados, text="Binario:").grid(row=2, column=0, sticky="e", padx=5)
resultado_binario = tk.Label(frame_resultados, text="", fg="green")
resultado_binario.grid(row=2, column=1, sticky="w")

tk.Label(frame_resultados, text="Octal:").grid(row=3, column=0, sticky="e", padx=5)
resultado_octal = tk.Label(frame_resultados, text="", fg="orange")
resultado_octal.grid(row=3, column=1, sticky="w")

tk.Label(frame_resultados, text="Hexadecimal:").grid(row=4, column=0, sticky="e", padx=5)
resultado_hexadecimal = tk.Label(frame_resultados, text="", fg="purple")
resultado_hexadecimal.grid(row=4, column=1, sticky="w")

ventana.mainloop()
