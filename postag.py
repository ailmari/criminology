from nltk.tag import pos_tag


def extract_NNPs(text):
    tagged = pos_tag(text.split())
    NNPs = [word for word, pos in tagged if pos == 'NNP']

    return NNPs


if __name__ == "__main__":
    # Load some text
    with open('news.txt', 'r', encoding="utf-8") as f:
        sample = f.read()

    names = extract_NNPs(sample)
    print(names)
