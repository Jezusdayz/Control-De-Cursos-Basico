#Funcion Menu
def menu():
    print('Sistema de Control de Cursos\nSeleccione acción a realizar\n1. Agregar curso\n2. Agregar calificación a curso\n3. Mostrar promedio por curso\n4. Mostrar curso con mejor promedio\n5. Listar todos los cursos\n6. Salir')

#Funcion agrega cursos
def agregarCurso(cursos):
    while True:
        nombre = input("Escriba el nombre del curso\nO escriba S para SALIR: ")
        if nombre == "S":
            break
        if nombre not in cursos:
            cursos[nombre] = []
            print("Se ha agregado el curso", nombre)
        else:
            print("El curso ya existe")
    return cursos

#Funcion agrega calificaicones a los cursos
def agregarCalificacion(cursos):
    while True:
        nombre = input("Ingrese el nombre del curso al que desea agregar calificaciones\nO escriba S para SALIR: ")
        if nombre == "S":
            break
        if nombre in cursos:
            while True:
                calificacion = input("Ingrese la calificación del curso\nO escriba S para SALIR: ")
                if calificacion == "S":
                    break
                try:
                    cursos[nombre].append(float(calificacion))
                    print("Calificación agregada correctamente")
                except ValueError:
                    print("Ingrese un número válido")
        else:
            print("El curso no existe, intente de nuevo")
    return cursos

#Funcion que Muestra el promedio de cada curso
def mostrarPromedio(cursos):
    while True:
        nombre = input("Escriba el nombre del Curso que desee promediar\n o escriba S para SALIR: ")
        
        if nombre == 'S':
            break
        
        if nombre in cursos:
            if len(cursos[nombre]) > 0:
                promedio = sum(cursos[nombre]) / len(cursos[nombre])
                print("El promedio es:", promedio)
            else:
                print("El curso no tiene calificaciones")
        else:
            print("El curso no existe")
    
    return cursos

#Funcion que muestra el mejor promedio de todos los cursos, o en su caso, si hay mas de uno, mostrara cuales
def mostrarMejorPromedio(cursos):
    mejprom = -1
    mejcur = []
    for curso in cursos:
        if len(cursos[curso]) > 0:
            promedio = sum(cursos[curso]) / len(cursos[curso])
            if promedio > mejprom:
                mejprom = promedio
                mejcur = [curso]  # reinicia la lista
            elif promedio == mejprom:
                mejcur.append(curso)
    if mejprom == -1:
        print("No hay cursos con calificaciones registradas.")
    else:
        print("El mejor promedio es:", mejprom)
        print("Curso(s) con mejor promedio:")
        for curso in mejcur:
            print("-", curso)

#Funcion que muestra todos los cursos, sus calificaciones almacenadas y promedio.
def listarCursos(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return
    for curso in cursos:
        print("\nCurso:", curso)
        print("Calificaciones:", cursos[curso])
        if len(cursos[curso]) > 0:
            promedio = sum(cursos[curso]) / len(cursos[curso])
            print("Promedio:", promedio)
        else:
            print("Promedio: No tiene calificaciones")

cursos = {}

# Funcionalidad del menu
while True:
    menu()
    opcion=int(input('Ingrese opcion: '))
    match opcion:
        case 1:
            cursos = agregarCurso(cursos)
        case 2:
            cursos = agregarCalificacion(cursos)
        case 3:
            mostrarPromedio(cursos)
        case 4:
            mostrarMejorPromedio(cursos)
        case 5:
            listarCursos(cursos)
        case 6:
            print('Saliendo del programa...')
            break