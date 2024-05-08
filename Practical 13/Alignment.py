import blosum as bl    # import necessary libraies
with open("SLC6A4_HUMAN.fa") as fa1:
    for line in fa1:
        line=line.replace('\n','')
        if line.startswith(">"):
            seq_name_human=line[1:]
            seq_human=""
        else:
            seq_human += line.replace('\n','')            # Create "seq_human" to store the sequence of human only
with open("SLC6A4_MOUSE.fa") as fa2:
    for line in fa2:
        line=line.replace('\n','')
        if line.startswith(">"):
            seq_name_mouse=line[1:]
            seq_mouse=""
        else:
            seq_mouse += line.replace('\n','')           # Create "seq_mouse" to store the sequence of mouse only
with open("SLC6A4_RAT.fa") as fa3:
    for line in fa3:
        line=line.replace('\n','')
        if line.startswith(">"):
            seq_name_rat=line[1:]
            seq_rat=""
        else:
            seq_rat += line.replace('\n','')            # Create "seq_rat" to store the sequence of rat only

matrix= bl.BLOSUM(62)         # Use BLOSUM62 to obtain the scores
alignment_score1=0
for i in range(len(seq_human)):
    col_name=seq_human[i]
    index_name=seq_mouse[i]
    alignment_score1 += matrix[col_name][index_name]       # Check the alignment score from the matrix and add it
print("The alignment score for human and mouse sequence is "+str(alignment_score1)+".")

alignment_score2=0
for i in range(len(seq_human)):
    col_name=seq_human[i]
    index_name=seq_rat[i]
    alignment_score2 += matrix[col_name][index_name]  # Check the alignment score from the matrix and add it
print("The alignment score for human and rat sequence is "+str(alignment_score2)+".")

alignment_score3=0
for i in range(len(seq_mouse)):
    col_name=seq_mouse[i]
    index_name=seq_rat[i]
    alignment_score3 += matrix[col_name][index_name]  # Check the alignment score from the matrix and add it
print("The alignment score for mouse and rat sequence is "+str(alignment_score3)+".")

edit_distance1=0
for i in range(len(seq_human)):
    if seq_human[i] != seq_mouse[i]:
        edit_distance1 += 1             # if there is difference, add 1
identical_percentage1 = (len(seq_human)-edit_distance1)/len(seq_human)*100
print("The identical percentage of human and mouse sequence is", identical_percentage1,"%.")

edit_distance2=0
for i in range(len(seq_human)):
    if seq_human[i] != seq_rat[i]:
        edit_distance2 += 1
identical_percentage2 = (len(seq_human)-edit_distance2)/len(seq_human)*100
print("The identical percentage of human and rat sequence is", identical_percentage2,"%.")

edit_distance3=0
for i in range(len(seq_mouse)):
    if seq_mouse[i] != seq_rat[i]:
        edit_distance3 += 1
identical_percentage3 = (len(seq_mouse)-edit_distance3)/len(seq_mouse)*100
print("The identical percentage of mouse and rat sequence is", identical_percentage3,"%.")

#From the results, we can see that the sequence of mouse and the sequence of rat are most closely related
print("The sequence of mouse and the sequence of rat are most closely related.")

#From the results, we can see that the mouse would be a better model organism for studying variation in the SLC6A4 gene in humans, because the mouse has a higher alignment score and more identical amino acids.
print("The mouse would be a better model organism for studying variation in the SLC6A4 gene in humans.")
