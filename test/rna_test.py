def transcribe_dna(dna_string: str) -> str:
    if not validate_dna_string(dna_string):
        raise ValueError("Error: The sequence is NOT a valid DNA string!!!!!")
    
    rna = dna_string.replace("T","U")
    
    return rna