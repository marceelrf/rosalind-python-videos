
def validate_dna_string(dna_string: str) -> bool:
    if not isinstance(dna_string, str):
        return False
    
    if not dna_string:
        return False
    
    valid_nucleotides = set('ATCG')
    return all(nucleotide in valid_nucleotides for nucleotide in dna_string.upper())

def count_nucleotides(dna_string: str) -> str:
    
    if not validate_dna_string(dna_string):
        raise ValueError("Error: The sequence is NOT a valide DNA string!!!!!")
    
    N_A = dna_string.count("A")
    N_C = dna_string.count("C")
    N_G = dna_string.count("G")
    N_T = dna_string.count("T")
    
    return print(f"{N_A} {N_C} {N_G} {N_T}")
