""" En python, las variables en si no tienen un tipo de dato
que nosotros podamos definir, sino que los objetos  a los que se hace 
referencia las varibales ya tienen sus propios tipos de datos,ya que python inferira
el tipo de dato de una variable a partir del objeto asignado"""

#Ejemplo
nombre = "Cristiam ramos"
edad = 23

cursos=["python","java","c++","golang"]

"""Y con la siguiente funcion type(nombre de la variable) 
conoceremos que tipo de dato es la variable, ya que devuelve el tipo de dato del objeto  """

print(type(nombre)) #Lo ponemos dentrode un print la funcion ya que no estamos en el mismo interprete de python ssi no en un ide
print(type(edad))
print(type(cursos))
