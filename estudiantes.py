import procesar_db as modulo

while True:
    print("")
    print("=== Alumnos ===")
    print("1. Registrar Alumno")
    print("2. Lista Alumnos")
    print("3. Buscar Alumno")
    print("4. Actualizar Carrera del Alumno")
    print("5. Eliminar Alumno")
    print("6. Cerrar Sistema")
    print("==========================")
    opcion = int(input("Elije una opción (1 - 6): ").strip())
    print("==========================")
    print("")

    if opcion == 1:
       print(" === Datos del Alumno === ")
       nombre = input("Nombre: ").strip().capitalize()
       apellido = input("Apellido: ").strip().capitalize()
       carrera = input("Carrera: ").strip().capitalize()
       edad = int(input("Edad: ").strip())

       resultado = modulo.registrar(nombre, apellido, carrera, edad)

       if resultado == 1:
             print("=== Error en el proceso de insertar registro ===")
       else:
             print("=== !!! El Alumno fue regsitrado correctamente ¡¡¡ ===")

    elif opcion == 2:
        print(" === Listar Alumnos === ")
        resultado = modulo.listar()
        print(resultado)

    elif opcion == 3:
        print(" === Buscar Alumno === ")
        id = int(input("Ingrese el ID del alumno: ").strip())

        resultado = modulo.Listar_Por_Id(id)
        if resultado == 1:
            print("=== Error al buscar alumno por ID ===")
        elif resultado == ():
            print("=== No existe un alumno con ese ID")
        else:
            print(resultado)

    elif opcion == 4:
        print(" === Actualizar carrera del Alumno === ")
        id = int(input("Ingrese el ID del alumno: ").strip())

        resultado = modulo.Listar_Por_Id(id)
        if resultado == 1:
            print("=== Error al buscar alumno por ID ===")
        elif resultado == ():
            print("=== No existe un alumno con ese ID")
        else:
            carrera = input("Ingrese la nueva carrera: ").strip().capitalize()

            resultado = modulo.actualizar_carrera(carrera, id)
            if resultado == 1:
                print("=== Error al actualizar la carrera ===")
            else:
                print("=== El cambio de carrera fue exitoso")

    elif opcion == 5:
        print(" === Eliminar Alumno === ")
        id = int(input("Ingrese el ID del alumno: ").strip())

        resultado = modulo.Listar_Por_Id(id)
        if resultado == 1:
            print("=== Error, intenta nuevamente ===")
        elif resultado == ():
            print("=== No existe un alumno con ese ID")
        else:
            resultado = modulo.eliminar(id)
            if resultado == 1:
                print("=== Error al eliminar alumno===")
            else:
                print("=== El alumno fue eliminado correctamente de la DB")

    elif opcion == 6:
        print("======= Sistema Cerrado ========")
        break
    else:
        print("ERROR: INTENTA NUEVAMENTE")