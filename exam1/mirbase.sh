 
echo "Número de artículos hasta la fecha:" `grep -c "PUBMED" miRNA.dat.gz`
echo "Número de estudios en Nature:" `grep -c "Nature" miRNA.dat.gz`
echo "Número de organismo elegans usado:" `grep -c "elegans" miRNA.dat.gz`
echo "Número de micro RNA estudiados:" `grep -c "139 BP" miRNA.dat.gz` 
