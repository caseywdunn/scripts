#!/usr/bin/env python
import sys
from Bio import SeqIO
import re

if __name__ == "__main__":
    records = []
    ids = set()
    for file_name in sys.argv[1:]:
        for record in SeqIO.parse(file_name, "fasta"):
            id = record.id
            taxon = "taxon"
            bracket_match = re.search(r"\[(.+?)\]", record.description)
            if bracket_match!=None:
                taxon=bracket_match.group(1)
            record.name = taxon
            
            # Only add the record if it is new
            if not id in ids:
                ids.add(id)
                records.append(record)
    
    for record in records:
        print(">" + record.name.replace(" ", "_") + "@" + record.id )
        print(str(record.seq))
