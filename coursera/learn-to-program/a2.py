'''
http://spark-public.s3.amazonaws.com/programming1/a2/a2.html

A2 Problem Domain: Deoxyribonucleic Acid (DNA)

DNA is the double-stranded molecule that encodes genetic information for living organisms. 
DNA is made up of four kinds of nucleotides, which are molecules that bond together to form DNA sequences.

The four nucleotides are adenine (A), guanine (G), cytosine (C), and thymine (T). 
Each strand of DNA is a sequence of nucleotides, for example AGCTAC. 
In a program, we will use a string representation of this, "AGCTAC".

DNA has 2 strands in a double helix. The nucleotides in one strand are bonded to the nucleotides in the other strand. 
A and T can be bonded together, and thus complement each other; similarly, C and G are complements of each other.

You can see a picture of this on the Wikipedia page for DNA. The two strands in DNA are complementary because 
each nucleotide in one strand is bonded with its complement in the other strand. 
Thus, given the DNA sequence ACGTACG, its complementary strand is TGCATGC.

Terminology in this handout

A DNA sequence is a sequence of nucleotides, such as TCATGT. 
'''


def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return(len(dna))

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    
    return (len(dna1) > len(dna2))

def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    counter = 0
    for i in range(0, len(dna)):
        if dna[i] == nucleotide: 
            counter += 1
        
    return counter

def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    '''

    for i in range(0, len(dna1)):
        if (i != len(dna1) - 1) and (dna2[0] == dna1[i]) and (dna2[1] == dna1[i+1]): 
            return True
    return False

def is_valid_sequence(dna):
    '''(str) -> bool
    
    Return True if and oly if the DNA sequence is valid; that is, it contains no other
    characters other than A, T, C and G.
    Lowercase characters are not valid
    
    >> is_valid_sequence('ATcGGC')
    False
    >> is_valid_sequence('21CGGC')
    False
    >> is_valid_sequence('ATCGG$')
    False
    >> is_valid_sequence('BTCGGT')
    False
    >> is_valid_sequence('ATCGGZ')
    False    
    >> is_valid_sequence('ATCGGC')
    True
    '''
    
    for char in dna:
        if (not char in 'ATCG') or (not char.isupper()) or (not char.isalpha()):
            return False
    return True

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str
    
    The first two parameters are DNA sequences and the third parameter is an index. 
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at
    the given index. (You can assume that the index is valid.) 
    
    >> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >> insert_sequence('CCGG', 'AT', 0)
    ATCCGG
    >> insert_sequence('CCGG', 'AT', 4)
    CCGGAT
    '''

    dna1 = dna1[:index] + dna2 + dna1[index:]
    return (dna1)    

def get_complement(nucleotide):
    '''(str) -> (str)
    
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement. 
    
    >> get_complement('A')
    T
    >> get_complement('T')
    A
    >> get_complement('C')
    G
    >> get_complement('G')
    C
    '''

    d = {'A':'T', 'T':'A', 'C':'G', 'G':'C', '':''}
    
    return d[nucleotide.upper()]

def get_complementary_sequence(sequence):
    '''(str) -> (str)
    
    The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.  
    
    >> get_complementary_sequence('AT')
    TA
    >> get_complementary_sequence('TA')
    AT
    >> get_complementary_sequence('CG')
    GC
    >> get_complementary_sequence('GC')
    CG
    >> get_complementary_sequence('')

    >> get_complementary_sequence('')    
    '''

#    d = {'AT':'TA', 'TA':'AT', 'CG':'GC', 'GC':'CG', '':'', 'ATCG':'TAGC', 'TACG':'ATGC', 'ATGC':'TACG','TAGC':'ATCG'}
    
    complementary = ''
    for nucleotide in sequence:
        complementary = complementary + get_complement(nucleotide)
    
    return (complementary)
#    return d[sequence.upper()]