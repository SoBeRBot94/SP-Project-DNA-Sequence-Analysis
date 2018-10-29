#!/usr/bin/env python3

class Error(Exception):
    """Base Class For The Following Exception"""
    pass

class DifferentLengthsError(Error):
    """Raised When DNA Sequences of Different Lengths are Compared"""
    pass

class Sequence:

    def __init__(self, dna):
        """Class Constuctor, transforms the input object to be case insensitive"""
        self.dna = dna.lower()

    def dnaBases(self):
        """This method reutrns the number of dna bases in the input object"""
        dnaBaseCount = len(self.dna)
        return(dnaBaseCount)

    def is_dna(self):
        """This method checks whether the input object is a dna sequence"""
        validDNA = "atgc"
        
        validityOfDNA = all(base in validDNA for base in self.dna)

        return(validityOfDNA)

    def __eq__(self, new):
        """This method overrides the defult __eq__ magic method with the newly defined method"""
         if isinstance(self, Sequence) == isinstance(new, Sequence) and self.dna == new.dna:
             return True
         else:
             return False
    
    def dnaComplement(self):
        """This generates the complement of the given input sequence"""
        complementDict = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
        return "".join(complementDict[base] for base in self.dna)

    def pairofNonMatchingBases(self, new):
        """This method returns the value of the first index where there is a mismatch"""
        sequenceA = self.dna
        sequenceB = new.dna

        try:
            if len(sequenceA) != len(sequenceB):
                raise DifferentLengthsError
            elif len(sequenceA) == len(sequenceB) and str(sequenceA) == str(sequenceB):
                return(-1)
            else:
                for base in range(0, len(sequenceA)):
                    if sequenceA[base] != sequenceB[base]:
                        return(base)
                        break
        except DifferentLengthsError:
            print('Cannot Compare DNA Sequences of Different Lengths ! \n')

    def sequenceToGenes(self):
        """This method splits the genome into individual genes based on the stop signal and returns them as a list"""
        signal = "AAAAAAAAAATTTTTTTTTT"
        dnaSequence = str(self.dna)
        findGenes = dnaSequence.split(signal.lower())
        findGenes = [Sequence(gene) for gene in findGenes]
        return(findGenes)

    def swapMutations(self, new):
        """This method counts the number of swap mutaions for two sequences that are being compared and returns the count"""
        sequenceA = self.dna
        sequenceB = new.dna

        mutationCount = 0

        try:
            if len(sequenceA) != len(sequenceB):
                raise DifferentLengthsError
            else:
                for base in range(0, len(sequenceA)):
                    if sequenceA[base] != sequenceB[base]:
                        mutationCount += 1
                return(mutationCount)
        except DifferentLengthsError:
            print('Cannot Compare DNA Sequences of Different Lengths ! \n')

#--------------------------------------------------

def readGenomeData(file):

    with open(file, mode = "r", encoding = "ascii") as genome:
        sequenceLines = genome.read().splitlines(True)
        sequenceLine = ''.join(sequenceLines[1:])

        DNAsequence = Sequence(sequenceLine)
        sequenceLength = Sequence.dnaBases(DNAsequence)
        return(DNAsequence)
