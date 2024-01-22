import sys
import bibtexparser
import pandas as pd

#check 3 arguments at least
if not len(sys.argv)==3:
    print("Need more arguments")
elif not sys.argv[1].endswith(".bib"): #check bib file
    print("No bib file specified")
elif not sys.argv[2].endswith(".csv"): #check csv file
    print("No csv file specified")
else:
    # Migrating starts here....
    bibtex_filename=sys.argv[1]
    csv_filename=sys.argv[2]
    with open(bibtex_filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    df = pd.DataFrame(bib_database.entries)
    df.to_csv(csv_filename, index=False)