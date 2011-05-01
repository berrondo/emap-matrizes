import copy

class Matriz(object):
    def __init__(self, linhas):
        self.linhas = linhas
        
    def __repr__(self):
        return '''
            [
                1,  2
                1,  2
            ]
        '''
        
    def __cmp__(self, other):
        if self.__repr__() == other.__repr__(): return 0
        else: return 1
        
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
        