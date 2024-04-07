import re
user_repeat = input("Enter the duplicated sequence you want to explore（'GTGTGT' or 'GTCTGT'）: ") # Ask the user to input duplicated sequence
output_filename = f"{user_repeat}_duplicate_genes.fa"        # Create the new file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as a:      # Read the original file
    lines = a.readlines()

with open(output_filename, 'w') as out:        # Write the output file
    gene = False             # Flag
    current_gene_name = None
    current_gene_sequence = ""        # Initialize the variables

    for line in lines:
        if line.startswith(">"):
            if gene and current_gene_name:   # If a gene is already being processed, output the information of the previous gene
                repeat_count = current_gene_sequence.count(user_repeat)      # Calculate the number of duplicated gene
                out.write(f">{current_gene_name} \n")    # Output the gene name on the first line
                out.write(f"{repeat_count}  {current_gene_sequence} \n")  # Output the duplicated times and the original DNA sequence
            gene = True          # Start the next gene (flag)
            current_gene_name = line.strip()[1:].split(' ')[0]     # Read the gene name (delete ">") 
            current_gene_sequence = ""
        else:
            if gene:                  #If it is not the start of a new gene, it is the sequence content
                current_gene_sequence += line.strip()        # Output the sequences
print(f" {output_filename} is the file you want")