seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
repeat1 = 'GTGTGT'
repeat2 = 'GTCTGT'
count1 = 0         # Create a new variable to count the duplicated times
count2 = 0
for i in range(len(seq) - 5):
    if seq[i:i+6] == repeat1:       # match the sequence and the repeated sequence required
        count1 += 1                 # If they match, the count will add +1
for i in range(len(seq) - 5):
    if seq[i:i+6] == repeat2:
        count2 += 1
repeat_total=count1+count2          # The final result is the sum of the two
print(repeat_total)