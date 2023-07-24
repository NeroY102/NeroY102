class Alumno:
  def inicio(self,Nombre,Nota,):
    self.Nombre = Nombre
    self.Nota = Nota
  def impri(self):
    print("Nombre",self.Nombre)
    print("Nota",self.Nota )
  def fin(self):
    if self.Nota>=10:
      print (APROBADO)
    else:
      print(REPROBADO)
    
person1=Alumno
person1.inicio("Pedro",2)
person1.impri()
person1.fin()

person2=Alumno
person2.inicio("Ana",10)
person2.impri()
person2.fin()

