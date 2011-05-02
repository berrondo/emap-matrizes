#-*- coding: utf-8 -*-

import copy

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
        
        if self.m != other.m:
            raise
        
        produto = MatrizNula(self.n, other.m).linhas
        for i, linha in enumerate(self.linhas):
            for j, linha in enumerate(self.linhas):
                for k, linha in enumerate(other.linhas):
                    produto[i][j] = produto[i][j] + self.linhas[i][k] * other.linhas[k][j]
        return Matriz(produto)

    def __add__(self, other):
        if self.dimensao != other.dimensao:
            raise
            
        soma = MatrizNula(self.n, self.m)
        for i, linha in enumerate(soma.linhas):
            for j, elemento in enumerate(linha):
                soma.linhas[i][j] = self.linhas[i][j] + other.linhas[i][j]
        return soma 
            
    def __sub__(self, other):
        if self.dimensao != other.dimensao:
            raise
            
        diferenca = MatrizNula(self.n, self.m)
        for i, linha in enumerate(diferenca.linhas):
            for j, elemento in enumerate(linha):
                diferenca.linhas[i][j] = self.linhas[i][j] - other.linhas[i][j]
        return diferenca 
        
    @property
    def n(self): return len(self.linhas)
    
    @property
    def m(self): return len(self.linhas[0])
    
    @property
    def dimensao(self): return (self.n, self.m)
    
    @property
    def quadrada(self): return self.n == self.m
    
    def ordem(self):
        if not self.quadrada: raise TypeError
        return self.n
    
    def simetrica(self):
        if not self.quadrada: raise TypeError
        return self.linhas == self.transposta().linhas
        
    def diagonal_principal(self):
        if not self.quadrada:
            raise TypeError
            
        diagonal_principal = []
        for i, linha in enumerate(self.linhas):
            for j, elemento in enumerate(linha):
                if i == j: diagonal_principal.append(elemento)
        return diagonal_principal
         
    def diagonal_secundaria(self):
        if not self.quadrada:
            raise TypeError
        
        diagonal_secundaria = []
        for i, linha in enumerate(self.linhas):
            for j, elemento in enumerate(linha):
                if i + j == self.ordem() - 1: diagonal_secundaria.append(elemento)
        return diagonal_secundaria

    def linha(self, n): return self.linhas[n]
        
    @property
    def colunas(self):
        colunas = MatrizNula(self.m, self.n).linhas
        for i, linha in enumerate(self.linhas):
            for j, elemento in enumerate(linha):
                colunas[j][i] = elemento
        return colunas
        
    def coluna(self, n): return self.colunas[n]
        
    def transposta(self): return Matriz(self.colunas)
        
    def multiplicada_pelo_escalar(self, o_escalar):
        linhas_multiplicadas = copy.deepcopy(self.linhas)
        for i, linha in enumerate(self.linhas):
            for j, elemento in enumerate(linha):
                linhas_multiplicadas[i][j] = elemento * o_escalar
        return Matriz(linhas_multiplicadas)
        
        
class MatrizNula(Matriz):
    def __init__(self, n, m):
        linhas = [[] for i in range(n)]
        for linha in linhas:
            for i in range(m):
                linha.append(0)
        self.linhas = linhas
