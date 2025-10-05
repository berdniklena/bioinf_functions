from bioinf_functions import run_dna_rna_tools


print(run_dna_rna_tools("aagGgAaatttcCCTa", name="is_nucleic_acid"))
print(run_dna_rna_tools("aAtTgGcC", name="is_nucleic_acid"))
print(run_dna_rna_tools("aaggaaUucCCTa", name="is_nucleic_acid"))
print(run_dna_rna_tools("aagguUaauUtttcCCTa", name="is_nucleic_acid"))
print(run_dna_rna_tools("aag-dfjgdtcCCTa", name="is_nucleic_acid"))
print(run_dna_rna_tools("aauuggcC", "aag-dfjgdtcCCTa", name="is_nucleic_acid"))

print(run_dna_rna_tools("aagGgAaatttcCCTa", name="transcribe"))
print(run_dna_rna_tools("aAtTgGcC", name="transcribe"))
print(run_dna_rna_tools("aaggaaUucCCTa", name="transcribe"))
print(run_dna_rna_tools("aagguUaauUtttcCCTa", name="transcribe"))
print(run_dna_rna_tools("aag-dfjgdtcCCTa", name="transcribe"))
print(run_dna_rna_tools("aauuggcC", "aag-dfjgdtcCCTa", name="transcribe"))

print(run_dna_rna_tools("aagGgAaatttcCCTa", name="reverse"))
print(run_dna_rna_tools("aAtTgGcC", name="reverse"))
print(run_dna_rna_tools("aaggaaUucCCTa", name="reverse"))
print(run_dna_rna_tools("aagguUaauUtttcCCTa", name="reverse"))
print(run_dna_rna_tools("aag-dfjgdtcCCTa", name="reverse"))
print(run_dna_rna_tools("aauuggcC", "aag-dfjgdtcCCTa", name="reverse"))

print(run_dna_rna_tools("aagGgAaatttcCCTa", name="complement"))
print(run_dna_rna_tools("aAtTgGcC", name="complement"))
print(run_dna_rna_tools("aaggaaUucCCTa", name="complement"))
print(run_dna_rna_tools("aagguUaauUtttcCCTa", name="complement"))
print(run_dna_rna_tools("aag-dfjgdtcCCTa", name="complement"))
print(run_dna_rna_tools("aauuggcC", "aag-dfjgdtcCCTa", name="complement"))

print(run_dna_rna_tools("aagGgAaatttcCCTa", name="reverse_complement"))
print(run_dna_rna_tools("aAtTgGcC", name="reverse_complement"))
print(run_dna_rna_tools("aaggaaUucCCTa", name="reverse_complement"))
print(run_dna_rna_tools("aagguUaauUtttcCCTa", name="reverse_complement"))
print(run_dna_rna_tools("aag-dfjgdtcCCTa", name="reverse_complement"))
print(run_dna_rna_tools("aauuggcC", "aag-dfgdtcTa", name="reverse_complement"))