from flask_testing import TestCase
from project import create_app

app = create_app()


class BaseTestCase(TestCase):

    # valid mutants dnas
    valid_mutant_dna = ["ATGCGA", "CTGAGC", "TTAAGT", "ATAAGG", "CCCTTA", "TCACTG"]
    valid_mutant_dna_double_vertical = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    valid_mutant_dna_double_horizontal = ["ATGCGA", "CAGTGC", "TTATTT", "AGGGGG", "CCCCTA", "TCACTG"]
    valid_mutant_dna_double_diagonal = ["ATGCGA", "CATTGC", "TTATTT", "AGGATG", "CCCGTA", "TCACTG"]
    valid_mutant_dna_horizontal_vertical = ["ATGCGA", "CAGTGC", "TTATGT", "AGAGGG", "CCCCTA", "TCACTG"]
    valid_mutant_dna_horizontal_diagonal = ["ATGCGA", "CAGAGC", "TTAAGT", "AGAAAG", "CCCCTA", "TCACTG"]
    valid_mutant_dna_vertical_diagonal = ["ATGCGA", "AAGAGC", "ATAAGT", "AGAAAG", "CCCGTA", "TCACTG"]

    # valid human dna
    valid_human_dna = ["ATGCGA", "CAGTGC", "TTTAGT", "AGAAGG", "CCCGTA", "TCACTG"]

    # invalid dnas
    invalid_chars_dna = ["ATGCGA", "CFFTGC", "TTTTGT", "AGAAGG", "CCCGTA", "TCACTG"]
    invalid_size_dna = ["ATGCGAA", "CAGAGC", "TTAAGT", "AGAAGG", "CCCATA", "TCACTG"]
    invalid_mutant_dna_single_horizontal = ["ATGCGA", "CAGTGC", "TTATTT", "AGAGGG", "CCCCTA", "TCACTG"]
    invalid_mutant_dna_single_vertical = ["ATGCGA", "CTGAGC", "TTAAGT", "AGAAGG", "CCCTTA", "TCACTG"]
    invalid_mutant_dna_single_diagonal = ["ATGCGA", "CAGAGC", "TTAAGT", "AGAAAG", "CCCTTA", "TCACTG"]

    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
