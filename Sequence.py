#!/usr/bin/env python3

class Error(Exception):
    """Base Class For The Following Exception"""
    pass

class DifferentLengthsError(Error):
    """Raised When DNA Sequences of Different Lengths are Compared"""
    pass

class Sequence:

    def __init__(self, dna):
        self.dna = dna.lower()

    def dnaBases(self):
        dnaBaseCount = len(self.dna)
        return(dnaBaseCount)

    def is_dna(self):
        validDNA = "atgc"
        
        validityOfDNA = all(base in validDNA for base in self.dna)

        return(validityOfDNA)

    def __eq__(self, new):
         if isinstance(self, Sequence) == isinstance(new, Sequence) and self.dna == new.dna:
             return True
         else:
             return False
    
    def dnaComplement(self):
        complementDict = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
        return "".join(complementDict[base] for base in self.dna)

    def pairofNonMatchingBases(self, new):
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
        signal = "AAAAAAAAAATTTTTTTTTT"
        dnaSequence = str(self.dna)
        findGenes = dnaSequence.split(signal.lower())
        findGenes = [Sequence(gene) for gene in findGenes]
        return(findGenes)

    def swapMutations(self, new):
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
