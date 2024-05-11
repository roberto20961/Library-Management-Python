from os import system
from claseBiblioteca import Biblioteca
from claseLibro import Libro
from claseBibliotecario import Bibliotecario
from claseUsuario import Usuario
from clasePrestamo import Prestamo


def pedirNumeroEntero():

  correcto = False
  num = 0
  while (not correcto):
    try:
      num = int(input("Introduce un numero entero: "))
      correcto = True
    except ValueError:
      print('Error, introduce un numero entero')

  return num


salir = False
opcion = 0

usuario1 = Usuario("Carlos", "Isidro", "AAAA1", "Avnd A", "345345345")
usuario2 = Usuario("Manuel", "Godoy", "BBBB2", "Calle Ac", "123123123")
usuario3 = Usuario("Francisco", "Francisco", "CCCC3", "Calle De",
                   "789789789")
usuario4 = Usuario("Pepe", "Botella", "DDDD4", "Calle Francia", "890890890")
usuario5 = Usuario("Almirante", "Topete", "EEEE5", "Calle Gloriosa",
                   "567567567")
usuario6 = Usuario("Praxedes", "Sagasta", "FFFF6", "Calle 1903DEP",
                   "134134134")
usuario7 = Usuario("Canovas", "Castillo", "GGGG7", "Calle El",
                   "389389389")
libro1 = Libro("Carlo", "Carlitos", "Tuit", "111111")
libro2 = Libro("Asi es la p*ta vida", "Jordi Wild", "Real", "222222")
libro3 = Libro("El trabajo", "David", "Locura", "333333")
libro4 = Libro("Wigetta 1", "Vegetta777", "Comics", "444444")
libro5 = Libro("Wigetta 2", "WillyRex", "Comics", "555555")
libro6 = Libro("Republica", "Platon", "Filosofia", "666666")
libro7 = Libro("Politica", "Glaucon", "Filosofia", "777777")
libro8 = Libro("Mates", "Baquero", "Educativo", "888888")
libro9 = Libro("Enanitos", "Nicolin", "Fantasia", "999999")
libro10 = Libro("Proposicion", "Rosales", "Algebra",
                "000000")
prestamo1 = Prestamo(usuario1, libro1, "20/04/2023", "28/05/2023")
prestamo2 = Prestamo(usuario2, libro2, "20/04/2023", "03/07/2023")
prestamo3 = Prestamo(usuario3, libro3, "20/04/2023", "25/11/2023")
prestamo4 = Prestamo(usuario4, libro4, "19/04/2023", "20/05/2023")
prestamo5 = Prestamo(usuario5, libro5, "20/02/2023", "10/03/2023")
prestamo6 = Prestamo(usuario6, libro6, "20/04/2023", "13/05/2023")

bibliotecario1 = Bibliotecario("Roberto", "Mindrila", "1111A",
                               [prestamo1, prestamo2, prestamo3])
bibliotecario2 = Bibliotecario("Fran", "Rojas", "2222B",
                               [prestamo4, prestamo5, prestamo6])

biblioteca = Biblioteca(
  "Miniboys", "Avenida de España", "Sabinillas", [
    libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9,
    libro10
  ], [bibliotecario1, bibliotecario2],
  [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7])

while not salir:
  print("--BIBLIOTECA--")
  print("")
  print("1. Nuevo bibliotecario")
  print("2. Dar de baja un bibliotecario")
  print("3. Nuevo libro")
  print("4. Dar de baja un libro")
  print("5. Nuevo usuario")
  print("6. Dar de baja un usuario")
  print("7. Listar todos los libros de la biblioteca")
  print("8. Listar todos los usuarios del sistema")
  print("9. Préstamo")
  print("10. Devolución")
  print("11. Buscar libro")
  print("12. Buscar usuarios")
  print("13. Imprimir todos los préstamos")
  print("14. Imprimir todos los préstamos sobrepasados")
  print("15. Salir")

  print("Elige una opcion")

  opcion = pedirNumeroEntero()

  if opcion == 1:
    print("Opcion 1. Nuevo bibliotecario")
    print("---------------------------------")

    nombreB = input("Introduce el nombre: ")
    apellidosB = input("Introduce los apellidos: ")
    dniB = input("Introduce el DNI: ")
    bibliotecarioNuevo = Bibliotecario(nombreB, apellidosB, dniB, [])
    biblioteca.altaBibliotecario(bibliotecarioNuevo, dniB)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 2:
    print("Opcion 2. Dar de baja un bibliotecario")
    print("---------------------------------")

    dniBE = input("Introduce el DNI del bibliotecario: ")
    biblioteca.bajaBibliotecario(dniBE)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 3:
    print("Opcion 3. Nuevo libro")
    print("---------------------------------")

    tituloL = input("Introduce el titulo: ")
    autorL = input("Introduce el nombre del autor: ")
    generoL = input("Introduce el genero: ")
    isbnL = input("Introduce el ISBN: ")
    libroNuevo = Libro(tituloL, autorL, generoL, isbnL)
    biblioteca.altaLibro(isbnL, libroNuevo)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 4:
    print("Opcion 4. Dar de baja un libro")
    print("---------------------------------")

    isbnLE = input("Introduce el ISBN del libro: ")
    biblioteca.bajaLibro(isbnLE)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 5:
    print("Opcion 5. Nuevo usuario")
    print("---------------------------------")

    nombreU = input("Introduce el nombre del usuario: ")
    apellidosU = input("Introduce los apellidos: ")
    dniU = input("Introduce el DNI: ")
    direccionU = input("Introduce la direccion: ")
    telefonoU = input("Introduce el telefono: ")
    usuarioNuevo = Usuario(nombreU, apellidosU, dniU, direccionU, telefonoU)
    biblioteca.altaUsuario(dniU, usuarioNuevo)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 6:
    print("Opcion 6. Dar de baja un usuario")
    print("---------------------------------")

    dniUE = input("Introduce el DNI del usuario: ")
    biblioteca.bajaUsuario(dniUE)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 7:
    print("Opcion 7. Listar todos los libros de la biblioteca")
    print("---------------------------------")

    for i in biblioteca.listaLibros:
      print("***********************")
      print("Título: ", i.getTitulo())
      print("Autor: ", i.getAutor())
      print("Genero: ", i.getGenero())
      print("ISBN: ", i.getIsbn())
      print("***********************")

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 8:
    print("Opcion 8. Listar todos los usuarios del sistema")
    print("---------------------------------")

    for i in biblioteca.listaUsuarios:
      print("***********************")
      print("Nombre: ", i.getNombre())
      print("Apellidos: ", i.getApellidos())
      print("DNI: ", i.getDni())
      print("Dirección: ", i.getDireccion())
      print("Telefono: ", i.getTelefono())
      print("***********************")

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 9:
    print("Opcion 9. Préstamo")
    print("---------------------------------")

    dniBi = input("Introduce el DNI del bibliotecario: ")
    para = 0
    for i in biblioteca.listaBibliotecarios:
      if dniBi == i.getDni():
        para = 1
        bibliotecarioP = i
        print("Nombre: ", i.getNombre())
        print("Apellidos: ", i.getApellidos())
    if para == 0:
      print("El bibliotecario no existe...")
    if para == 1:
      dniUi = input("Introduce el DNI del usuario: ")
      para1 = 0
      for i in biblioteca.listaUsuarios:
        if dniUi == i.getDni():
          para1 = 1
          usuarioP = i
          print("Nombre: ", i.getNombre())
          print("Apellidos: ", i.getApellidos())
      if para1 == 0:
        print("El usuario no existe...")
      if para1 == 1:
        isbnLi = input("Introduce el ISBN del libro: ")
        para2 = 0
        for i in biblioteca.listaLibros:
          if isbnLi == i.getIsbn():
            para2 = 1
            libroP = i
            print("Titulo: ", i.getTitulo())
        if para2 == 0:
          print("El libro no existe...")
        if para2 == 1:
          pres = 1
          pres2 = 1
          for bibliotecario in biblioteca.getListaBibliotecarios():
            for i in bibliotecario.listaPrestamos: 
              j = i.getUsuario()
              if usuarioP.getDni() == j.getDni():
                pres = 0
            for i in bibliotecario.listaPrestamos:
              j = i.getLibro()
              if libroP.getTitulo() == j.getTitulo():
                pres2 = 0

          if pres2 == 0:
            print("El libro ya está prestado...")
          if pres == 0:
            print("El usuario ya tiene un prestamo...")
            pres2 = 1
          elif pres2 == 1 and pres == 1:
            bibliotecarioP.realizarPrestamo(usuarioP, libroP)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 10:
    print("Opcion 10. Devolución")
    print("---------------------------------")

    dniEL = input("Introduce el DNI del usuario: ")
    para6 = 0
    for i in biblioteca.listaUsuarios:
      if dniEL == i.getDni():
        para6 = 1
    if para6 == 0:
      print("El usuario no existe...")
    pres = 1
    if para6 == 1:
      for bibliotecario in biblioteca.getListaBibliotecarios():
        for i in bibliotecario.listaPrestamos:
          j = i.getUsuario()
          if dniEL == j.getDni():
            pres = 0
            elim = i
            h = bibliotecario

    if pres == 1:
      print("El usuario no tiene ningún préstamo realizado...")
    elif para6 == 1 and pres == 0:
      h.devolucion(elim, h)

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 11:
    print("Opcion 11. Buscar libro")
    print("---------------------------------")

    isbnBL = input("Introduce el ISBN del libro: ")
    para = 0
    for i in biblioteca.listaLibros:
      if isbnBL == i.getIsbn():
        para = 1
        print("***********************")
        print("Titulo: ", i.getTitulo())
        print("Autor: ", i.getAutor())
        print("Genero: ", i.getGenero())
        print("ISBN: ", i.getIsbn())
        print("***********************")

    if para == 0:
      print("El libro no está en la biblioteca...")

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 12:
    print("Opcion 12. Buscar usuarios")
    print("---------------------------------")

    dniBU = input("Introduce el DNI del usuario: ")
    para = 0
    for i in biblioteca.listaUsuarios:
      if dniBU == i.getDni():
        para = 1
        print("***********************")
        print("Nombre: ", i.getNombre())
        print("Apellidos: ", i.getApellidos())
        print("DNI: ", i.getDni())
        print("Direccion: ", i.getDireccion())
        print("Telefono", i.getTelefono())
        print("***********************")

    if para == 0:
      print("El usuario no está registrado en la biblioteca...")

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 13:
    print("Opcion 13. Imprimir todos los préstamos")
    print("---------------------------------")

    for i in biblioteca.listaBibliotecarios:
      for j in i.listaPrestamos:
        k = j.getUsuario()
        print("*******************************")
        print("Nombre usuario: ", k.getNombre())
        print("Apellidos usuario: ", k.getApellidos())
        print("DNI usuario: ", k.getDni())
        l = j.getLibro()
        print("Titulo libro: ", l.getTitulo())
        print("ISBN libro: ", l.getIsbn())
        print("Fecha Préstamo: ", j.getFechaPrestamo())
        print("Fecha Devolución: ", j.getFechaDevolucion())
        print("*******************************")
    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 14:
    print("Opcion 14. Imprimir todos los préstamos sobrepasados")
    print("---------------------------------")
    fecha = input("Introduce la fecha actual (dd/mm/aa): ")
    f = fecha.split("/")
    no = 0
    pasado = 0
    for i in biblioteca.listaBibliotecarios:
      for j in i.listaPrestamos:
        pasado = 0
        n = j.getUsuario()
        w = j.getLibro()
        k = j.getFechaDevolucion()
        m = k.split("/")
        if m[2] < f[2]:
          pasado = 1
          no = no + 1
        elif m[2] > f[2]:
          pasado = 0
        else:
          if m[1] < f[1]:
            pasado = 1
            no = no + 1
          elif m[1] > f[1]:
            pasado = 0
          else:
            if m[0] < f[0]:
              pasado = 1
              no = no + 1
            elif m[0] > f[0]:
              pasado = 0
            else:
              pasado = 0
        
        if pasado == 1:
          print("*******************************")
          print("Nombre usuario: ", n.getNombre())
          print("Apellidos usuario: ", n.getApellidos())
          print("DNI usuario: ", n.getDni())
          l = j.getLibro()
          print("Titulo libro: ", w.getTitulo())
          print("ISBN libro: ", w.getIsbn())
          print("Fecha Préstamo: ", j.getFechaPrestamo())
          print("Fecha Devolución: ", j.getFechaDevolucion())
          print("*******************************")

    if no == 0:
      print("No hay préstamos sobrepasados...")

    input("Presione una tecla para continuar...")
    system("clear")

  elif opcion == 15:
    salir = True

  else:
    print("Introduce un numero entre 1 y 14, 15 para salir")
    input("Presione una tecla para continuar...")
    system("clear")

print("Fin")
