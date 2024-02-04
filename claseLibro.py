class Libro:
  titulo = ""
  autor = ""
  genero = ""
  isbn = 0

  def __init__(
    self,
    _titulo,
    _autor,
    _genero,
    _isbn,
  ):
    self.titulo = _titulo
    self.autor = _autor
    self.genero = _genero
    self.isbn = _isbn

  def getTitulo(self):
    return self.titulo

  def setTitulo(self, _titulo):
    self.titulo = _titulo

  def getAutor(self):
    return self.autor

  def setAutor(self, _autor):
    self.autor = _autor

  def getGenero(self):
    return self.genero

  def setGenero(self, _genero):
    self.genero = _genero

  def getIsbn(self):
    return self.isbn

  def setIsbn(self, _isbn):
    self.isbn = _isbn
