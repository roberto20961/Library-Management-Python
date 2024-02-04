class Usuario:
  nombre = ""
  apellidos = ""
  dni = ""
  direccion = ""
  telefono = ""

  def __init__(self, _nombre, _apellidos, _dni, _direccion, _telefono):
    self.nombre = _nombre
    self.apellidos = _apellidos
    self.dni = _dni
    self.direccion = _direccion
    self.telefono = _telefono

  def getNombre(self):
    return self.nombre

  def setNombre(self, _nombre):
    self.nombre = _nombre

  def getApellidos(self):
    return self.apellidos

  def setApellidos(self, _apellidos):
    self.apellidos = _apellidos

  def getDni(self):
    return self.dni

  def setDni(self, _dni):
    self.dni = _dni

  def getDireccion(self):
    return self.direccion

  def setDireccion(self, _direccion):
    self.direccion = _direccion

  def getTelefono(self):
    return self.telefono

  def setTelefono(self, _telefono):
    self.telefono = _telefono
