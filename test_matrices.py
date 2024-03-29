import unittest
from matrices import Matriz, MatrizNula

_2_x_2 = Matriz([[1, 2], 
                 [3, 4]])
                 
SIMETRICA = Matriz([[1, 2], 
                    [2, 1]])
                    
_2_x_2_X_SIMETRICA = Matriz([[5,  4], 
                             [11, 10]])
                 
_3_x_3 = Matriz([['A', 'B', 'C'], 
                 ['D', 'E', 'F'],
                 ['G', 'H', 'I']])
                 
_2_x_3 = Matriz([['A', 'B', 'C'], 
                 ['D', 'E', 'F']])
                 
_2_x_2_NULA = Matriz([[0, 0],
                      [0, 0]])

_2_x_3_NULA = Matriz([[0, 0, 0],
                      [0, 0, 0]])

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
        self.assertEqual(self.A.colunas, [['A', 'D', 'G'], 
                                          ['B', 'E', 'H'], 
                                          ['C', 'F', 'I']])
        self.assertEqual(self.A.coluna(0), ['A', 'D', 'G'])
        self.assertEqual(self.A.coluna(1), ['B', 'E', 'H'])
        self.assertEqual(self.A.coluna(2), ['C', 'F', 'I'])
        
    def teste_colunas_da_matriz_2_x_3(self):
        self.assertEqual(_2_x_3_NULA.colunas, [[0, 0], [0, 0], [0, 0]])
        
    def teste_transposta_da_matriz_3_x_3(self):
        AT = Matriz([['A', 'D', 'G'], 
                     ['B', 'E', 'H'], 
                     ['C', 'F', 'I']])
        self.assertEqual(self.A.transposta(), AT)
    
    def teste_transposta_da_matriz_2_x_3(self):
        AT = Matriz([['A', 'D'], 
                     ['B', 'E'], 
                     ['C', 'F']])
        self.assertEqual(_2_x_3.transposta(), AT)

        
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
        self.assertFalse(_2_x_3_NULA.quadrada)
        
    def teste_simetria(self):
        self.AS = SIMETRICA
        self.assertFalse(self.A.simetrica())
        self.assertTrue(self.AS.simetrica())
        
    def teste_dimensoes(self):
        self.assertEqual(self.A.dimensao, SIMETRICA.dimensao)
        self.assertNotEqual(self.A.dimensao, self.B.dimensao)
        
    def teste_ordem(self):
        self.assertEqual(self.A.ordem(), 2)
        self.assertEqual(self.B.ordem(), 3)
        self.assertRaises(TypeError, _2_x_3_NULA.ordem)
        
        
class TesteOperacoes(unittest.TestCase):
    def teste_multiplicacao_por_escalar(self):
        self.assertEqual(Matriz([[1, 2], 
                                 [3, 4]]) * 3, Matriz([[3, 6 ], 
                                                       [9, 12]])
                         )
        
    def teste_soma(self):
        self.assertRaises(TypeError, _2_x_2.__add__, _3_x_3)
        self.assertEqual(_2_x_2 + _2_x_2_X_SIMETRICA, Matriz([[6, 6],
                                                              [14, 14]]))
        
    def teste_subtracao(self):
        self.assertRaises(TypeError, _2_x_2.__sub__, _3_x_3)
        self.assertEqual(_2_x_2 - _2_x_2_X_SIMETRICA, Matriz([[-4, -2],
                                                              [-8, -6]]))
        
    def teste_multiplicacao(self):
        self.assertRaises(TypeError, _2_x_2.__mul__, _3_x_3)
        self.assertEqual(_2_x_2 * SIMETRICA, _2_x_2_X_SIMETRICA)
        
    def teste_acesso_a_item(self):
        self.assertEqual(_2_x_2[0][0], 1)
        
    def teste_atribuicao_a_item(self):
        matriz = Matriz([[1, 2], 
                         [3, 4]])
        matriz[0][0] = 5
        self.assertEqual(matriz, Matriz([[5, 2], 
                                         [3, 4]]))
        
    def teste_diagonal_principal(self):
        self.assertRaises(TypeError, _2_x_3.diagonal_principal)
        self.assertEqual(_2_x_2.diagonal_principal(), [1, 4])
        
    def teste_diagonal_secundaria(self):
        self.assertRaises(TypeError, _2_x_3.diagonal_secundaria)
        self.assertEqual(_2_x_2.diagonal_secundaria(), [2, 3])

        
class TesteMatrizNula(unittest.TestCase):
    def test_criacao_matriz_nula(self):
        self.assertEqual(MatrizNula(2, 2), _2_x_2_NULA)
        self.assertEqual(MatrizNula(2, 3), _2_x_3_NULA)

unittest.main()