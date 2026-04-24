**Bioinformatics utilities (OOP + FASTQ filtering with Biopython)**

This repository contains two main components:

1. Object-оriented implementation of biological sequences

2. FASTQ read filtering using Biopython

The project is educational and demonstrates both OOP principles and basic FASTQ processing.


Requirements
* Python 3.12
* Biopython

Install dependencies:
```bash
pip install biopython
```

**1. OOP: biological sequences**

File: bioinf_functions_oop.py
The following classes are implemented:
* BiologicalSequence - abstract base class
* NucleicAcidSequence - abstract class for nucleic acids
* DNASequence - supports:
    * reverse()
    * complement()
    * reverse_complement()
    * transcribe()
* RNASequence - RNA sequence validation
* AminoAcidSequence - aminoacid sequence handling and alphabet validation

**2. FASTQ filtering (Biopython)**

File: FastQ_files_Biopy.py
The function filter_fastq() filters reads based on:
* GC content (gc_bounds)
* Sequence length (length_bounds)
* Mean Phred quality score (quality_threshold)

GC content is calculated using Bio.SeqUtils.gc_fraction.
Phred quality scores are extracted from Biopython via 
```record.letter_annotations["phred_quality"]```
Filtered reads are written to the filtered/ directory.


**Project structure**
```
BIOINF_FUNCTIONS/
├── bioinf_functions_oop.py
├── FastQ_files_Biopy.py
├── README.md
│
├── example_data/
│   └── example_fastq.fastq
│
└── filtered/
    └── filtered.fastq

```
