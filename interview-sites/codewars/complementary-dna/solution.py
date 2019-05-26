# https://www.codewars.com/kata/complementary-dna/train/python

def DNA_strand(dna):
    compliment = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(compliment[l] for l in dna)
