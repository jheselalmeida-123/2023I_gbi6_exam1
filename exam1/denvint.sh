N_archivo="denvint.csv"
echo "Archivo, Filas, Columnas" > "$output_file"
Dirección="./data/denvint"
for CSV in "$Dirección"/*.csv; do
Nombrefila=$(basename "$CSV" .csv)
filas=$(awk 'END{print NR}' "$CSV")
columnas=$(awk -F ',' 'NR==1{print NF}' "$CSV")
echo "$Nombrefila" "$filas" "$columnas" >> "$N_archivo"
done

