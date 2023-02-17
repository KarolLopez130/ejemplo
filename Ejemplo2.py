import Ejemplo1 as ej

cliente_Uno = ej.Cliente("123456","Pepe","pepe@gmail.com",20)
print(cliente_Uno.get_Documento())
print(cliente_Uno.get_Nombre())


cliente_Uno.set_Nombre("Ramon")
print(cliente_Uno.get_Nombre())
