import sys
import os

from src.utils.dna_tools import reverse_complement

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def solve():
    with open(r"data\rosalind_revc (5).txt", "r") as f:
        
        dna_seq = f.read().strip();
        
        revc = reverse_complement(dna_seq)
        
        return print(revc)
    
if __name__ == "__main__":
    solve()