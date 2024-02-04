from clasePrestamo import Prestamo

class Bibliotecario:
  nombre = ""
  apellidos = ""
  dni = ""
  listaPrestamos = []

  def __init__(
    self,
    _nombre,
    _apellidos,
    _dni,
    _listaPrestamos,
  ):
    self.nombre = _nombre
    self.apellidos = _apellidos
    self.dni = _dni
    self.listaPrestamos = _listaPrestamos

  def getNombre(self):
    return self.nombre

  def setNombre(self, _nombre):
    self.nombre = _nombre

  def getApellidos(self):
    return self.apellidos

  def setApellidos(self, _apellidos):
    self.autor = _apellidos

  def getDni(self):
    return self.dni

  def setDni(self, _dni):
    self.dni = _dni

  def getListaPrestamos(self):
    return self.listaPrestamos

  def setIsbn(self, _listaPrestamos):
    self.listaPrestamos = _listaPrestamos

  def realizarPrestamo(self, usuarioP, libroP):
    fechaPrestamo = input("Introduce la fecha del préstamo (dd/mm/aa): ")
    fechaDevolucion = input(
       "Introduce la fecha de la devolución (dd/mm/aa): ")
    prestamo = Prestamo(usuarioP, libroP, fechaPrestamo, fechaDevolucion)
    self.listaPrestamos.append(prestamo)
    print("Préstamo realizado con éxito...")

  def devolucion(self, elim, j):
    self.listaPrestamos.remove(elim)
    print("Libro devuelto...")
