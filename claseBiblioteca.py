class Biblioteca:
  nombre = ""
  direccion = ""
  localidad = ""
  listaLibros = []
  listaBibliotecarios = []
  listaUsuarios = []

  def __init__(self, _nombre, _direccion, _localidad, _listaLibros,
               _listaBibliotecarios, _listaUsuarios):
    self.nombre = _nombre
    self.direccion = _direccion
    self.localidad = _localidad
    self.listaLibros = _listaLibros
    self.listaBibliotecarios = _listaBibliotecarios
    self.listaUsuarios = _listaUsuarios

  def getNombre(self):
    return self.nombre

  def setNombre(self, _nombre):
    self.nombre = _nombre

  def getDireccion(self):
    return self.direccion

  def setDireccion(self, _direccion):
    self.direccion = _direccion

  def getLocalidad(self):
    return self.localidad

  def setLocalidad(self, _localidad):
    self.localidad = _localidad

  def getListaLibros(self):
    return self.listaLibros

  def setListaLibros(self, _listaLibros):
    self.listaLibros = _listaLibros

  def getListaBibliotecarios(self):
    return self.listaBibliotecarios

  def setListaBibliotecarios(self, _listaBibliotecarios):
    self.listaBibliotecarios = _listaBibliotecarios

  def getListaUsuarios(self):
    return self.listaUsuarios

  def setListaUsuarios(self, _listaUsuarios):
    self.listaUsuarios = _listaUsuarios

  def altaBibliotecario(self, bibliotecarioNuevo, _dni):
    ya = []
    for i in self.listaBibliotecarios:
      ya.append(i.getDni())
    if _dni not in ya:
      self.listaBibliotecarios.append(bibliotecarioNuevo)
      print("Bibliotecario añadido con éxito...")
    else:
      print("El bibliotecario ya está registrado...")

  def bajaBibliotecario(self, _dniBE):
    esta = False
    conta = -1
    for i in self.listaBibliotecarios:
      conta += 1
      if i.getDni() == _dniBE:
        self.listaBibliotecarios.pop(conta)
        esta = True
    if esta:
      print("Bibliotecario eliminado con exito...")
    else:
      print("El bibliotecario no está registrado en la biblioteca...")

  def altaLibro(self, isbnL, libroNuevo):
    ya = []
    for i in self.listaLibros:
      ya.append(i.getIsbn())
    if isbnL not in ya:
      self.listaLibros.append(libroNuevo)
      print("Libro añadido con éxito...")
    else:
      print("El libro ya está registrado...")

  def bajaLibro(self, isbnLE):
    esta = False
    conta = -1
    for i in self.listaLibros:
      conta += 1
      if i.getIsbn() == isbnLE:
        self.listaLibros.pop(conta)
        esta = True
    if esta:
      print("Libro eliminado con exito...")
    else:
      print("El libro no está registrado en la biblioteca...")

  def altaUsuario(self, dniU, usuarioNuevo):
    ya = []
    for i in self.listaUsuarios:
      ya.append(i.getDni())
    if dniU not in ya:
      self.listaUsuarios.append(usuarioNuevo)
      print("Usuario añadido con éxito...")
    else:
      print("El usuario ya está registrado...")

  def bajaUsuario(self, dniUE):
    esta = False
    conta = -1
    for i in self.listaUsuarios:
      conta += 1
      if i.getDni() == dniUE:
        self.listaUsuarios.pop(conta)
        esta = True
    if esta:
      print("Usuario eliminado con exito...")
    else:
      print("El usuario no está registrado en la biblioteca...")
