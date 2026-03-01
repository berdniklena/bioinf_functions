from abc import ABC, abstractmethod
import os

class BiologicalSequence(ABC):

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def get_element(self, index) -> str:
        pass

    @abstractmethod
    def pretty_print(self) -> None:
        pass

    @abstractmethod
    def check_alphabet(self) -> bool:
        pass


class NucleicAcidSequence(BiologicalSequence):

    def __init__(self, seq: str):
        if not self.check_alphabet(seq):
            raise ValueError("Invalid sequence: contains non-nucleic acid characters.")
        self._seq = seq

    @property
    def seq(self) -> str:
        return self._seq


    @abstractmethod
    def complement(self) -> str:
        pass
    

    @abstractmethod
    def reverse_complement(self) -> str:
        pass


    @abstractmethod
    def check_alphabet(self, seq: str) -> bool:
        pass


    def reverse(self) -> str:
        """
        Reverse each sequence in seq.
        """
        return self._seq[::-1]


    def __len__(self) -> int:
        return len(self._seq)


    def get_element(self, index) -> str:
        return self._seq[index]


    def pretty_print(self) -> None:
        print(self._seq.upper())
 
    

class DNASequence(NucleicAcidSequence):

    NUCLEOTIDES_DNA = set(["a", "A", "t", "T", "g", "G", "c", "C"])
    NUCLEOTIDES_COMPL = {
            "a": "t",
            "A": "T",
            "t": "a",
            "T": "A",
            "g": "c",
            "G": "C",
            "c": "g",
            "C": "G",
        }
    

    def __init__(self, seq: str):
        super().__init__(seq)


    def complement(self) -> str:
        """
        Return complements for DNA sequence.
        """
        return self.complement_nucleotides()


    def reverse_complement(self) -> str:
        """
        Return reverse complements for DNA sequences.
        """
        compl = self.complement_nucleotides()
        return compl[::-1]
    

    def complement_nucleotides(self) -> str:
        """
        Return the DNA complement (A - T, G - C).
        """
        result = ""
        for nucleotide in self.seq:
            result += self.NUCLEOTIDES_COMPL[nucleotide]
        return result
    

    def transcribe(self) -> str:
        """
        Transcribe DNA sequences in seq to RNA.
        """
        result = ""
        for nucleotide in self._seq:
            match nucleotide:
                case "t":
                    result += "u"
                case "T":
                    result += "U"
                case _:
                    result += nucleotide
        return result


    def check_alphabet(self, seq: str) -> bool:
        """
        Check if the sequence is valid DNA.

        Returns True if it contains only A, T, G, and C (case-insensitive).
        """ 
        for nucleotide in str(seq):
            if nucleotide not in self.NUCLEOTIDES_DNA:
                return False
        return True
    


class RNASequence(NucleicAcidSequence):

    NUCLEOTIDES_RNA = set(["a", "A", "u", "U", "g", "G", "c", "C"])

    def __init__(self, seq: str):
        super().__init__(seq)


    def complement(self) -> str:
        raise NotImplementedError("RNA does not have complements.")
    

    def reverse_complement(self) -> str:
        raise NotImplementedError("RNA does not have complements.")


    def check_alphabet(self, seq: str) -> bool:
        """
        Check if the sequence is valid RNA.

        Returns True if it contains only A, U, G, and C (case-insensitive).
        """
        for nucleotide in str(seq):
            if nucleotide not in self.NUCLEOTIDES_RNA:
                return False
        return True    
    

class AminoAcidSequence(BiologicalSequence):

    AMINO_ACIDS = set([
        "A", "R", "N", "D", "C",
        "Q", "E", "G", "H", "I",
        "L", "K", "M", "F", "P",
        "S", "T", "W", "Y", "V",
        "a", "r", "n", "d", "c",
        "q", "e", "g", "h", "i",
        "l", "k", "m", "f", "p",
        "s", "t", "w", "y", "v"
    ])

    def __init__(self, aa_seq: str):
        self._aa_seq = aa_seq

    @property
    def aa_seq(self) -> str:
        return self._aa_seq


    def len(self) -> int:
        return len(self._aa_seq)


    def get_element(self, index) -> str:
        return self._aa_seq[index]


    def pretty_print(self) -> None:
        print(self._aa_seq.upper())
 

    def check_alphabet(self, seq: str) -> bool:
        for amino_acid in str(seq):
            if amino_acid not in self.AMINO_ACIDS:
                return False
        return True



    
# test
seq1 = DNASequence("ATgC")
print(seq1.__len__())
print(seq1.check_alphabet(seq1.seq))
print(seq1.get_element(0))
seq1.pretty_print()


