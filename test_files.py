from bioinf_functions import filter_fastq
from bio_files_processor import convert_multiline_fasta_to_oneline, parse_blast_output

EXAMPLE_FASTQ = 'example_data/example_fastq.fastq'
print(filter_fastq(EXAMPLE_FASTQ, gc_bounds=(50,), length_bounds=(85,), quality_threshold=30))

convert_multiline_fasta_to_oneline('example_data/example_multiline_fasta.fasta')

parse_blast_output('example_data/example_blast_results.txt')