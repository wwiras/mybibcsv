import sys
import bibtexparser
import pandas as pd

if not len(sys.argv)==3:
    print("Need more arguments")
elif not sys.argv[1].endswith(".bib"):
    print("No bib file specified")
elif not sys.argv[2].endswith(".csv"):
    print("No csv file specified")
else:
    # for n,arg in enumerate(sys.argv):
    #     print(n,arg)
    bibtex_filename=sys.argv[1]
    csv_filename=sys.argv[2]
    with open(bibtex_filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    df = pd.DataFrame(bib_database.entries)
    df.to_csv(csv_filename, index=False)


# with open('ref.bib') as bibtex_file:
#   bib_database = bibtexparser.load(bibtex_file)
# df = pd.DataFrame(bib_database.entries)
# df.to_csv('ref.csv', index=False)