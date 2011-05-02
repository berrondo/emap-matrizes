#-*- coding: utf-8 -*-

from types import IntType

class Matriz(object):
    def __init__(self, linhas):
        self.linhas = linhas
        
    def __repr__(self):
        '''
            [
                1,  2
                1,  2
            ]
        '''
        return str(self.linhas)
        
    def __cmp__(self, other):
        if self.linhas == other.linhas: return 0
        else: return 1
        
    def __mul__(self, other):
        ''' para i := 1 a n faça
            para j := 1 a n faça
            para k := 1 a m faça
            c[i][j] := C[i][j] + A[i][k] * B[k][j]
         '''
        
        if type(other) is IntType:
            return self.vezes(other)
        
        if self.m != other.m:
            raise
        
        produto = MatrizNula(self.n, other.m)
        for i, linha in enumerate(self):
            for j, linha in enumerate(self):
                for k, linha in enumerate(other):
                    produto[i][j] = produto[i][j] + self[i][k] * other[k][j]
        return produto

    def __add__(self, other):
        if self.dimensao != other.dimensao:
            raise
            
        soma = MatrizNula(self.n, self.m)
        for i, linha in enumerate(soma):
            for j, elemento in enumerate(linha):
                soma[i][j] = self[i][j] + other[i][j]
        return soma 
            
    def __sub__(self, other):
        if self.dimensao != other.dimensao:
            raise
            
        diferenca = MatrizNula(self.n, self.m)
        for i, linha in enumerate(diferenca):
            for j, elemento in enumerate(linha):
                diferenca[i][j] = self[i][j] - other[i][j]
        return diferenca
        
    def __getitem__(self, item):
        return self.linhas[item]
        
    def __iter__(self):
        return iter(self.linhas)
        
    @property
    def n(self): return len(self.linhas)
    
    @property
    def m(self): return len(self.linhas[0])
    
    @property
    def dimensao(self): return (self.n, self.m)
    
    @property
    def quadrada(self): return self.n == self.m
    
    def ordem(self):
        if not self.quadrada:
            raise TypeError
        return self.n
    
    def simetrica(self):
        if not self.quadrada:
            raise TypeError
        return self == self.transposta()
        
    def diagonal_principal(self):
        if not self.quadrada:
            raise TypeError
            
        diagonal_principal = []
        for i, linha in enumerate(self):
            for j, elemento in enumerate(linha):
                if i == j: diagonal_principal.append(elemento)
        return diagonal_principal
         
    def diagonal_secundaria(self):
        if not self.quadrada:
            raise TypeError
        
        secundaria = []
        for i, linha in enumerate(self):
            for j, elemento in enumerate(linha):
                if i+j == self.ordem()-1: secundaria.append(elemento)
        return secundaria

    def linha(self, n): return self.linhas[n]
        
    @property
    def colunas(self):
        return self.transposta().linhas
        
    def coluna(self, m): return self.colunas[m]
        
    def transposta(self):
        transposta = MatrizNula(self.m, self.n)
        for i, linha in enumerate(self):
            for j, elemento in enumerate(linha):
                transposta[j][i] = elemento
        return transposta
        
    def vezes(self, escalar):
        produto_escalar = MatrizNula(self.n, self.n)
        for i, linha in enumerate(self):
            for j, elemento in enumerate(linha):
                produto_escalar[i][j] = elemento * escalar
        return produto_escalar
        
        
class MatrizNula(Matriz):
    def __init__(self, n, m):
        linhas = [[] for i in range(n)]
        for linha in linhas:
            for i in range(m):
                linha.append(0)
        self.linhas = linhas
