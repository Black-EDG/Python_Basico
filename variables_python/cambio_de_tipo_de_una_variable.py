
"""en Python, las variables en sí no tienen tipos de datos
   En cambio, los objetos a los que hacen referencia las variables tienen tipos 
"""

nombre="Yhury cristiam"
edad = 19
cursos = ["python","java","c++","golang"]

print(type(nombre))
print(type(edad))
print(type(cursos))

"""Ahora ya que python esta escrito dinamicamente, puedes hacer las variables
   hagan referencia a objetos de diferentes tipos de datos en diferentes momentos simplemente reasignando la variable
   """

# Ejemplo

edad = "19"

print(type(edad))
"""Aqui vemos que edad ahora es un str"""

cursos = {"python","java","c++","golang"}
print(type(cursos))
"""Aqui observamos que ahora cursos se refiere a un objeto de tipo set"""

