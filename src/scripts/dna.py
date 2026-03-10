import sys
import os

from src.utils.dna_tools import count_nucleotides

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def solve():
    with open(r"data\rosalind_dna (4).txt", "r") as f:
        seq = f.read().strip()
        count_nucleotides(seq)
        
if __name__ == "__main__":
    solve()