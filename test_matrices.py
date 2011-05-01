import unittest
from matrices import Matriz

class TesteMatriz(unittest.TestCase):
    def teste_criacao(self):
        matriz = Matriz([[1, 1], [2, 2]])
        self.assertTrue(matriz)
        
    def teste_linhas(self):
        matriz = Matriz([[1, 1], [2, 2]])
        self.assertEqual(matriz.linha(0), [1, 1])
        self.assertEqual(matriz.linha(1), [2, 2])
        
unittest.main()