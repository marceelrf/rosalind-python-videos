import sys
import os

from src.utils.dna_tools import transcribe_dna

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def solve():
    with open(r"data\rosalind_rna (4).txt", "r") as f:
        dna_seq = f.read().strip()
        rna_seq = transcribe_dna(dna_seq)
        
        print(rna_seq)
        
if __name__ == "__main__":
    solve()