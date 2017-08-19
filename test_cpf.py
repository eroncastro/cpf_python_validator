import unittest
from cpf import Cpf


class TestCpfValidator(unittest.TestCase):
    def test_cpf_with_the_same_digits_is_invalid(self):
        self.assertFalse(Cpf('11111111111').valid())

    def test_cpf_with_non_numerical_digits_is_invalid(self):
        self.assertFalse(Cpf('1111111111a').valid())

    def test_valid_cpf(self):
        self.assertTrue(Cpf('36768801619').valid())
