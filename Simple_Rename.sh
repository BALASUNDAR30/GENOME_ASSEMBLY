#!/bin/bash

# Input/output
input="Vigna_mungo.fasta"
output="evm_proteins_renamed.fasta"

awk '
BEGIN { OFS="\n" }
{
    if ($0 ~ /^>/) {
        # Try to match EVM CP ID
        if (match($0, /(CP[0-9]+\.[0-9]+_RagTag\.[0-9]+)/, m)) {
            print ">" m[1]
        }
        # Try to match contig ID
        else if (match($0, /(contig_[0-9]+\.[0-9]+)/, m)) {
            print ">" m[1]
        }
        # Otherwise, keep header as-is
        else {
            print $0
        }
    } else {
        # Sequence lines
        print $0
    }
}' "$input" > "$output"

echo "✅ FASTA headers simplified and saved to: $output"
