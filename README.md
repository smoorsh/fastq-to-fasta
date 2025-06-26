# fastq-to-fasta
A python script that takes a FASTQ file and creates a FASTA file as well as a reverse complement FASTA.

## Introduction
This python script takes a FASTQ-formatted forward-read DNA file and creates a FASTA formatted DNA file using those reads. Then, it creates a reverse complement of the FASTA file, also in FASTA format.

## Download Instructions
Use the following command line to download the GitHub repository:

```
git clone https://github.com/smoorsh/fastq-to-fasta.git
```
## Usage Instructions
After downloading the repository, change to the repository directory:
```
cd fastq-to-fasta
```
Run the program:
```
python complement.py /path/to/fastq/file /name/and/path/to/forward/fasta/file /name/and/path/to/reverse/fasta/file
```
Be sure to change all file paths to match your own file paths to your input FASTQ file, as well as to the destination and desired name for your FASTA files.
