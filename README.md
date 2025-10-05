**DNA/RNA and FASTQ processing tools**

This module provides a collection of utility functions for analysing and processing DNA/RNA sequences and FASTQ files.
It combines two sets of tools:

_Nucleic acid operations_ - is nucleic acid, reverse, complement, transcribe, reverse complement

_FASTQ filtering_ - sequence filtering by GC content, length, and quality.

**Project structure**
```
project/
├── main.py                    # Contains the run_dna_rna_tools and filter_fastq functions
└── tools/
    ├── fastq_tools.py         # Defines filter_gc, filter_length, and filter_quality
    └── rna_dna_tools.py       # Defines complement, reverse, transcribe, etc.
```

__Usage__

1. Nucleic acid utilities
Use the run_dna_rna_tools() function to perform DNA/RNA operations.
It supports several commands via the name argument.
Supported operations
is_nucleic_acid - checks whether input sequences are DNA or RNA
transcribe - converts DNA to RNA
reverse - returns the reversed sequence
complement - returns the complementary sequence
reverse_complement - returns the reverse complementary sequence

2. FASTQ filtering
The filter_fastq() function filters FASTQ data (as a dictionary) by:
- GC-content range. GC filter - removes sequences with GC% outside gc_bounds
- sequence length range. Length filter - removes sequences shorter or longer than length_bounds
- average quality threshold. Quality filter - removes sequences below quality_threshold


License © 2025 - Elena Kalita 