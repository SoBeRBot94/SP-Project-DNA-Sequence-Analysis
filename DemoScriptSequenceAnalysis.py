#!/usr/bin/env python3

import Sequence
from Sequence import Sequence as sq
import matplotlib.pyplot as plt

numberOfSequences = int(input("Enter the number of input sequences: \t"))
sequenceList = []

for number in range(numberOfSequences):
    dna = sq(str(input("\n Enter the dna sequence: \t")))
    print("\n ==================== NEW SEQUENCE INSTANCE IS GETTING CREATED ==================== \n")
    sequenceList.append(dna)
    print("\n ==================== SEQUENCE ISNTANCE CREATION IS DONE ==================== \n")

lengthOfSequence = sq.dnaBases(sequenceList[0])
print("\n The length of the dna sequence is: \t {}".format(lengthOfSequence))

validDNA = sq.is_dna(sequenceList[0])
assert validDNA == True, "\n The input sequence is not a valid dna sequence"

sequenceX = sq("TGCAATGC")
sequenceY = sq("tgcaatgc")
sequenceZ = sq("TGACATGC")

valueA = (sequenceX == sequenceY)
valueB = (sequenceX == sequenceZ)

assert valueA == True, "\n The dna sequences are not of the same object type and are not equal"
assert valueB == False, "\n The dna sequences are equal"

dna = sq("TGCAATGC")
dnaComplement = sq("ACGTTACG")
sequenceComplement = sq.dnaComplement(dna)

if dnaComplement == sequenceComplement:
    print("\n The sequences have been complemented successfully")
else:
    print("\n sequence complement has failed")

mismatchedIndex = sq.pairofNonMatchingBases(sequenceX, sequenceZ)
print("\n DNA mismatch found at position: \t {}".format(mismatchedIndex))

genomeA = Sequence.readGenomeData("./genome_01.dat")
print("\n ==================== GENOME DATA IMPORTED ==================== \n")

geneA = sq.sequenceToGenes(genomeA)
lengthOfGeneA = sq.dnaBases(geneA[0])
print("\n The length of the first gene is: \t {}".format(lengthOfGeneA))

genomeB = Sequence.readGenomeData("./genome_02.dat")
print("\n ==================== GENOME DATA IMPORTED ==================== \n")

geneB = sq.sequenceToGenes(genomeB)

geneMutation = []
geneLength = []

for base in range(0, len(geneA)):
    mutationCount = sq.swapMutations(geneA[base], geneB[base])
    geneMutation.append(mutationCount)
    geneCount = sq.dnaBases(geneA[base])
    geneLength.append(geneCount)


plt.style.use(['ggplot','dark_background'])
plt.figure(0,figsize = (19,9))
plt.title("Gene Length Histogram")
plt.xlabel("Gene", fontsize = "15")
plt.ylabel("Gene Length", fontsize = "15")
plt.bar(range(len(geneLength)), geneLength)
plt.savefig("GeneLengthHistogram.png")
plt.show()

plt.figure(1,figsize = (19,9))
plt.title("Gene Mutation vs Gene Length", fontsize = "20")
plt.xlabel("Gene Mutation", fontsize = "15")
plt.ylabel("Gene Length", fontsize = "15")
plt.scatter(geneMutation, geneLength, color = "red")
plt.savefig("GeneMutation-vs-GeneLength.png")
plt.show()
