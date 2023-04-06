
class myarray():
    def __init__(self, elems, f, c, by_row=True):
        self.elems=elems
        self.f=f
        self.c=c
        self.by_row=by_row 
        
    def get_pos(self, j, k):
        '''Toma las coordenadas (j,k) y devuelve su posicion en la matriz'''
        largo_lista_elems = len(self.elems)
        if largo_lista_elems != (self.f*self.c):
            print('No ingreso una matriz valida.')
            pass
        else:
            return (j*self.c-(self.c-k))-1
        
    def get_coords(self, m):
        '''Toma una posición m en la lista y devuelve en forma de tupla las coordenadas j,k correspondientes en la matriz.'''
        j1 = 0
        count = 0
        while j1 < (m+1):
            j1 += self.c
            count += 1
        j = count
        k = self.c-(j1-(m+1))
        return (j,k) 
    
    def get_row(self, j):
        '''Funcion que devuelve el contenido de la fila j'''
        ultimo_num = j*self.c # ultimo elemento de la fila que se pide
        count = 0
        new_list = []
        while count < self.c:
            new_list.append(self.elems[ultimo_num-1])
            count += 1
            ultimo_num -= 1
        return list(reversed(new_list))
    
    def get_col(self, k):
        '''Funcion que devuelve el contenido de la columna k'''
        posicion_columna = k-1
        count = 0
        new_list = []
        while count < self.f:
            new_list.append(self.elems[posicion_columna])
            posicion_columna += self.c
            count += 1
        return new_list
    
    def get_elem(self, j, k):
        '''Funcion que devuelve el elemento (j,k) de la matriz respectivamente.'''
        posicion_m = (j*self.c-(self.c-k))-1
        return self.elems[posicion_m]
            
    def del_row(self, j):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la fila j'''
        ultimo_num = j*self.c
        count = 0
        new_list = self.elems.copy()
        while count < self.c:
            new_list.pop(self.elems[ultimo_num-2])
            count += 1
            ultimo_num -= 1
        return myarray(new_list, self.f-1, self.c, self.by_row)
    
    def del_col(self, k):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la columna k'''
        new_list = []
        for m in range(len(self.elems)+1):
            if self.get_coords(m)[1] != k:
                new_list.append(self.elems[m])
            else:
                pass
        return myarray(new_list, self.f, self.c-1, self.by_row)
    
    def swap_rows(self, j, k):
        '''Funcion que devuelve un objeto de la clase con las filas (j,k) intercambiadas.'''
        new_list = []
        for row in range(1, j):
            new_list.extend(self.get_row(row))
        new_list.extend(self.get_row(k))
        for row in range(j+1, k):
            new_list.extend(self.get_row(row))
        new_list.extend(self.get_row(j))
        for row in range(k+1, self.c+1):
            new_list.extend(self.get_row(row))
        return myarray(new_list, self.f, self.c, self.by_row)
    
    def swap_cols(self, l, m):
        '''Funcion que que devuelve un objeto de la clase con las filas (l,m) intercambiadas.'''
        f = 1
        new_list = self.elems.copy()
        for i in range(len(self.elems)):
            if self.get_coords(i)[1] == l:
                new_list[self.get_pos(f,l)], new_list[self.get_pos(f,m)] = new_list[self.get_pos(f,m)], new_list[self.get_pos(f,l)]
                f += 1
            else:
                pass
        return myarray(new_list, self.f, self.c, self.by_row)
    
    def scale_row(self, j, x):
        '''Funcion que devuelve un objeto de la clase con la fila j multiplicada por el factor x.'''
        new_list = []
        for i in range(len(self.elems)):
            if self.get_coords(i)[0] == j:
                new_list.append(x*self.elems[i])
            else:
                new_list.append(self.elems[i])
        return myarray(new_list, self.f, self.c, self.by_row)
    
    def scale_col(self, k, y):
        '''Funcion que que devuelve un objeto de la clase con la columna k multiplicada por el factor y.'''
        new_list = []
        for i in range(len(self.elems)):
            if self.get_coords(i)[1] == k:
                new_list.append(y*self.elems[i])
            else:
                new_list.append(self.elems[i])
        return myarray(new_list, self.f, self.c, self.by_row)
    
    def transpose(self):
        '''Funcion que devuelve un elemento de la clase pero con la matriz transpuesta'''
        new_list = []
        count = 0
        while count < self.c:
            new_list.extend(self.elems[count::self.c])
            count += 1
        return myarray(new_list, self.c, self.f, self.by_row)
    
    def flip_rows(self):
        '''Funcion que devuelve un objeto de la clase con el orden de las filas al reves.'''
        new_list = []
        for row in range(self.f, 0, -1):
            new_list.extend(self.get_row(row))
        return myarray(new_list, self.c, self.f, self.by_row)
    
    def flip_cols(self):
        '''Funcion que devuelve un objeto de la clase con el orden de las columnas al reves.'''
        matrix = self
        first_col = 1
        last_col = self.c
        count = 0
        if self.c % 2 == 0: # Es decir que el numero de columnas es par
            while count != self.c/2:
                matrix = matrix.swap_cols(first_col, last_col)
                first_col += 1
                last_col -= 1
                count += 1
            salida = matrix
        else:
            while count != self.c/2-0.5:
                matrix = matrix.swap_cols(first_col, last_col)
                first_col += 1
                last_col -= 1
                count += 1
            salida = matrix
        return salida
    
    def __add__(self, b):
        '''Funcion que efectua la suma de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for elemento in self.elems:
                elemento += b
                new_list.append(elemento)
            salida = new_list 
        elif (isinstance(b,type(self))):
            new_list = []
            count = 0
            for elemento in self.elems:
                elemento += b.elems[count]
                new_list.append(elemento)
                count += 1
            salida = myarray(new_list, self.f, self.c)
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida 

    def __radd__(self, b):
        '''Funcion que efectua la suma de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for elemento in self.elems:
                elemento += b
                new_list.append(elemento)
            salida = new_list 
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def __sub__(self, b):
        '''Funcion que efectua la resta de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for elemento in self.elems:
                elemento -= b
                new_list.append(elemento)
            salida = new_list 
        elif (isinstance(b,type(self))):
            new_list = []
            count = 0
            for elemento in self.elems:
                elemento -= b.elems[count]
                new_list.append(elemento)
                count += 1
            salida = myarray(new_list, self.f, self.c)
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida 

    def __rsub__(self, b):
        '''Funcion que efectua la resta de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for elemento in self.elems:
                elemento -= b
                new_list.append(elemento)
            salida = new_list 
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def __mul__(self, b):
        '''Funcion que efectua la multiplicacion de un objeto matriz por otro de su clase elemento a elemento o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for elemento in self.elems:
                elemento *= b
                new_list.append(elemento)
            salida = new_list 
        elif (isinstance(b,type(self))):
            new_list = []
            count = 0
            for elemento in self.elems:
                elemento *= b.elems[count]
                new_list.append(elemento)
                count += 1
            salida = myarray(new_list, self.f, self.c)
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida 
    
    def __rmul__(self, b):
        '''Funcion que efectua la multiplicacion de un objeto matriz por otro de su clase elemento a elemento o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for elemento in self.elems:
                elemento *= b
                new_list.append(elemento)
            salida = new_list 
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def __matmul__(self, b):
        '''Funcion que efectua la multiplicacion de matrices.'''
        if self.c != b.f:
            print ('Estas matrices no se pueden multiplicar.')
            salida = None
        else:
            new_list = []
            for row in range(1, self.f+1):
                fila = self.get_row(row)
                for col in range(1, b.c+1):
                    columna = b.get_col(col)
                    elemento = 0
                    for posicion in range(b.f):
                        elemento += fila[posicion] * columna[posicion]
                    new_list.append(elemento)
            salida = myarray(new_list, self.f, b.c)
        return salida
    
    def __pow__(self, b):
        '''Funcion que efectua la potencia entera de una matriz.'''
        if self.f != self.c:
            print ('No se puede hacer la potencia de esta matriz.')
            salida = None
        elif (isinstance(b, int)):
            count = 2
            matriz_multiplicada = self @ self
            while count < b:
                matriz_multiplicada @= self
                count += 1
            salida = matriz_multiplicada
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def identidad(self):
        '''Crea una matriz identidad NxN donde N es igual al numero de columnas de la matriz ingresada.'''
        identidad = []
        count = 0
        while count != self.c-1:
            identidad.extend([1]+[0]*self.c)
            count += 1
        identidad.extend([1])
        return myarray(identidad, self.c, self.c)
    
    def swap_rows_identidad(self,j,k):
        '''Funcion que devuelve un objeto de la clase con las filas (j,k) intercambiadas.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().swap_rows(j,k)
        return (identidad @ self)
    
    def swap_cols_identidad(self,l,m):
        '''Funcion que devuelve un objeto de la clase con las columnas (l,m) intercambiadas.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().swap_cols(l,m)
        return (self @ identidad)
            
    def del_row_identidad(self,j):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la fila j.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().del_row(j)
        return (identidad @ self)
        
    def del_col_identidad(self,k):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la columna k.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().del_col(k)
        return (self @ identidad)

elems = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = 3
c = 3
x = myarray(elems, f, c)

elems_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f_b = 3
c_b = 3
x_b = myarray(elems_b, f_b, c_b)

# Get Position 
print (f'La posicion del elemento en la lista es: {x.get_pos(3,2)}.')

# Get Coordenadas
print (f'Las coordenadas en la matriz de la posicion dada en la lista son: {x.get_coords(1)}.')

# Get Row
print (f'Los elementos de la fila dada son: {x.get_row(3)}.')

# Get Column 
print (f'Los elementos de la columna dada son: {x.get_col(1)}.')

# Get Element
print (f'El elemento es: {x.get_elem(1, 2)}.')

# Delete Row 
print (f'La matriz sin la fila es: {x.del_row(3).elems}.')

# Delete Column 
print (f'La matriz sin la columna es: {x.del_col(1).elems}.')

# Swap Rows
print (f'La matriz con las filas swapeadas es: {x.swap_rows(1,3).elems}.')

# Swap Columns
print (f'La matriz con las columnas swapeadas es: {x.swap_cols(1,3).elems}.')

# Scale Row
print (f'La matriz con la fila multiplicada es: {x.scale_row(1,2).elems}.')

# Scale Column
print (f'La matriz con la columna multiplicada es: {x.scale_col(1,2).elems}.')

# Transpose 
print (f'La matriz transpuesta es: {x.transpose().elems}.')

# Flip Rows 
print (f'La matriz con el orden de las filas invertido es: {x.flip_rows().elems}.')

# Flip Columns
print (f'La matriz con el orden de las columnas invertido es: {x.flip_cols().elems}.')

# OPERACIONES MATEMATICAS:
print ()
print ('OPERACIONES MATEMATICAS:')
print (f'x+x_b = {(x+x_b).elems}')
print (f'x-x_b = {(x-x_b).elems}')
print (f'x*x_b = {(x*x_b).elems}')
print (f'x@x_b = {(x@x_b).elems}')
print (f'x**4 = {(x**4).elems}')
print()

# SWAP Y DELETE MULTIPLICANDO MATRICES CON LA IDENTIDAD ALTERADA
print ('SWAP Y DELETE MULTIPLICANDO MATRICES CON LA IDENTIDAD ALTERADA:')
print(f'La matriz con las filas swapeadas es: {x.swap_rows_identidad(1, 2).elems}')
print(f'La matriz con las columnas swapeadas es: {x.swap_cols_identidad(1, 3).elems}')
print(f'La matriz sin la fila es: {x.del_row_identidad(1).elems}')
print(f'La matriz sin la columna es: {x.del_col_identidad(1).elems}')


#%%

class Myarray2():
    def __init__(self, elems, f, c, by_row=True):
        self.elems=elems
        self.f=f
        self.c=c
        self.by_row=by_row 
        
    def get_pos(self, j, k):
        '''Toma las coordenadas (j,k) y devuelve su posicion en la matriz'''
        return [j-1, k-1]
    
    def get_row(self, j):
        '''Funcion que devuelve el contenido de la fila j'''
        return self.elems[j-1]
    
    def get_col(self, k):
        '''Funcion que devuelve el contenido de la columna k'''
        columna = []
        for elemento in range(0,self.f):
            columna.append(self.elems[elemento][k-1])
        return columna
    
    def del_row(self, j):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la fila j'''
        new_list = [elem.copy() for elem in self.elems]
        new_list.pop(j-1)
        return Myarray2(new_list, self.f-1, self.c, self.by_row)
    
    def del_col(self, k):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la columna k'''
        index_col = k-1
        elems = self.elems.copy()
        new_list = []
        for lista in elems:
            fila = []
            for posicion in range(self.c):
                if posicion != index_col:
                    fila.append(lista[posicion])
            new_list.append(fila)
        return Myarray2(new_list, self.f, self.c-1, self.by_row)
    
    def swap_rows(self, j, k):
        '''Funcion que devuelve un objeto de la clase con las filas (j,k) intercambiadas.'''
        new_list = [elem.copy() for elem in self.elems]
        new_list[j-1], new_list[k-1] = new_list[k-1], new_list[j-1] 
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def swap_cols(self, l, m):
        '''Funcion que que devuelve un objeto de la clase con las filas (l,m) intercambiadas.'''
        new_list = [elem.copy() for elem in self.elems]
        for lista in new_list:
            lista[l-1], lista[m-1] = lista[m-1], lista[l-1]
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def scale_row(self, j, x):
        '''Funcion que devuelve un objeto de la clase con la fila j multiplicada por el factor x.'''
        new_list = [elem.copy() for elem in self.elems]
        fila_multiplicada = []
        for elemento in new_list[j-1]:
            fila_multiplicada.append(elemento*x)
        new_list[j-1] = fila_multiplicada
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def scale_col(self, k, y):
        '''Funcion que que devuelve un objeto de la clase con la columna k multiplicada por el factor y.'''
        new_list = [elem.copy() for elem in self.elems]
        for lista in new_list:
            lista[k-1] = lista[k-1]*y
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def transpose(self):
        '''Funcion que devuelve un elemento de la clase pero con la matriz transpuesta'''
        new_list = []
        columna = 0
        while columna < self.c:
            mini_list = []
            for lista in self.elems:
                mini_list.append(lista[columna])
            new_list.append(mini_list)
            columna += 1
        return new_list
    
    def flip_rows(self):
        '''Funcion que devuelve un objeto de la clase con el orden de las filas al reves.'''
        new_list = [elem.copy() for elem in self.elems]
        return list(reversed(new_list))
    
    def flip_cols(self): 
        '''Funcion que devuelve un objeto de la clase con el orden de las columnas al reves.'''
        new_list = [elem.copy() for elem in self.elems]
        first_col = 0
        last_col = self.c-1
        count = 0
        while count != self.c/2 and count != self.c/2-0.5:
            for lista in new_list:
                lista[first_col], lista[last_col] = lista[last_col], lista[first_col] 
            first_col += 1
            last_col -= 1
            count += 1
        return new_list
    
    def __add__(self, b):
        '''Funcion que efectua la suma de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for lista in self.elems:
                mini_list = []
                for elemento in lista:
                    elemento += b
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = new_list
        elif (isinstance(b,type(self))):
            new_elems = []
            for fila in range(self.f):
                row = []
                for col in range(self.c):
                    row.append(self.elems[fila][col] + b.elems[fila][col])
                new_elems.append(row)
            salida = Myarray2(new_elems, self.f, self.c)
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida

    def __radd__(self, b):
        '''Funcion que efectua la suma de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for lista in self.elems:
                mini_list = []
                for elemento in lista:
                    elemento += b
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = new_list
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def __sub__(self, b):
        '''Funcion que efectua la resta de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for lista in self.elems:
                mini_list = []
                for elemento in lista:
                    elemento -= b
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = new_list
        elif (isinstance(b,type(self))):
            new_elems = []
            for fila in range(self.f):
                row = []
                for col in range(self.c):
                    row.append(self.elems[fila][col] - b.elems[fila][col])
                new_elems.append(row)
            salida = Myarray2(new_elems, self.f, self.c)
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida

    def __rsub__(self, b):
        '''Funcion que efectua la resta de un objeto matriz por otro de su clase o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for lista in self.elems:
                mini_list = []
                for elemento in lista:
                    elemento -= b
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = new_list
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def __mul__(self, b):
        '''Funcion que efectua la multiplicacion de un objeto matriz por otro de su clase elemento a elemento o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for lista in self.elems:
                mini_list = []
                for elemento in lista:
                    elemento *= b
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = new_list
        elif (isinstance(b,type(self))):
            new_elems = []
            for fila in range(self.f):
                row = []
                for col in range(self.c):
                    row.append(self.elems[fila][col] * b.elems[fila][col])
                new_elems.append(row)
            salida = Myarray2(new_elems, self.f, self.c)
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida

    def __rmul__(self, b):
        '''Funcion que efectua la multiplicacion de un objeto matriz por otro de su clase elemento a elemento o por un escalar'''
        if (isinstance(b, int)):
            new_list = []
            for lista in self.elems:
                mini_list = []
                for elemento in lista:
                    elemento *= b
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = new_list
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def __matmul__(self, b):
        if self.c != b.f:
            print ('Estas matrices no se pueden multiplicar.')
            salida = None
        else:
            new_list = []
            for fila in range(self.f):
                mini_list = []
                for col in range(b.c):
                    elemento = 0
                    for posicion in range(b.f):
                        elemento += self.elems[fila][posicion] * b.elems[posicion][col]
                    mini_list.append(elemento)
                new_list.append(mini_list)
            salida = Myarray2(new_list, self.f, self.c)
        return salida
    
    def __pow__(self, b):
        '''Funcion que efectua la potencia entera de una matriz.'''
        if self.f != self.c:
            print ('No se puede hacer la potencia de esta matriz.')
            salida = None
        elif (isinstance(b, int)):
            count = 2
            matriz_multiplicada = self @ self
            while count < b:
                matriz_multiplicada @= self
                count += 1
            salida = matriz_multiplicada
        else:
            print ('El parametro de entrada es de tipo ', str(type(b)))
            salida = None
        return salida
    
    def identidad(self):
        '''Crea una matriz identidad NxN donde N es igual al numero de columnas de la matriz ingresada.'''
        identidad = []
        for fila in range (self.f):
            mini_list = [0]*self.c
            for col in range (self.c):
                if fila == col:
                    mini_list[col] = 1
            identidad.append(mini_list)
        return Myarray2(identidad, self.c, self.c)
        
    def swap_rows_identidad(self,j,k):
        '''Funcion que devuelve un objeto de la clase con las filas (j,k) intercambiadas.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().swap_rows(j,k)
        return (identidad @ self)
    
    def swap_cols_identidad(self,l,m):
        '''Funcion que devuelve un objeto de la clase con las columnas (l,m) intercambiadas.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().swap_cols(l,m)
        return (self @ identidad)
            
    def del_row_identidad(self,j):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la fila j.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().del_row(j)
        return (identidad @ self)
        
    def del_col_identidad(self,k):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la columna k.
            Para hacer esto, la funcion multiplica la matriz por una matriz identidad alterada.'''
        matrix = self
        identidad = matrix.identidad().del_col(k)
        return (self @ identidad)
                        
        
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
f2 = 4
c2 = 4
y = Myarray2(matriz, f2, c2)

matriz_b = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
f2_b = 4
c2_b = 4
y_b = Myarray2(matriz_b, f2_b, c2_b)

# Get Position 
print (f'La posicion del elemento en la lista es: {y.get_pos(3,2)}.')

# Get Row
print (f'Los elementos de la fila dada son: {y.get_row(3)}.')

# Get Column 
print (f'Los elementos de la columna dada son: {y.get_col(2)}.')

# Get Element
print (f'El elemento es: {x.get_elem(3, 2)}.')

# Delete Row
print (f'La matriz sin la fila es: {y.del_row(3).elems}.')

# Delete Column 
print (f'La matriz sin la columna es: {y.del_col(1).elems}.')

# Swap Rows
print(f'La matriz con las filas swapeadas es: {y.swap_rows(1,3).elems}.')

# Swap Columns 
print(f'La matriz con las columnas swapeadas es: {y.swap_cols(1,3).elems}.')
    
# Scale Row
print(f'La matriz con la fila multiplicada es: {y.scale_row(1,4).elems}')

# Scale Column 
print(f'La matriz con la columna multiplicada es: {y.scale_col(1, 10).elems}')  

# Transpose
print (f'La matriz transpuesta es: {y.transpose()}')

# Flip rows
print (f'La matriz con el orden de las filas invertido es: {y.flip_rows()}')

# Flip columns
print (f'La matriz con el orden de las columnas invertido es: {y.flip_cols()}')

# OPERACIONES MATEMATICAS: 
print ()
print ('OPERACIONES MATEMATICAS:')
print (f'y+y_b = {(y+y_b).elems}')
print (f'y-y_b = {(y-y_b).elems}')
print (f'y*y_b = {(y*y_b).elems}')
print (f'y@y_b = {(y@y_b).elems}')
print (f'y**3 = {(y**3).elems}')
print ()

# SWAP Y DELETE MULTIPLICANDO MATRICES CON LA IDENTIDAD ALTERADA
print ('SWAP Y DELETE MULTIPLICANDO MATRICES CON LA IDENTIDAD ALTERADA:')
print(f'La matriz con las filas swapeadas es: {y.swap_rows_identidad(1, 2).elems}')
print(f'La matriz con las columnas swapeadas es: {y.swap_cols_identidad(1, 3).elems}')
print(f'La matriz sin la fila es: {y.del_row_identidad(1).elems}')
print(f'La matriz sin la columna es: {y.del_col_identidad(1).elems}')

















