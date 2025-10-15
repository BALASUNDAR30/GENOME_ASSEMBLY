#!/bin/bash

# Input/output
input_fasta="evm_proteins_renamed.fasta"
output_fasta="evm_proteins_renamed_Final.fasta"
mapping_csv="protein_name_mapping.csv"

# Initialize CSV
echo "Old_Name,New_Name" > "$mapping_csv"

awk -v csv="$mapping_csv" '
BEGIN {
    # Chromosome mapping
    chrom["CP144700.1"]="Chr01"
    chrom["CP144699.1"]="Chr02"
    chrom["CP144698.1"]="Chr03"
    chrom["CP144697.1"]="Chr04"
    chrom["CP144696.1"]="Chr05"
    chrom["CP144695.1"]="Chr06"
    chrom["CP144694.1"]="Chr07"
    chrom["CP144693.1"]="Chr08"
    chrom["CP144692.1"]="Chr09"
    chrom["CP144691.1"]="Chr10"
    chrom["CP144690.1"]="Chr11"
    chrom["CP144689.1"]="Chr12"
    chrom["CP144701.1"]="MT"
    chrom["CP144688.1"]="Pltd"
}
{
    if ($0 ~ /^>/) {
        # Match CP IDs
        if (match($0, /(CP[0-9]+\.[0-9]+)_RagTag\.([0-9]+)/, m)) {
            ref = m[1]
            num = sprintf("%06d", m[2])
            chr = chrom[ref]
            if (chr == "") {
                newname = "VmUnkG" num
            } else if (chr == "MT") {
                newname = "VmMtG" num
            } else if (chr == "Pltd") {
                newname = "VmPltG" num
            } else {
                newname = "Vm" chr "G" num
            }
            print ">" newname
            print ref "_RagTag." m[2] "," newname >> csv
        }
        # Match contigs
        else if (match($0, /(contig_[0-9]+)\.([0-9]+)/, c)) {
            contig = c[1]
            num = sprintf("%06d", c[2])
            newname = "VmUnkG" num
            print ">" newname
            print contig "." c[2] "," newname >> csv
        }
        else {
            # Keep header as-is if no match
            print $0
        }
    } else {
        # Sequence lines
        print $0
    }
}' "$input_fasta" > "$output_fasta"

echo "✅ Renaming complete!"
echo "Output FASTA: $output_fasta"
echo "Mapping CSV: $mapping_csv"
