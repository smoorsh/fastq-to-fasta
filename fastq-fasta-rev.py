import sys

#### convert fastq to fasta and create a reverse complement ####

##### User defined variables #####
## input format: python complement.py /path/to/fastq/file /name/and/destination/of/fasta/file /name/and/destination/of/reverse/file

fastq_input = sys.argv[1]
fastaf = sys.argv[2]
fastar = sys.argv[3]

##### User defined functions #####
def complement(line):
    new_transcript = ''
    for base in line:
        if (base.find('N') != -1):
            new_transcript += 'N'
        else:
            new_transcript += (reverse_comp[base])
    return(new_transcript)

#### open and read fastq file and make it into a fasta file

newline = '\n'
line_count = 0
with open(fastq_input, 'r') as infile, open(fastaf, 'w') as outfile:
    lines = infile.readlines()
    for line in lines:
        line = line.rstrip('\n')
        fasta_line = line.replace("@", ">")
        line_count += 1
        if line_count %4 != 3 and line_count %4 !=0:
            outfile.write(fasta_line + newline)


#### create a reverse complement of every other line and place it into a new file

# use a dictionary to store the complements
reverse_comp = {"A":"T", "T":"A", "C":"G", "G":"C", "N":"N"}

with open(fastaf, 'r') as fastain, open(fastar, 'w') as fastaout:
    lines = fastain.readlines()
    for line in lines:
        line = line.rstrip('\n')
        newline = '\n'
        if line[0] == '>':
            fastaout.write(line + newline)
        else:
            reverse = complement(line)
            fastaout.write(reverse + newline)

## close files
fastain.close()
fastaout.close()