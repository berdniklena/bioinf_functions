from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import os


def filter_fastq(
    input_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
    output_fastq="filtered.fastq",
):
    """
    Filter FASTQ reads by GC%, length and mean Phred quality; write results to file.
    """
    seqs = read_file(input_fastq)

    filtered_gc = dict(
        filter(lambda x: is_within_gc_bounds(x[1][0], gc_bounds), seqs.items())
    )
    filtered_len = dict(
        filter(lambda x: is_within_length(x[1][0], length_bounds), filtered_gc.items())
    )
    filtered_qual = dict(
        filter(lambda x: is_quality_satisfied(x[1][1], quality_threshold), filtered_len.items())
    )

    write_result(output_fastq, filtered_qual)


def read_file(input_fastq):
    """
    Read FASTQ using Biopython into dict: {id: (seq_str, phred_scores_list)}.
    """
    seqs = {}
    for record in SeqIO.parse(input_fastq, "fastq"):
        seqs["@" + record.id] = (str(record.seq), record.letter_annotations["phred_quality"])
    return seqs


def write_result(output_fastq, filtered_reads):
    """
    Write filtered FASTQ reads to filtered/<output_fastq>.
    """
    output_path = os.path.join("filtered", output_fastq)
    os.makedirs("filtered", exist_ok=True)

    with open(output_path, "w") as f:
        for read_id, (seq, phred_scores) in filtered_reads.items():
            qual_str = "".join(chr(q + 33) for q in phred_scores)
            f.write(read_id + "\n")
            f.write(seq + "\n")
            f.write("+\n")
            f.write(qual_str + "\n")


def is_within_gc_bounds(seq: str, gc_bounds: tuple) -> bool:
    gc_percent = gc_fraction(seq) * 100
    if len(gc_bounds) == 1:
        return gc_percent <= gc_bounds[0]
    return gc_bounds[0] <= gc_percent <= gc_bounds[1]


def is_within_length(seq: str, length_bounds: tuple) -> bool:
    n = len(seq)
    if len(length_bounds) == 1:
        return n <= length_bounds[0]
    return length_bounds[0] <= n <= length_bounds[1]


def is_quality_satisfied(phred_scores: list[int], quality_threshold: float) -> bool:
    mean_q = sum(phred_scores) / len(phred_scores)
    return mean_q >= quality_threshold

EXAMPLE_FASTQ = "example_data/example_fastq.fastq"
filter_fastq(EXAMPLE_FASTQ, gc_bounds=(50,), length_bounds=(85,), quality_threshold=30, output_fastq="out.fastq")