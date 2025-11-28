import os


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta="output.fa"):
    """
    Convert multiline FASTA to one-line-per-sequence format.
    """
    fasta = read_file(input_fasta)
    write_result(output_fasta, fasta)


def parse_blast_output(input_file, output_file='filtered_proteins.txt'):
    """
    Extract protein IDs with significant BLAST hits and save them.
    """
    proteins = filter_file(input_file)
    write_to_file(proteins, output_file)


def read_file(input_fasta):
    """
    Read FASTA into dict: {header: sequence} (one-line merged).
    """
    fasta = {}
    fasta_list = open(input_fasta).readlines()
    i = 0
    while i < len(fasta_list):
        value = ""
        key = fasta_list[i].strip() 
        i+=1
        while i < len(fasta_list) and not fasta_list[i].startswith('>'):
            value+=fasta_list[i].strip()
            i+=1
        fasta[key] = value
       
    return fasta


def write_result(output_fasta, converted_fasta):
    """
    Write converted FASTA to converted/output.fa.
    """
    output_path = os.path.join("converted", output_fasta)
    os.makedirs("converted", exist_ok=True)
    for (k, v) in converted_fasta.items():
        open(output_path, 'a').write(k + "\n" + v + "\n")


def filter_file(input_file):
    """
    Parse BLAST output and return sorted list of matched protein IDs.
    """
    protein = []
    protein_list = open(input_file).readlines()
    for i in range(0, len(protein_list)):
        if protein_list[i].startswith('Sequences producing significant alignments:'):
            protein.append(protein_list[i + 3][:66].strip())
    return sorted(protein)
    

def write_to_file(proteins, output_file):
    """
    Write list of protein IDs to filtered/filtered_proteins.txt.
    """
    output_path = os.path.join("filtered", output_file)
    os.makedirs("filtered", exist_ok=True)
    for protein in proteins:
        open(output_path, 'a').write(protein + '\n')