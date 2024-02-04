class Prestamo:
  usuario = []
  libro = []
  fechaPrestamo = ""
  fechaDevolucion = ""

  def __init__(self, _usuario, _libro, _fechaPrestamo, _fechaDevolucion):
    self.usuario = _usuario
    self.libro = _libro
    self.fechaPrestamo = _fechaPrestamo
    self.fechaDevolucion = _fechaDevolucion

  def getUsuario(self):
    return self.usuario

  def setUsuario(self, _usuario):
    self.usuario = _usuario

  def getLibro(self):
    return self.libro

  def setLibro(self, _libro):
    self.libro= _libro

  def getFechaPrestamo(self):
    return self.fechaPrestamo

  def setFechaPrestamo(self, _fechaPrestamo):
    self.fechaPrestamo = _fechaPrestamo

  def getFechaDevolucion(self):
    return self.fechaDevolucion

  def setFechaDevolcion(self, _fechaDevolucion):
    self.fechaDevolucion = _fechaDevolucion
