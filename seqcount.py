import sys
with open(r"C:\Users\KENEEL DIAM\Downloads\sequence (4).fasta") as seq:
    seq.readline()                  #Remove first line of fasta file
    geneseq=seq.read()              #storing remaining sequence
    seq.close()
geneseq=geneseq.replace("\n","")
genelength=len(geneseq)            #length of geneseq
A_count=geneseq.count("A")          #number of A's
T_count=geneseq.count("T")          #number of T's
G_count=geneseq.count("G")          #number of G's
C_count=geneseq.count("C")          #number of C's
stop_count=geneseq.count("TAA")+geneseq.count("TAG")+geneseq.count("TGA")  #number of stop codons
start_count=geneseq.count("ATG")    #number of A's
GCcontent=((C_count+G_count)/genelength)*100
print("length of gene sequence is "+str(genelength))
print("count of A in seq is "+str(A_count))
print("count of T in seq is "+str(T_count))
print("count of G in seq is "+str(G_count))
print("count of C in seq is "+str(C_count))
print("count of stop codons in seq is "+str(stop_count))
print("count of start codons in seq is "+str(start_count))
print("GC content is "+str(GCcontent))
