from tarfile import REGTYPE
from Bio import Entrez
from Bio import SeqIO
import glob
# Define os parâmetros da busca


Entrez.email ="mscb.suporte@gmail.com"
handle = Entrez.einfo()

#Acesso ao database e procura de proteína, busca por espécie (todas as proteínas da mesma especie,sem saber o nome do gene, separar por genoma)=> genomas completos
handle = Entrez.esearch(db="protein", term="tp53[gene] NOT partial AND mammals[ORGN]", retmax='100')
record = Entrez.read (handle)

#Criar um arquivo de leitura e escrita
arquivo = open("tp53.txt","r") ####

for arquivo in glob.glob("*fasta"):
with open("tp53.fasta","w") as arquivo:
    arquivo.write(handle.read())
handle.close()

#Obtém sequencias
id_list = record["IdList"]
handle = Entrez.efetch(db="protein", term="tp53[gene] NOT partial AND mammals[ORGN]", retmax='100')
records = SeqIO.parse(handle, REGTYPE)
with open("tp53.fasta", "w") as arquivo:
    arquivo.write(handle.read())
handle.close()