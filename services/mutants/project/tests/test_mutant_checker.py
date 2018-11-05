from project import create_app
from project.tests.base import BaseTestCase
from project.api.mutant_checker import MutantChecker

app = create_app()


class TestMutantChecker(BaseTestCase):
    def test_valid_mutant_dna(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna))

    def test_valid_mutant_dna_double_vertical(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna_double_vertical))

    def test_valid_mutant_dna_double_horizontal(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna_double_horizontal))

    def test_valid_mutant_dna_double_diagonal(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna_double_diagonal))

    def test_valid_mutant_dna_horizontal_diagonal(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna_horizontal_diagonal))

    def test_valid_mutant_dna_horizontal_vertical(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna_horizontal_vertical))

    def test_valid_mutant_dna_vertical_diagonal(self):
        '''Ensures the MutantChecker algorithm returns true when a valid mutant
        dna is checked.'''

        checker = MutantChecker()
        self.assertTrue(checker.isMutant(self.valid_mutant_dna_vertical_diagonal))

    def test_valid_human_dna(self):
        '''Ensures the MutantChecker algorithm returns false when a valid human
        (not mutant) dna is checked'''

        checker = MutantChecker()
        self.assertFalse(checker.isMutant(self.valid_human_dna))

    def test_invalid_chars_dna(self):
        '''Ensures the MutantChecker algorithm raises an exception when invalid
        chars are used in the DNA matrix.'''

        checker = MutantChecker()
        self.assertRaises(ValueError, checker.isMutant, self.invalid_chars_dna)

    def test_invalid_size_dna_matrix(self):
        '''Ensures the MutantChecker algorithm raises an exception when the matrix is
        not square.'''

        checker = MutantChecker()
        self.assertRaises(ValueError, checker.isMutant, self.invalid_size_dna)

    def test_invalid_mutant_dna_one_match_only_horizontal(self):
        '''Ensures the MutantChecker algorithm returns false when a DNA containing only one mutant chain is checked.'''

        checker = MutantChecker()
        self.assertFalse(checker.isMutant(self.invalid_mutant_dna_single_horizontal))

    def test_check_invalid_mutant_one_match_only_vertical(self):
        '''Ensures the MutantChecker algorithm returns false when a DNA containing only one mutant chain is checked.'''

        checker = MutantChecker()
        self.assertFalse(checker.isMutant(self.invalid_mutant_dna_single_vertical))

    def test_check_invalid_mutant_one_match_only_diagonal(self):
        '''Ensures the MutantChecker algorithm returns false when a DNA containing only one mutant chain is checked.'''

        checker = MutantChecker()
        self.assertFalse(checker.isMutant(self.invalid_mutant_dna_single_diagonal))
