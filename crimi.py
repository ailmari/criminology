import pandas as pd
from nltk.tag import pos_tag


def extract_NNPs(text):
    tagged = pos_tag(text.split())
    NNPs = [word for word, pos in tagged if pos == 'NNP']

    return NNPs


if __name__ == "__main__":
    # Broken, fix read_csv arguments (http://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options)
    df = pd.read_csv('panamapapers/Officers.csv')
    names = df.name

    #Load some text
    with open('article.txt', 'r', encoding="utf-8") as f:
        sample = f.read()

    #names = extract_NNPs(sample)
    print(sample)
