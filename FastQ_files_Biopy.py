import argparse
import logging
import os
import sys
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


logging.basicConfig(
    filename="fastq_filter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


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
    logging.info(f"Starting filtering of {input_fastq}")
    logging.info(
        f"Parameters: GC {gc_bounds}, Length {length_bounds}, Quality >={quality_threshold}"
    )

    try:
        seqs = read_file(input_fastq)
    except FileNotFoundError as e:
        logging.error(f"Error reading file. Please ensure the path is correct: {e}")
        raise

    if not seqs:
        logging.warning("File is empty or has an invalid format.")

    filtered_gc = dict(
        filter(lambda x: is_within_gc_bounds(x[1][0], gc_bounds), seqs.items())
    )
    filtered_len = dict(
        filter(lambda x: is_within_length(x[1][0], length_bounds), filtered_gc.items())
    )
    filtered_qual = dict(
        filter(
            lambda x: is_quality_satisfied(x[1][1], quality_threshold),
            filtered_len.items(),
        )
    )

    write_result(output_fastq, filtered_qual)
    logging.info(
        f"Filtering completed successfully. {len(filtered_qual)} reads saved to {output_fastq}"
    )


def read_file(input_fastq):
    """
    Read FASTQ using Biopython into dict: {id: (seq_str, phred_scores_list)}.
    """
    seqs = {}
    for record in SeqIO.parse(input_fastq, "fastq"):
        seqs["@" + record.id] = (
            str(record.seq),
            record.letter_annotations["phred_quality"],
        )
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
    if not phred_scores:
        return False
    mean_q = sum(phred_scores) / len(phred_scores)
    return mean_q >= quality_threshold


def main():
    parser = argparse.ArgumentParser(
        description="Filtration of FASTQ files by GC content, length, and quality (Phred)."
    )

    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input FASTQ file"
    )
    parser.add_argument(
        "-o", "--output", default="filtered.fastq", help="Name of the output file"
    )
    parser.add_argument("--gc_min", type=float, default=0.0, help="Minimum % GC")
    parser.add_argument("--gc_max", type=float, default=100.0, help="Maximum % GC")
    parser.add_argument("--len_min", type=int, default=0, help="Minimum read length")
    parser.add_argument(
        "--len_max", type=int, default=2**32, help="Maximum read length"
    )
    parser.add_argument(
        "-q", "--quality", type=float, default=0.0, help="Minimum average Phred quality"
    )

    args = parser.parse_args()

    try:
        filter_fastq(
            input_fastq=args.input,
            gc_bounds=(args.gc_min, args.gc_max),
            length_bounds=(args.len_min, args.len_max),
            quality_threshold=args.quality,
            output_fastq=args.output,
        )
    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    main()
