**Bioinformatics utilities (OOP + FASTQ filtering with Biopython)**

This repository contains two main components:

1. Object-оriented implementation of biological sequences

2. FASTQ read filtering using Biopython

The project is educational and demonstrates both OOP principles and basic FASTQ processing.


Requirements
The project dependencies are listed in `requirements.txt`:
* Python 3.12
* Biopython
* pytest (for running tests)

Install dependencies:
```bash
pip install -r requirements.txt
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

**2. FASTQ filtering (Biopython + CLI Tool)**

File: FastQ_files_Biopy.py
A command-line tool that filters FASTQ reads based on GC content, sequence length, and mean Phred quality score. GC content is calculated using Bio.SeqUtils.gc_fraction.

Usage:

```bash
python FastQ_files_Biopy.py -i <input_file.fastq> [options]
```
Options:
-i, --input (Required): Path to the input FASTQ file
-o, --output: Name of the output file (default: filtered.fastq)
--gc_min: Minimum % GC (default: 0.0)
--gc_max: Maximum % GC (default: 100.0)
--len_min: Minimum read length (default: 0)
--len_max: Maximum read length (default: 4294967296)
-q, --quality: Minimum average Phred quality (default: 0.0)

Example:
```bash
python FastQ_files_Biopy.py -i example_data/example_fastq.fastq --gc_min 40 --gc_max 60 -q 30
```
Filtered reads are written to the filtered/ directory.

**Logging and testing**

Logging: The FASTQ filter runs silently in the console. All processes, parameters, success messages, and errors are logged to a file named fastq_filter.log in the root directory.

Testing: The FASTQ filtering logic is fully covered by unit and integration tests using pytest.

To run the tests, execute the following command in the root directory:

```bash
python -m pytest
```


**Project structure**
```
BIOINF_FUNCTIONS/
├── tests/
│   └── test_fastq_filter.py
├── bioinf_functions_oop.py
├── FastQ_files_Biopy.py
├── requirements.txt
├── README.md
├── example_data/
│   └── example_fastq.fastq
├── filtered/
│   └── filtered.fastq
└── fastq_filter.log

```
