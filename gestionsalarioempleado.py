class procesador:
	def __init__(self, datos):
		self.datos = datos
	def procesador(self):
		for numero in self.datos:
			if numero == 3:
				continue
			if numero == 5:
				print(f"El programa va a terminar con el número: {numero}")
				break
			else:
				print(f"El numero del procesador es: {numero}")
lista = [1,2,3,4,5,6]
calculo = procesador(lista)
calculo.procesador()
