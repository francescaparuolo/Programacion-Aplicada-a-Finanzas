#%% INTRODUCCION A LAS CLASES. 

class a():
    x = 23
    
z = a() # 'z' es la instancia de la clase 
# Para entender un poco mejor sobre las clases y sus instancias, oensemos en la clase de programacion. 
# Yo, 'Francesca', soy una instancia de la clase. Mientras "Nico", por ejemplo, es otra instancia de la clase. 

print (z.x) # 'z.x' es la notacion utilizada para buscar el ATRIBUTO 'x' en 'z'. Notar que z es igual a a(). 
print ()

print (a.__dict__) # me escribe los atributos de 'a', que son parte de un diccionario 
print ()
print (z.__dict__)
print ()

print(a.__dict__['x']) # Le pido que dentro dentro del diccionario, me busque el atributo 'x'. 

#%% CLASES PADRES E HIJAS

class a():
    x = 23
class b(a):  # la clase B es hija de la clase A. 
    y = 30
    
z = b() # Fijarse que si entramos a la variable 'z', nos damos cuenta que incluye a ambas, 'x' y 'y'. 
        # Esto se debe a que la clase B esta incluida en la clase A. 
        
        
#%% Como usar el 'init' para agregar argumentos a una instancia de una clase. 

class a(): # Parent class
    x = 23
    
class b(a): # Child class
    y = 40
    def __init__(self, value): # El 'self' funciona para decirle a Python que el nuevo 'value' es parte del diccionario 'z'. 
        self.z = value # te das cuenta que es parte del diccionario 'z' pq se pone 'self.z'

w = b(value = 50) # Con esto se crea una nueva instancia dentro de la clase B. 
                  # Esta nueva instancia tiene como atributos 'x' e 'y' pq son parte de B y se esta definiento w = b().
                  # Y ADEMAS tiene un atributo nuevop llamado 'z', el cual es igual a 'value', cual es igual a 50. 

#%% DOCUMENTATION Y EJEMPLO FINANZAS PARA ENCONTRAR EL VA DE UN FLUJO DE FONDOS. 

# La documentacion de la clase son como los 'doc strings' de una funcion. 
# Se escriben debajo de l creacion de la clase y se busca como __doc__

def vactual (lista, i):
    if len(lista) == 1:
        return lista[0]
    else:
        x = lista[1] / (1+i)
        new_list = (lista[1:])
        return x + vactual(new_list,i)
    
    


#%% EJEMPLO PARA ENCONTRAR EL VA DE FLUJOS DE FONDOS 

# RESOUESTA CONJUNTA EN CLASE

class ff2():
    def __init__(self, flujos, tasa):
        self.flujos=flujos
        self.tasa=tasa
    def valor_actual(self):
        if len(self.flujos) == 1:
            return self.flujos[0]
        else:
            x = self.flujos[1] / (1+self.tasa)
            new_list = (self.flujos[1:])
            return x + valor_actual(self, new_list,self.tasa)
            
    


#%% FLUJO DE FONDOS QUE HIZO ECHI

class flujos_fondo():
    def __init__(self, flujos, tasa):
        self.flujos = flujos
        self.tasa = tasa
    def va (self, n=0):
        if n == len(self.flujos):
            salida = 0
        else:
            salida = self.flujos[n]+1/(1+self.tasa)*self.va(n+1)
        return salida 
    
valor_actual = flujos_fondo([100000, 100000, 90000, 80000], 0.5)
print(valor_actual.va())

b = 100000+100000/(1+0.5)+90000/(1+0.5)**2+80000/(1+0.5)**3

print()
print (b)

#%% FLUJO DE FONDOS, CODIGO QUE NOS MANDO GABI DE COMO HACERLO

class FF():
    """ Documentacion que va al __doc__ del objeto
        Poner aqui lo que se quiera explicar en un help.
        Por una cuestion de seguridad, vamos a usar tuplas 
        para garantizar la inmutabilidad del objeto
        """
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
    
#%%
if __name__=='__main__':
    
    a = FF((-80,10,10,10,10,10,10,10,10,100))    

    # dos formas de llamar al help    
    print((a.van).__doc__)
    help(a.vt)        
        
    # Busqueda de TIR...
    for x in range(1,20) : print(x, a.van(x/100.0))   
    
    # van a un valor proximo a la tir...
    print('\n',a.van(0.1330055))
    
    # Valor futuro en t a la tir. 
    # Notar que al no ser la tir exacta, 
    # a 25 periodos hacia el futuro, se aleja del 0.
    # Haria falta una funcion para computar la tir.... :) 
    print('\n', a.vt(0.1330055,25))
    
    
    #test caso FF vacio
    a = FF()
    print('\n',a.van(0.0))
















                  
                  