from tools.fastq_tools import is_quality_satisfied, is_within_gc_bounds, is_within_length
from tools.rna_dna_tools import (
    complement,
    is_nucleic_acid,
    reverse,
    reverse_complement,
    transcribe,
)


def run_dna_rna_tools(*sequences, name):
    match name:
        case "is_nucleic_acid":
            return is_nucleic_acid(sequences)
        case "transcribe":
            return transcribe(sequences)
        case "reverse":
            return reverse(sequences)
        case "complement":
            return complement(sequences)
        case "reverse_complement":
            return reverse_complement(sequences)
        case _:
            return "Invalid operation"


def filter_fastq(
    seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0
):
    filtered_gc_bounds = dict(
        filter(lambda fastq: is_within_gc_bounds(fastq[1][0], gc_bounds), seqs.items())
    )
    filtered_length_bounds = dict(
        filter(
            lambda fastq: is_within_length(fastq[1][0], length_bounds),
            filtered_gc_bounds.items(),
        )
    )
    filtered_quality_threshold = dict(
        filter(
            lambda fastq: is_quality_satisfied(fastq[1][1], quality_threshold),
            filtered_length_bounds.items(),
        )
    )

    return filtered_quality_threshold
