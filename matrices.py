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
        if self.m != other.m:
            raise
            
    def __add__(self, other):
        if self.dimensao != other.dimensao:
            raise
            
    def __sub__(self, other):
        if self.dimensao != other.dimensao:
            raise
        
    @property
    def n(self): return len(self.linhas)
    
    @property
    def m(self): return len(self.colunas)
    
    @property
    def dimensao(self): return (self.n, self.m)
    
    @property
    def quadrada(self): return self.n == self.m
    
    @property
    def simetrica(self): return self.linhas == self.transposta().linhas
        
    def linha(self, n):
        return self.linhas[n]
        
    @property
    def colunas(self):
        colunas = copy.deepcopy(self.linhas)
        for i, linha in enumerate(self.linhas):
            for j, elemento in enumerate(linha):
                colunas[j][i] = elemento
        return colunas
        
    def coluna(self, n):
        return self.colunas[n]
        
    def transposta(self):
        return Matriz(self.colunas)
        
    def multiplicada_pelo_escalar(self, o_escalar):
        linhas_multiplicadas = copy.deepcopy(self.linhas)
        for i, linha in enumerate(self.linhas):
            for j, elemento in enumerate(linha):
                linhas_multiplicadas[i][j] = elemento * o_escalar
        return Matriz(linhas_multiplicadas)