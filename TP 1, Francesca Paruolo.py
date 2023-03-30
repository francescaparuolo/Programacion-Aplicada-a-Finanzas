
class myarray():
    def __init__(self, elems, f, c, by_row=True):
        self.elems=elems
        self.f=f
        self.c=c
        self.by_row=by_row 
        
    def get_pos(self, j, k):
        largo_lista_elems = len(self.elems)
        if largo_lista_elems != (self.f*self.c):
            print('No ingreso una matriz valida.')
            pass
        else:
            return (j*self.c-(self.c-k))-1
        
    def get_coords(self, m):
        j1 = 0
        count = 0
        while j1 < (m+1):
            j1 += self.c
            count += 1
        j = count
        k = self.c-(j1-(m+1))
        return (j,k)
    
    def get_row(self, j):
        ultimo_num = j*self.c # ultimo elemento de la fila que se pide
        count = 0
        new_list = []
        while count < self.c:
            new_list.append(self.elems[ultimo_num-1])
            count += 1
            ultimo_num -= 1
        return list(reversed(new_list))
    
    def get_col(self, k):
        posicion_columna = k-1
        count = 0
        new_list = []
        while count < self.f:
            new_list.append(self.elems[posicion_columna])
            posicion_columna += self.c
            count += 1
        return new_list
    
    def get_elem(self, j, k):
        posicion_m = (j*self.c-(self.c-k))-1
        return self.elems[posicion_m]
            
    def del_row(self, j):
        ultimo_num = j*self.c
        count = 0
        new_list = self.elems.copy()
        while count < self.c:
            new_list.pop(self.elems[ultimo_num-2])
            count += 1
            ultimo_num -= 1
        return myarray(new_list, self.f-1, self.c, self.by_row)
    
    def del_col(self, k):
        new_list = []
        for m in range(len(self.elems)+1):
            if self.get_coords(m)[1] != k:
                new_list.append(self.elems[m])
            else:
                pass
        return myarray(new_list, self.f, self.c-1, self.by_row)
    
    def swap_rows(self, j, k):
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
        new_list = []
        for i in range(len(self.elems)):
            if self.get_coords(i)[0] == j:
                new_list.append(x*self.elems[i])
            else:
                new_list.append(self.elems[i])
        return myarray(new_list, self.f, self.c, self.by_row)
    
    def scale_col(self, k, y):
        new_list = []
        for i in range(len(self.elems)):
            if self.get_coords(i)[1] == k:
                new_list.append(y*self.elems[i])
            else:
                new_list.append(self.elems[i])
        return myarray(new_list, self.f, self.c, self.by_row)
    
    def transpose(self):
        new_list = []
        count = 0
        while count < self.c:
            new_list.extend(self.elems[count::self.c])
            count += 1
        return myarray(new_list, self.c, self.f, self.by_row)
    
    def flip_rows(self):
        new_list = []
        for row in range(self.f, 0, -1):
            new_list.extend(self.get_row(row))
        return myarray(new_list, self.c, self.f, self.by_row)
    
    # def flip_cols(self):
    #     new_list = self.elems.copy()
    #     first_col = 0
    #     last_col = self.c-1
    #     count = 0
    #     if self.c % 2 == 0: # Es decir que el numero de columnas es par
    #         while count != self.c/2:
    #             self.swap_cols(first_col, last_col)
    #             first_col += 1
    #             last_col -= 1
    #             count += 1
    #     return new_list
            
        
elems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
f = 4
c = 3
x = myarray(elems, f, c)

# Get Position 
pos = x.get_pos(4,2)
print (f'La posicion del elemento en la lista es: {pos}.')

# Get Coordenadas
coords = x.get_coords(10)
print (f'Las coordenadas en la matriz de la posicion dada en la lista son: {coords}.')

# Get Row
row = x.get_row(4)
print (f'Los elementos de la fila dada son: {row}.')

# Get Column 
col = x.get_col(1)
print (f'Los elementos de la columna dada son: {col}.')

# Get Element
element = x.get_elem(4, 2)
print (f'El elemento es: {element}.')

# Delete Row 
matriz_with_del_row = x.del_row(4).elems
print (f'La nueva matriz es: {matriz_with_del_row}.')

# Delete Column 
matriz_with_del_col = x.del_col(1).elems
print (f'La nueva matriz es: {matriz_with_del_col}.')

# Swap Rows
swap_rows = x.swap_rows(1,4).elems
print (f'La nueva matriz es: {swap_rows}.')

# Swap Columns
swap_cols = x.swap_cols(1,3).elems
print (f'La nueva matriz es: {swap_cols}.')

# Scale Row
scale_row = x.scale_row(1,2).elems
print (f'La nueva matriz es: {scale_row}.')

# Scale Column
scale_col = x.scale_col(1,2).elems
print (f'La nueva matriz es: {scale_col}.')

# Transpose 
transpose = x.transpose().elems
print (f'La nueva matriz es: {transpose}.')

# Flip Rows 
flipped_rows = x.flip_rows().elems
print (f'La nueva matriz es: {flipped_rows}.')

# Flip Columns
flipped_cols = x.flip_cols()
print (f'La nueva matriz es: {flipped_cols}.')


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
        for elemento in range(0,self.c):
            columna.append(self.elems[elemento][0])
        return columna
    
    def del_row(self, j):
        '''Funcion que devuelvan un objeto de la clase habiendo eliminando la fila j'''
        new_list = self.elems.copy()
        new_list.pop(j-1)
        return Myarray2(new_list, self.f-1, self.c, self.by_row)
    
    def del_col(self, k):
        index_col = k-1
        elems = self.elems.copy()
        new_list = []
        for lista in elems:
            fila = []
            for posicion in range(self.c):
                if posicion != index_col:
                    print(lista[posicion])
                    fila.append(lista[posicion])
            new_list.append(fila)
        return Myarray2(new_list, self.f, self.c-1, self.by_row)
    
    def swap_rows(self, j, k):
        '''Funcion que que devuelve un objeto de la clase con las filas (j,k) intercambiadas.'''
        new_list = self.elems.copy()
        new_list[j-1], new_list[k-1] = new_list[k-1], new_list[j-1] 
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def swap_cols(self, l, m):
        '''Funcion que que devuelve un objeto de la clase con las filas (l,m) intercambiadas.'''
        new_list = self.elems.copy()
        for lista in new_list:
            lista[l-1], lista[m-1] = lista[m-1], lista[l-1]
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def scale_row(self, j, x):
        '''Funcion que que devuelve un objeto de la clase con la fila j multiplicada por el factor x.'''
        new_list = self.elems.copy()
        fila_multiplicada = []
        for elemento in new_list[j-1]:
            fila_multiplicada.append(elemento*x)
        new_list[j-1] = fila_multiplicada
        return Myarray2(new_list, self.f, self.c, self.by_row)
    
    def scale_col(self, k, y):
        '''Funcion que que devuelve un objeto de la clase con la columna k multiplicada por el factor y.'''
        new_list = self.elems.copy()
        for lista in new_list:
            lista[k-1] = lista[k-1]*y
        return Myarray2(new_list, self.f, self.c, self.by_row)

        
matriz = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
f2 = 4
c2 = 3
y = Myarray2(matriz, f2, c2)

# Get Position 
pos = y.get_pos(4,2)
print (f'La posicion del elemento en la lista es: {pos}.')


# Get Row
row = y.get_row(4)
print (f'Los elementos de la fila dada son: {row}.')

# Get Column 
col = y.get_col(1)
print (f'Los elementos de la columna dada son: {col}.')

# Get Element
element = x.get_elem(4, 2)
print (f'El elemento es: {element}.')

# Delete Row 
matriz_with_del_row = y.del_row(4).elems
print (f'La nueva matriz es: {matriz_with_del_row}.')

# Delete Column 
matriz_with_del_col = y.del_col(1).elems
print (f'La nueva matriz es: {matriz_with_del_col}.')

# Swap Rows
swap_row = y.swap_rows(1,4).elems
print(f'La nueva matriz es: {swap_row}.')

# Swap Columns 
swap_cols = y.swap_cols(1,3).elems
print(f'La nueva matriz es: {swap_cols}.')
    
# Scale Row
print(y.scale_row(1,4).elems)

# Scale Column 
print(y.scale_col(1, 10).elems)








































