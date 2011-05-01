import unittest
from matrices import Matriz

class TesteMatriz(unittest.TestCase):
    def teste_linhas(self):
        A = Matriz([[1, 1], 
                    [2, 2]])
        self.assertEqual(A.linhas, [[1, 1], [2, 2]])
        self.assertEqual(A.linha(0), [1, 1])
        self.assertEqual(A.linha(1), [2, 2])
        
    def teste_colunas(self):
        A = Matriz([[1, 1], 
                    [2, 2]])
        self.assertEqual(A.colunas(), [[1, 2], [1, 2]])
        self.assertEqual(A.coluna(0), [1, 2])
        self.assertEqual(A.coluna(1), [1, 2])
        
    def teste_comparacao(self):
        A = Matriz([[1, 1], 
                    [2, 2]])
        B = A.transposta().transposta()
        self.assertEqual(A, B)
        
    def teste_transposta(self):
        A = Matriz([[1, 1], 
                    [2, 2]])
        AT = Matriz([[1, 2], 
                     [1, 2]])
        self.assertEqual(A.transposta(), AT)

                    
        
unittest.main()