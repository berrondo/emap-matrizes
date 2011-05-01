

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
        
    def colunas(self):
        coluna0 = [self.linhas[0][0], self.linhas[1][0]]
        coluna1 = [self.linhas[0][1], self.linhas[1][1]]
        colunas = [coluna0, coluna1]
        return colunas
        
    def coluna(self, n):
        return self.colunas()[n]
        
    def transposta(self):
        return Matriz(self.colunas())
        