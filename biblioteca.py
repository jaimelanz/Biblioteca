

class Libro:
    def __init__(self, nombre, tipo, editorial, anio):
        self.nombre = nombre
        self.tipo = tipo
        self.editorial = editorial
        self.anio = anio

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return self.nombre

    def getNombre(self):
        return  self.nombre

    def setTipo(self, nuevoTipo):
        self.tipo = nuevoTipo
        return self.tipo

    def getTipo(self):
        return self.tipo

    def setEditorial(self, nuevaEditorial):
        self.editorial = nuevaEditorial
        return self.nombre

    def getEditorial(self):
        return self.editorial

    def setAnio(self,nuevoAnio):
        self.a = nuevoAnio
        return self.nombre

    def getAnio(self):
        return self.anio


class Copia:
    def __init__(self, codigo_copia, estado):
        self.codigo_copia = codigo_copia
        self.estado = estado

    def getCodigo(self):
        return self.codigo_copia

    def setEstado(self, nuevoEstado):
        self.estado = nuevoEstado

    def getEstado(self):
         return self.estado

    def prestar_copia(self, codigoCopia):
        pass


class Autor:
    def __init__(self, nombre, pais, fechaNac):
        self.nombre = nombre
        self.pais = pais
        self.fechaNac = fechaNac

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return self.nombre

    def getNombre(self):
        return  self.nombre

    def setPais(self, nuevoPais):
        self.pais = nuevoPais
        return self.pais

    def getPais(self):
        return  self.pais

    def setFecha(self, nuevaFecha):
        self.fechaNac = nuevaFecha
        return self.fechaNac

    def getFecha(self):
        return  self.fechaNac


class Lector:
    def __init__(self, codigo_lector, estado):
        self.codigo_lector = codigo_lector
        self.estado = estado

    def setEstado(self, nuevoEstado):
        self.estado = nuevoEstado
        return self.estado

    def getEstado(self):
        return  self.estado

    def reservar(self, codigo_libro):
        pass
    
    def devolver(self, codigo_libro):
        pass

