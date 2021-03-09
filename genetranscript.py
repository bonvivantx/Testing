import sys
with open(r"C:\Users\KENEEL DIAM\Downloads\sequence (4).fasta") as seq:
    seq.readline()                  #remove first line of fasta file
    geneseq=seq.read()              #storing remaining sequence
    seq.close()
geneseq=geneseq.replace("\n","")    #cleaning sequence
print("The gene has "+str(len(geneseq))+" nucleotides \n")  #length of gene
cds=geneseq[82:925]                 #splicing cds
mRNA=cds.replace("T","U")           #substituting U with T
print("The trandcript's length is "+str(len(mRNA))+"\n")    #length of transcipt
print("The transcipt is: "+mRNA+"\n")   #printing transcipt
revseq=list(reversed(geneseq))          #making and reversing list
revseq=''.join(revseq)                  #converting to string
print("The reversed dna is: "+revseq+"\n")  #printing reversed dna
revcomp=((((geneseq.replace("T","a")).replace("A","t")).replace("C", "g")).replace("G", "c")).upper()
print("The reversed complement is: "+revcomp+"\n")  #printing reverse complement
count_EcoRI=geneseq.count("GAATTC")        #counting resctriction sites
count_BamHI=geneseq.count("GGATCC")
count_HindIII=geneseq.count("AAGCTT")
print("The number of recognition sites for EcorI is "+str(count_EcoRI)+"\n")    #printing number os restriction sites
print("The number of recognition sites for BamHI is "+str(count_BamHI)+"\n")
print("The number of recognition sites for HindIII is "+str(count_HindIII)+"\n")
