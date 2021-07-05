class Departamentos:

    def __init__(self):
        pass
    
    @property
    def precio(self):               #cuando se ejecute departamento.precio
        print("Metodo getter")
        return self._precio         #retornar el atributo privado _precio
    
    @precio.setter                  #setter, se ejecutará cuando se intente cambiar los valores
    def precio(self, nuevo_valor):  
        print("Metodo setter")
        if nuevo_valor < 1000 or nuevo_valor > 200000:  #si valor es menor a 1000 o mayor a 200000
            raise ValueError('No es posible cambiar a estos valores')   #arrojamos error
        else:                                          
            self._precio = nuevo_valor                  #asignamos el nuevo valor
            print(f'El nuevo valor del departamento es: {self._precio}')    #imprimimos el nuevo valor

dep = Departamentos()

dep.precio = 6000

print(dep.precio)
