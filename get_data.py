# %%
import multiprocessing
import itertools
import glob
import pandas
from nltk.tokenize import sent_tokenize

from taggers import AbstractTagger, NLTKPerceptronTagger, SpacyTagger, StanfordTagger

# %%
files = glob.glob("books/txt_clean/*.txt")
texts = {f[16:-4]: open(f).read() for f in files}
titles = texts.keys()

# %%
taggers: dict[str, AbstractTagger] = {
    # "hunpos": NLTKHunposTagger(),
    "spacy": SpacyTagger(),
    "perceptron": NLTKPerceptronTagger(),
    "stanford": StanfordTagger(),
}

# %%
sents = {title: sent_tokenize(texts[title]) for title in titles}

# %%
def tag_text(title, label, tagger, sents):
    print(label, title)
    return [(title, label, w[0], w[1]) for s in sents for w in tagger.tag_sent(s)]


# %%
with multiprocessing.Pool(processes=4) as pool:
    data = pool.starmap(
        tag_text,
        [
            (i[1], i[0][0], i[0][1], sents[i[1]])
            for i in itertools.product(taggers.items(), titles)
        ],
    )

# %%
df = pandas.DataFrame(itertools.chain(*data))
df.columns = ["title", "tagger", "word", "tag"]
df = df[df.tag != "SPACE"]

# %%
df.to_csv("data.csv.zip")

# %%
count_by_tag = df.groupby(by=["title", "tagger", "tag"]).count().unstack()
freq_by_tag = count_by_tag.div(count_by_tag.sum(axis=1), axis=0)

# %%
freq_by_tag.to_csv("out/freq.csv")
# %%
