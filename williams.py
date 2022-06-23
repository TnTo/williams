# %%
from itertools import count
import nltk
import glob
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas

# %%
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("universal_tagset")

# %%
def pos_tag_sents(sentences, tagger, tagset="universal"):
    lang = "eng"
    return [nltk.tag._pos_tag(sent, tagset, tagger, lang) for sent in sentences]

# %%
def mean(list):
    return sum(list) / len(list)


def is_adj(w):
    return "ADJ" == w[1]


# %%
files = glob.glob("books/txt_clean/*.txt")
texts = {f[16:-4]: open(f).read() for f in files}
titles = texts.keys()

# %%
words = {
    title: [word_tokenize(s) for s in sent_tokenize(texts[title])] for title in titles
}

# %%
tagger = nltk.tag.perceptron.PerceptronTagger()
tags = {title: pos_tag_sents(words[title], tagger) for title in titles}

# %%
flatten_tags = {title: [w for s in tags[title] for w in s] for title in titles}


# %%
adj = {title: mean([is_adj(w) for w in flatten_tags[title]]) for title in flatten_tags}

# %%
pandas.DataFrame.from_dict(adj, orient="index").sort_values(by=0).plot(
    kind="line", rot=90, xticks=range(0, 11)
)
# %%
adj_num = {
    title: sum([is_adj(w) for w in flatten_tags[title]]) for title in flatten_tags
}
adj_count = {
    title: len(set([w[0] for w in flatten_tags[title] if is_adj(w)]))
    for title in flatten_tags
}

# %%
length = {title: len([w[0] for w in flatten_tags[title]]) for title in flatten_tags}
length_unique = {
    title: len(set([w[0] for w in flatten_tags[title]])) for title in flatten_tags
}
# %%
df = pandas.concat(
    [
        # pandas.DataFrame.from_dict(adj, orient="index", columns=["mean-#adj/#tot"]),
        pandas.DataFrame.from_dict(adj_num, orient="index", columns=["#adj"]),
        pandas.DataFrame.from_dict(adj_count, orient="index", columns=["#adjU"]),
        pandas.DataFrame.from_dict(length, orient="index", columns=["#tot"]),
        pandas.DataFrame.from_dict(length_unique, orient="index", columns=["#totU"]),
    ],
    axis=1,
)
df["#adj/#tot"] = df["#adj"] / df["#tot"]
df["#adjU/#totU"] = df["#adjU"] / df["#totU"]
df["#tot/#totU"] = df["#tot"] / df["#totU"]
df["#adj/#adjU"] = df["#adj"] / df["#adjU"]

# %%
tabellone = pandas.DataFrame(
    [(title, w[0], w[1]) for title in titles for s in tags[title] for w in s]
)

# %%
count_by_tag = tabellone.groupby(by=[0, 2]).count().unstack()
count_by_tag = count_by_tag.div(count_by_tag.sum(axis=1), axis=0)

# %%
filtered = (
    tabellone[tabellone[2].isin(["ADJ", "ADV", "CONJ", "NOUN", "VERB"])]
    .groupby(by=[0, 2])
    .count()
    .unstack()
)”  NOUN     557
                           NUM        4
                           PRON       1
                           VERB     131
filtered = filtered.div(filtered.sum(axis=1), axis=0)
filtered.columns = [c[1] for c in filtered.columns]

# %%
tabellone.groupby(by=[0, 1, 2]).size()
# %%
