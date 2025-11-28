def is_dna(sequence: str) -> bool:
    """
    Check if the sequence is valid DNA.

    Returns True if it contains only A, T, G, and C (case-insensitive).
    """
    nucleotides_dna = set(["a", "A", "t", "T", "g", "G", "c", "C"])
    for nucleotide in str(sequence):
        if nucleotide not in nucleotides_dna:
            return False
    return True


def is_rna(sequence: str) -> bool:
    """
    Check if the sequence is valid RNA.

    Returns True if it contains only A, U, G, and C (case-insensitive).
    """
    nucleotides_rna = set(["a", "A", "u", "U", "g", "G", "c", "C"])
    for nucleotide in sequence:
        if nucleotide not in nucleotides_rna:
            return False
    return True


def is_nucleic_acid(seq: list[str]) -> list[bool]:
    """
    Return True for each sequence that is DNA or RNA.
    """
    result = []
    for sequence in seq:
        if is_dna(sequence) or is_rna(sequence):
            result.append(True)
        else:
            result.append(False)
    return result


def transcribe(seq: list[str]) -> list[str]:
    """
    Transcribe all valid DNA sequences in seq to RNA.
    """
    result = []
    for sequence in seq:
        if is_dna(sequence):
            rna = make_rna(sequence)
            result.append(rna)
    return result


def make_rna(sequence: str) -> str:
    """
    Transcribe a DNA sequence to RNA.

    Replaces thymine (T/t) with uracil (U/u).
    """
    result = ""
    for nucleotide in sequence:
        match nucleotide:
            case "t":
                result += "u"
            case "T":
                result += "U"
            case _:
                result += nucleotide
    return result


def complement(seq: list[str]) -> list[str]:
    """
    Return complements for all valid DNA sequences.
    """
    result = []
    for sequence in seq:
        if is_dna(sequence):
            result.append(complement_nucleotides(sequence))
    return result


def complement_nucleotides(sequence: str) -> str:
    """
    Return the DNA complement (A - T, G - C).
    """
    nucleotides_compl = {
        "a": "t",
        "A": "T",
        "t": "a",
        "T": "A",
        "g": "c",
        "G": "C",
        "c": "g",
        "C": "G",
    }
    result = ""
    for nucleotide in sequence:
        result += nucleotides_compl.get(nucleotide)
    return result


def reverse(seq: list[str]) -> list[str]:
    """
    Reverse each sequence in seq.
    """
    result = []
    for sequence in seq:
        result.append(sequence[::-1])
    return result


def reverse_complement(seq: list[str]) -> list[str]:
    """
    Return reverse complements for all valid DNA sequences.
    """
    result = []
    for sequence in seq:
        if is_dna(sequence):
            compl = complement_nucleotides(sequence)
            result.append(compl[::-1])
    return result
