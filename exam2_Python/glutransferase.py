# Escriba aquí su código para el ejercicio 2
#import modulo
def source(data): 
    seqs = open(data, "r")
    secuencias  = open("data/source.gb", "w")
    for linea in seqs: 
        Entrez.email = "jhesel.almeida@est.ikiam.edu.ec"
        handle=Entrez.efetch(db="nucleotide" ,id=linea ,rettype="gb", retmode="text")
        data=(handle.read())
        secuencias.write(data) 
        print (contador)
    record_gb = list(SeqIO.parse("data/source.gb", "genbank"))
    source = []
    for i in range(len(record_gb)):
        source.append(record_gb[i].annotations["source"])
        frecuencias = collections.Counter(source)
    frecuencias = collections.Counter(source)
    df = pd.DataFrame(frecuencias.items(), columns=["Especie", "Frecuencia"])
    df.to_csv("results/frecuencias.csv") 
    return df 


def sequences(data): 
    seqs = open(data, "r")
    secuencias  = open("data/sequences.gb", "w")
    for linea in seqs: 
        Entrez.email = "jhesel.almeida@est.ikiam.edu.ec"
        handle=Entrez.efetch(db="nucleotide" ,id=linea ,rettype="gb", retmode="text")
        data=(handle.read())
        secuencias.write(data) 
    record_gb = list(SeqIO.parse("data/sequences.gb", "genbank"))
    MW = []
    indice_ins = []
    for i in range(len(record_gb)):
        pep = record_gb[i].seq.translate()
        if pep[0] == "M" and not re.search(re.escape("x"), str(pep[0:-1])):
            temp = ProteinAnalysis(pep[0:-1])
            MW.append(temp.molecular_weight())
            indice_ins.append(temp.instability_index())
    df = pd.DataFrame() 
    df ["Peso Molecular"] = MW 
    df ["Indice de inestabilidad"] = indice_ins
    df.to_csv("results/glupeptides.csv")  
    plt.plot(MW, indice_ins, 'o', color='black')
    plt.xlabel('Peso Molecular [Daltons]', fontsize=14)
    plt.ylabel('Indice de Inestabilidad', fontsize=14)
    plt.savefig("results/glupeptides.png") 
