import unittest
from matrices import Matriz

class TesteMatriz_2_x_2(unittest.TestCase):
    A = Matriz([[1, 1], 
                [2, 2]])
                    
    def teste_linhas(self):
        self.assertEqual(self.A.linhas, [[1, 1], [2, 2]])
        self.assertEqual(self.A.linha(0), [1, 1])
        self.assertEqual(self.A.linha(1), [2, 2])
        
    def teste_colunas(self):
        self.assertEqual(self.A.colunas, [[1, 2], [1, 2]])
        self.assertEqual(self.A.coluna(0), [1, 2])
        self.assertEqual(self.A.coluna(1), [1, 2])
        
    def teste_colunas_da_matriz_3_x_3(self):
        A = Matriz([['A', 'B', 'C'], 
                    ['D', 'E', 'F'],
                    ['G', 'H', 'I']])
        self.assertEqual(A.colunas, [['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I']])
        self.assertEqual(A.coluna(0), ['A', 'D', 'G'])
        self.assertEqual(A.coluna(1), ['B', 'E', 'H'])
        self.assertEqual(A.coluna(2), ['C', 'F', 'I'])
        
    def teste_transposta_da_matriz_3_x_3(self):
        A = Matriz([['A', 'B', 'C'], 
                    ['D', 'E', 'F'],
                    ['G', 'H', 'I']])
        AT = Matriz([['A', 'D', 'G'], 
                     ['B', 'E', 'H'], 
                     ['C', 'F', 'I']])
        self.assertEqual(A.transposta(), AT)
        
    def teste_comparacao(self):
        B = self.A.transposta().transposta()
        self.assertEqual(self.A, B)
        
    def teste_transposta(self):
        AT = Matriz([[1, 2], 
                     [1, 2]])
        self.assertEqual(self.A.transposta(), AT)

                    
        
unittest.main()