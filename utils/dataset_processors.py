import numpy as np
import pandas as pd
import re
import csv
import preprocessor as p
import sys

csv.field_size_limit(sys.maxsize)

def preprocess_text(sentence):
    # remove hyperlinks, hashtags, smileys, emojies
    sentence = p.clean(sentence)
    # Remove hyperlinks
    sentence = re.sub(r"http\S+", " ", sentence)
    # Remove punctuations and numbers
    # sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    # sentence = re.sub('[^a-zA-Z.?!,]', ' ', sentence)
    # Single character removal (except I)
    # sentence = re.sub(r"\s+[a-zA-HJ-Z]\s+", ' ', sentence)
    # Removing multiple spaces
    sentence = re.sub(r"\s+", " ", sentence)
    sentence = re.sub(r"\|\|\|", " ", sentence)

    return sentence

def load_reddit_df(datafile):
    with open(datafile, "rt", encoding="utf-8") as csvf:
        csvreader = csv.reader(csvf, delimiter=",", quotechar='"')
        first_line = True
        df = pd.DataFrame(columns=["user", "text", "E", "N", "F", "J"])
        for line in csvreader:
            if first_line:
                first_line = False
                continue

            text = line[1]

            df = df.append(
                {
                    "user": line[3],
                    "text": text,
                    "E": 1 if line[0][0] == "E" else 0,
                    "N": 1 if line[0][1] == "N" else 0,
                    "F": 1 if line[0][2] == "F" else 0,
                    "J": 1 if line[0][3] == "J" else 0,
                },
                ignore_index=True,
            )

    print("E : ", df["E"].value_counts())
    print("N : ", df["N"].value_counts())
    print("F : ", df["F"].value_counts())
    print("J : ", df["J"].value_counts())
    
    print("Length of df:", len(df))
    return df


def reddit_embeddings(datafile, tokenizer, token_length):
    targets = []
    token_len = []
    input_ids = []
    author_ids = []
    total_skipped = 0

    df = load_reddit_df(datafile)
    cnt = 0
    for ind in df.index:

        text = preprocess_text(df["text"][ind])
        tokens = tokenizer.tokenize(text)
        if(len(tokens) == 0): continue

        token_len.append(len(tokens))
        token_ids = tokenizer.encode(
            tokens,
            add_special_tokens=True,
            max_length=token_length,
            padding='longest',
            truncation=True
        )
        if(len(token_ids) != token_length):
            total_skipped += 1
            continue

        input_ids.append(token_ids)
        targets.append([df["E"][ind], df["N"][ind], df["F"][ind], df["J"][ind]])
        author_ids.append(int(df["user"][ind]))
        cnt += 1
    print(f"Skipped total: {total_skipped}")
    print(f"Total dataset length: {cnt}")
    print("average length : ", int(np.mean(token_len)))
    author_ids = np.array(author_ids)

    return author_ids, input_ids, targets
