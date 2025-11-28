from tools.fastq_tools import is_quality_satisfied, is_within_gc_bounds, is_within_length
from tools.rna_dna_tools import (
    complement,
    is_nucleic_acid,
    reverse,
    reverse_complement,
    transcribe,
)
import os


def run_dna_rna_tools(*sequences, name):
    """
    Run a DNA/RNA operation by name on one or more sequences.
    """
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
    input_fastq, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0, output_fastq='filtered.fastq'
):
    """
    Filter FASTQ reads by GC%, length and quality; write results to file.
    """
    seqs = read_file(input_fastq)
    
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

    write_result(output_fastq, filtered_quality_threshold)


def read_file(input_fastq):
    """
    Read FASTQ file into dict: {id: (seq, qual)}.
    """
    seqs = {}
    seqs_list = open(input_fastq).readlines()

    for i in range (0, len(seqs_list), 4):
        key = seqs_list[i].strip()
        seq = seqs_list[i+1].strip()
        qual = seqs_list[i+3].strip()
        seqs[key] = (seq, qual)
    return seqs


def write_result(output_fastq, filtered_quality_threshold):
    """
    Write filtered FASTQ reads to filtered/filtered.fastq.
    """
    output_path = os.path.join("filtered", output_fastq)
    os.makedirs("filtered", exist_ok=True)
    for (k, v) in filtered_quality_threshold.items():
        open(output_path, 'a').write(k + "\n" + str(v[0]) + "\n" + "+\n" + str(v[1]) + "\n")