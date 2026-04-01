from Bio import SeqIO

def gc_percent(dna_string: str) -> str:
    GC_count = record.seq.count("C") + record.seq.count("G")
    GC_percent = (GC_count/len(record.seq))*100
    
    return GC_percent

with open(r"C:\Users\madra\Downloads\protein (2).fasta", "r") as file:
    GC_max = 0
    
    for record in SeqIO.parse(file, "fasta"):
        
        GC_percent = gc_percent(record.seq)
        
        if GC_percent > GC_max:
            GC_max = GC_percent
            id_max = record.id
        
    
    print(f"{id_max}\n{GC_max:.4f}")