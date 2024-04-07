with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as input, open("duplicate_genes.fa", "w") as output:
    duplication = False         # Flag
    gene_description = ""           # Initialize the variable
    for line in input:
        if line.startswith('>'):       # ">" is the signal of a gene name
            if "duplication" in line:
                duplication = True   # Change the flag
                gene_description = line   # get the gene description
                gene_name = line.strip()[1:].split(' ')[0]   # Read the gene name (delete ">")
                output.write(f">{gene_name}\n")
            else:
                duplication = False      # if duplication is not in the gene description, ignore it (skip)
                gene_description = ""
        elif duplication:         # Output the sequence
            output.write(line)  