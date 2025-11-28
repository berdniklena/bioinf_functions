**Bioinformatics utilities**

A small collection of Python tools for basic bioinformatics workflows, including DNA/RNA sequence operations, FASTQ filtering, FASTA processing, and simple BLAST result extraction.

Features

1. DNA/RNA sequence utilities
Use run_dna_rna_tools() to apply common operations:
- is_nucleic_acid - check if sequences are valid DNA/RNA
- transcribe - DNA → RNA
- reverse - reverse sequences
- complement - DNA complement
- reverse_complement - reverse DNA complement

2. FASTQ filtering
filter_fastq() filters reads based on:
- GC-content (gc_bounds)
- sequence length (length_bounds)
- average quality score (quality_threshold)
Filtered reads are written to filtered/filtered.fastq.

3. FASTA and BLAST processing
- convert_multiline_fasta_to_oneline() - converts multiline FASTA into one-line-per-sequence format.
Converted format is written to converted/output.fa
- parse_blast_output() - extracts protein IDs with significant BLAST hits.
Filtered and sorted proteins ID are written to filtered/filtered_proteins.txt


**Project structure**
```
BIOINF_FUNCTIONS/
├── bioinf_functions.py
├── bio_files_processor.py
├── test_files.py
├── test_nucleic_acids.py
├── README.md
│
├── example_data/
│   ├── example_fastq.fastq
│   ├── example_multiline_fasta.fasta
│   └── example_blast_results.txt
│
├── filtered/
│   ├── filtered.fastq
│   └── filtered_proteins.txt
│
├── converted/
│   └── output.fa
│
└── tools/
    ├── fastq_tools.py
    └── rna_dna_tools.py
```
