from Bio import Entrez, SeqIO

Entrez.email = "araoianarao@gmail.com"

# Fetch a sample DNA sequence (Human Insulin gene fragment)
handle = Entrez.efetch(db="nucleotide", id="NM_000207", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

print("Sequence ID:", record.id)
print("Sequence Length:", len(record.seq))
print("First 100 bases:", record.seq[:100])

# Basic analysis
gc_content = (record.seq.count("G") + record.seq.count("C")) / len(record.seq) * 100
print(f"GC Content: {gc_content:.2f}%")
