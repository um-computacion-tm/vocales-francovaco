import unittest
def contar_vocales(palabra):
    resultado = {}
    for letra in palabra:
        if letra in 'aeiouáéíóúAEIOUÁÉÍÓÚ':
            if letra in resultado:
                resultado[letra] += 1
            else:
                resultado[letra] = 1
    return resultado

class TestContarVocales(unittest.TestCase):
    def test_ninguna(self):
        self.assertEqual(contar_vocales("zzz"), {})
    def test_contar_a(self):
        self.assertEqual(contar_vocales("cas"), {'a': 1})
    def test_contar_dos_a(self):
        self.assertEqual(contar_vocales("casa"), {'a': 2})
    def test_contar_beso(self):
        self.assertEqual(contar_vocales("beso"), {'e': 1, 'o': 1})
    def test_contar_bese(self):
        self.assertEqual(contar_vocales("bese"), {'e': 2})
    def test_contar_todas(self):
        self.assertEqual(contar_vocales("murcielago"), {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})
    def test_contar_casanova(self):
        self.assertEqual(contar_vocales("casanova"), {'a': 3, 'o': 1})
    def test_mayusculas_casa(self):
        self.assertEqual(contar_vocales("CASA"), {'A': 2})
    def test_mayusculas_casanova(self):
        self.assertEqual(contar_vocales("CASANOVA"), {'A': 3, 'O': 1})
    def test_mayusculas_murcielgo(self):
        self.assertEqual(contar_vocales("MURCIELAGO"), {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1})
    def test_tilde(self):
        self.assertEqual(contar_vocales("áéíóú"), {'á': 1, 'é': 1, 'í': 1, 'ó': 1, 'ú': 1})
    def test_tilde_mayusculas(self):
        self.assertEqual(contar_vocales("ÁÉÍÓÚ"), {'Á': 1, 'É': 1, 'Í': 1, 'Ó': 1, 'Ú': 1})
    def test_tilde_mayusculas_minusculas(self):
        self.assertEqual(contar_vocales("áÉíÓú"), {'á': 1, 'É': 1, 'í': 1, 'Ó': 1, 'ú': 1})
    def test_tilde_murcielago(self):
        self.assertEqual(contar_vocales("murciélago"), {'a': 1, 'é': 1, 'i': 1, 'o': 1, 'u': 1})
                         

unittest.main()

