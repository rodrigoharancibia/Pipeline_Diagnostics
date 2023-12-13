from Bio import Entrez
from Bio import SeqIO

# Define os parâmetros da busca
search_term = "proteina spike covid"
database = "protein"
rettype = "fasta"
retmode = "text"

# Faz a busca no NCBI
Entrez.email = "seu_email@exemplo.com"
handle = Entrez.esearch(db=database, term=search_term)
record = Entrez.read(handle)
handle.close()

# Obtém as sequências
id_list = record["IdList"]
handle = Entrez.efetch(db=database, id=id_list, rettype=rettype, retmode=retmode)
records = SeqIO.parse(handle, rettype)
handle.close()

# Imprime as sequências obtidas
#for record in records:
    #print(record.id)
    #print(record.seq)