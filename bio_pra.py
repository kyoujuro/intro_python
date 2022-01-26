from Bio.Seq import Seq
from Bio import SeqIO
my_seq = Seq("AGTACACTGGTA")
print(my_seq.complement())
with open("file.fasta", "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        id_part = record.id
        desc_part = record.description
        seq = record.seq
        print("id:", id_part)
        print("desc:", desc_part)
        print("seq:", seq)
        print("Residues 1-10 of the sequence are " + seq[0:10])