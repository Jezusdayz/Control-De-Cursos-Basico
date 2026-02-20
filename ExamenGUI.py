import tkinter as tk
from tkinter import messagebox

cursos = {}

def agregar_curso():
    nombre = entry_curso.get()
    if nombre:
        if nombre not in cursos:
            cursos[nombre] = []
            messagebox.showinfo("Éxito", f"Curso '{nombre}' agregado")
        else:
            messagebox.showwarning("Error", "El curso ya existe")
    entry_curso.delete(0, tk.END)

def agregar_calificacion():
    nombre = entry_curso.get()
    calificacion = entry_calificacion.get()
    
    if nombre in cursos:
        try:
            cursos[nombre].append(float(calificacion))
            messagebox.showinfo("Éxito", "Calificación agregada")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
    else:
        messagebox.showerror("Error", "El curso no existe")
    
    entry_calificacion.delete(0, tk.END)

def mostrar_mejor_promedio():
    mejor = -1
    mejores = []
    
    for curso in cursos:
        if len(cursos[curso]) > 0:
            promedio = sum(cursos[curso]) / len(cursos[curso])
            if promedio > mejor:
                mejor = promedio
                mejores = [curso]
            elif promedio == mejor:
                mejores.append(curso)
    
    if mejor == -1:
        resultado.set("No hay calificaciones registradas")
    else:
        resultado.set(f"Mejor promedio: {mejor}\nCursos: {', '.join(mejores)}")

def listar_cursos():
    texto = ""
    for curso in cursos:
        texto += f"\nCurso: {curso}\n"
        texto += f"Calificaciones: {cursos[curso]}\n"
        if len(cursos[curso]) > 0:
            promedio = sum(cursos[curso]) / len(cursos[curso])
            texto += f"Promedio: {promedio}\n"
        else:
            texto += "Promedio: Sin calificaciones\n"
    
    resultado.set(texto)


# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Control de Cursos")
ventana.geometry("400x400")

# Widgets
tk.Label(ventana, text="Nombre del Curso").pack()
entry_curso = tk.Entry(ventana)
entry_curso.pack()

tk.Label(ventana, text="Calificación").pack()
entry_calificacion = tk.Entry(ventana)
entry_calificacion.pack()

tk.Button(ventana, text="Agregar Curso", command=agregar_curso).pack(pady=5)
tk.Button(ventana, text="Agregar Calificación", command=agregar_calificacion).pack(pady=5)
tk.Button(ventana, text="Mostrar Mejor Promedio", command=mostrar_mejor_promedio).pack(pady=5)
tk.Button(ventana, text="Listar Cursos", command=listar_cursos).pack(pady=5)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left").pack()

ventana.mainloop()