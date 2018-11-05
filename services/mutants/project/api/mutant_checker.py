import numpy as np


class MutantChecker():

    def __init__(self):
        self.totalFound = 0
        self.VALID_DNA = ['A', 'T', 'G', 'C']

    def check_chain(self, chain):
        ''' searchs for a repetition of chars in a chain of DNA,
            based on the equalty of the next value.'''
        repeated_found = 0
        for i in range(0, len(chain)):
            if chain[i] not in self.VALID_DNA:
                raise ValueError('Error: invalid DNA. Only accepts DNA with (A, C, G, T) and with NxN dimentions. Please check your input DNA payload.')
            if i < len(chain)-1 and chain[i] == chain[i+1]:
                repeated_found += 1
            else:
                repeated_found = 0
            if repeated_found == 3:
                self.totalFound += 1
                repeated_found = 0

    def check_horizontal(self, dna_matrix):
        ''' Extract all horizontal chains from the DNA to check'''
        for chain in dna_matrix:
            self.check_chain(chain)

    def check_vertical(self, dna_matrix):
        ''' Extract all vertical chains from the DNA to check'''
        for i in range(0, len(dna_matrix)):
            self.check_chain(dna_matrix[:,i])

    def check_diagonal(self, dna_matrix):
        ''' Extract all diagonals chains from the DNA to check'''
        i = 0
        v_diagonal = np.diag(dna_matrix, k=i)
        h_diagonal = None
        while len(v_diagonal) >= 4:  # como a atrix eh NxN, podemos confiar
            self.check_chain(v_diagonal)
            # como as diagonais k=0, k=-0 sao iguais, verificamos se i > 0
            # para evitar check repetido da primeira diagonal (0,0)
            if i > 0:
                self.check_chain(h_diagonal)
            i += 1
            v_diagonal = np.diag(dna_matrix, k=i)
            h_diagonal = np.diag(dna_matrix, k=-i)

    def isValidDNA(self, dna_matrix):
        ''' Checks if DNA is valid. To be valid, a DNA matrix should only contains \
            valid DNA chars (A, C, G, T) and NxN dimension.
            Thows a ValueError exception if the matrix is not validselfself.
            If the DNA matrix is valid, does nothing. '''

        if not len(dna_matrix):
            raise ValueError('Error: DNA matrix must be informed. ')

        if len(dna_matrix) != len(dna_matrix[0]):
            raise ValueError('Error: DNA matrix must be square (NxN). ')

    def isMutant(self, dna):
        matrix = np.array([list(i) for i in dna])

        self.isValidDNA(matrix)
        self.check_horizontal(matrix)
        self.check_vertical(matrix)
        self.check_diagonal(matrix)
        return self.totalFound > 1
