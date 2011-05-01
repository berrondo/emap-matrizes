import unittest
from matrices import Matriz

_2_x_2 = Matriz([[1, 2], 
                 [3, 4]])
                 
_3_x_3 = Matriz([['A', 'B', 'C'], 
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I']])
                
class TesteMatriz_2_x_2(unittest.TestCase):
    A = _2_x_2

    def teste_linhas(self):
        self.assertEqual(self.A.linhas, [[1, 2], [3, 4]])
        self.assertEqual(self.A.linha(0), [1, 2])
        self.assertEqual(self.A.linha(1), [3, 4])
        
    def teste_colunas(self):
        self.assertEqual(self.A.colunas, [[1, 3], [2, 4]])
        self.assertEqual(self.A.coluna(0), [1, 3])
        self.assertEqual(self.A.coluna(1), [2, 4])

    def teste_comparacao(self):
        B = self.A.transposta().transposta()
        self.assertEqual(self.A, B)
        
    def teste_transposta(self):
        AT = Matriz([[1, 3], 
                     [2, 4]])
        self.assertEqual(self.A.transposta(), AT)
        

class TesteMatriz_3_x_3(unittest.TestCase):
    A = _3_x_3
                
    def teste_colunas_da_matriz_3_x_3(self):
        self.assertEqual(self.A.colunas, [['A', 'D', 'G'], ['B', 'E', 'H'], ['C', 'F', 'I']])
        self.assertEqual(self.A.coluna(0), ['A', 'D', 'G'])
        self.assertEqual(self.A.coluna(1), ['B', 'E', 'H'])
        self.assertEqual(self.A.coluna(2), ['C', 'F', 'I'])
        
    def teste_transposta_da_matriz_3_x_3(self):
        AT = Matriz([['A', 'D', 'G'], 
                     ['B', 'E', 'H'], 
                     ['C', 'F', 'I']])
        self.assertEqual(self.A.transposta(), AT)
        
        
class TestePropriedades(unittest.TestCase):
    A = _2_x_2
    B = _3_x_3
    
    def teste_n(self):
        self.assertEqual(self.A.n, 2)
        self.assertEqual(self.B.n, 3)
        
    def teste_m(self):
        self.assertEqual(self.A.m, 2)
        self.assertEqual(self.B.m, 3)

    def teste_quadrada(self):
        self.assertTrue(self.A.quadrada)
        self.assertTrue(self.B.quadrada)
        
    def teste_simetria(self):
        AS = Matriz([[1, 2], 
                     [2, 1]])
        self.assertFalse(self.A.simetrica)
        self.assertTrue(AS.simetrica)
        
class TesteMultiplicacaoPorEscalar(unittest.TestCase):
    A = _2_x_2
    
    def teste_multiplicacao_por_escalar(self):
        _3xA = Matriz([[3, 6], 
                       [9, 12]])
        self.assertEqual(self.A.multiplicada_pelo_escalar(3), _3xA)
                            
unittest.main()