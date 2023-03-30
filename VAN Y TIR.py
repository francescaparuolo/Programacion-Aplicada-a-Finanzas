

class FF():
    def __init__(self,tupla=tuple()):
        self.flujos=tupla
        
    def van(self,tasa, n=0):
        """ Calculo de valor actual neto recursivo
            Inputs: 
                1 - tasa (posicional)
                2 - n posicion en el vector ( default = 0, named argument ). 
                    Sirve para manejar recursivamene las iteraciones 
                    sin alterar la lista del flujo de fondos  
        """
        if len(self.flujos)>0:
            if n==len(self.flujos):
                salida = 0
            else:
                salida = self.flujos[n]+1.0/(1.0+tasa)*self.van(tasa, n=n+1)
        else:
            print('\n',"La tupla de flujo de fondos esta vacia. Se devuelve 0")
            salida = 0
        return salida
    
    def vt(self,tasa,t = 0):
        """ Calculo de valor del flujo de fondos a un tiempo t
            Funciona calculando van y luego llevando a tiempo t correspondiente
            Inputs: 
                1 - tasa (posicional)
                2 - t momento de valuacion ( default = 0, named argument ). 
                    
        """
        return self.van(tasa)*(1.0+tasa)**t
    
    def tir_GS(self, a, b, n, tol):
        """ Calculo la TIR
        Inputs:
            1 - desde que porcentaje se puede encontarr la TIR 
            2 - hasta que porcentaje se puede encontrar la TIR
            3 - numero de particiiones entre a y b 
            4 - tolerancia decimal de la TIR (que diferencia decimal acepto)
        """
        punto_porcentual = (b-a)/n
        b -= (n-1)*punto_porcentual
        
        while self.van(a)>0 and self.van(b)>0:
            a += punto_porcentual
            b += punto_porcentual 
        
        if (b-a) < tol:
            salida =  (b+a)/2 
        
        else:
            salida = self.tir_GS(a, b, n, tol)
            
        return salida

    def tir_BI(self, a, b, tol):
        return self.tir_GS(a, b, 2, tol)
    
    def tir_AS(self, a, paso, tol=0.0001):
        b = a+paso
        
        if self.van(a)>0 and self.van(b)>0:
            salida = self.tir_GS(a, b, 10, tol)
        else:
            a += paso
            b += paso
            salida = self.tir_AS(a, b, paso)
        return salida


ff = FF((-80, 10, 10, 10, 10, 10, 10, 10, 10, 100))

print (f'La TIR GS es: {ff.tir_GS(0, 1, 10, 0.00001)}.')
print (f'La TIR BI es: {ff.tir_BI(0, 1, 0.00001)}.')
print (f'La TIR AS es: {ff.tir_AS(0, 0.1)}.')









