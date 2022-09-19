# %%
import pandas
import seaborn
import matplotlib.pyplot as plt
import nltk
import glob
import itertools
import collections

# %%
nltk.download("stopwords")
stopwords = nltk.corpus.stopwords.words("english")

# %%
df = pandas.read_csv("out/data.csv.zip", index_col=0)

# %%
df["split"] = df.title.str[-1].str.isdigit()
df["group"] = 0
df.loc[df.split, "group"] = pandas.to_numeric(df[df.split].title.str[-1])
df["is_essay"] = df.title.str.contains("Essays_and_Reviews")
df["is_cultural"] = df.is_essay | df.title.str.contains("On_Opera")
df["lowercase_word"] = df.word.str.lower()

# %%
count_by_tag = (
    df.groupby(by=["title", "tagger", "is_essay", "group", "tag"])
    .count()["word"]
    .unstack()
)
freq_by_tag = count_by_tag.div(count_by_tag.sum(axis=1), axis=0).reset_index()

# %%
seaborn.relplot(
    data=freq_by_tag.melt(["title", "tagger"]),
    x="value",
    y="title",
    hue="tagger",
    col="tag",
    col_wrap=1,
    aspect=3,
    facet_kws={"sharey": True, "sharex": False},
).savefig("out/freq_by_type.pdf")

# %%
freq_by_tag.melt(["title", "tagger", "group", "is_essay"]).groupby(
    ["tag", "title", "group", "is_essay"]
)["value"].aggregate(["min", "median", "mean", "max"]).sort_values(
    ["tag", "median"], ascending=[True, False]
).to_csv(
    "out/freq_by_type.csv"
)

# %%
seaborn.scatterplot(
    data=freq_by_tag,
    x="NOUN",
    y="VERB",
    style="is_essay",
    hue="title",
    palette=seaborn.color_palette("Spectral", 35),
)
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0)
plt.savefig("out/noun_verb.pdf", bbox_inches="tight")

# %%
count_by_tag[["NOUN", "ADJ", "VERB", "ADV"]].div(
    count_by_tag[["NOUN", "ADJ", "VERB", "ADV"]].sum(axis=1), axis=0
).reset_index().melt(["title", "tagger", "group", "is_essay"]).groupby(
    ["title", "group", "is_essay", "tag"]
)[
    "value"
].median().unstack().to_csv(
    "out/freq_by_type_ADJ_ADV_NOUN_VERB.csv"
)


# %%
most_used = (
    df.groupby(["title", "group", "tagger", "tag", "lowercase_word"])
    .count()
    .word.rename("N")
    .reset_index()
    .sort_values(["title", "tag", "tagger", "N"], ascending=[True, True, True, False])
    .groupby(["title", "group", "tagger", "tag"])
    .head(20)
    .reset_index()
)
most_used.to_csv("out/most_used.csv", index=False)

# %%
most_used[["title", "group", "tag", "lowercase_word", "N"]].groupby(
    ["title", "group", "tag", "lowercase_word"]
).max().sort_values(
    ["title", "tag", "N"], ascending=[True, True, False]
).reset_index().to_csv(
    "out/most_used_grouped_by_tagger.csv", index=False
)

# %%
most_used_nosw = (
    df[~df.lowercase_word.isin(stopwords)]
    .groupby(["title", "group", "tagger", "tag", "lowercase_word"])
    .count()
    .word.rename("N")
    .reset_index()
    .sort_values(["title", "tag", "tagger", "N"], ascending=[True, True, True, False])
    .groupby(["title", "group", "tagger", "tag"])
    .head(10)
    .reset_index()
)
most_used_nosw.to_csv("out/most_used_nosw.csv", index=False)

# %%
most_used_nosw[["title", "group", "tag", "lowercase_word", "N"]].groupby(
    ["title", "group", "tag", "lowercase_word"]
).max().sort_values(
    ["title", "tag", "N"], ascending=[True, True, False]
).reset_index().to_csv(
    "out/most_used_nosw_grouped_by_tagger.csv", index=False
)

# %%
df[
    df.lowercase_word.isin(
        df[~df.split][["title", "lowercase_word"]]
        .drop_duplicates()
        .groupby("lowercase_word")
        .count()
        .query("title == 1")
        .query("lowercase_word.str.isalpha()")
        .reset_index()
        .lowercase_word
    )
].query("split == False").groupby(
    ["title", "lowercase_word", "tagger"]
).count().word.rename(
    "N"
).groupby(
    ["title", "lowercase_word"]
).max().reset_index().sort_values(
    ["title", "N"], ascending=[True, False]
).to_csv(
    "out/unique_words.csv", index=False
)

# %%
df[
    df.lowercase_word.isin(
        df[df.split][["title", "lowercase_word"]]
        .drop_duplicates()
        .groupby("lowercase_word")
        .count()
        .query("title == 1")
        .query("lowercase_word.str.isalpha()")
        .reset_index()
        .lowercase_word
    )
].query("split").groupby(["title", "lowercase_word", "tagger"]).count().word.rename(
    "N"
).groupby(
    ["title", "lowercase_word"]
).max().reset_index().sort_values(
    ["title", "N"], ascending=[True, False]
).to_csv(
    "out/unique_words_split.csv", index=False
)
# %%
for i in range(3):
    df[
        ~df.lowercase_word.isin(
            df[(df.group == i) & df.is_essay]
            .lowercase_word.drop_duplicates()
            .where(lambda w: w.str.isalpha())
            .dropna()
        )
    ].query("group == @i and ~is_cultural").groupby(
        ["tagger", "lowercase_word"]
    ).count().word.rename(
        "N"
    ).groupby(
        "lowercase_word"
    ).max().reset_index().query(
        "lowercase_word.str.isalpha() and lowercase_word.str.len() > 2"
    ).sort_values(
        "N", ascending=False
    ).to_csv(
        f"out/not_in_essays_{i}.csv", index=False
    )

# %%
for i in range(3):
    df[
        ~df.lowercase_word.isin(
            df[(df.group == i) & df.is_cultural]
            .lowercase_word.drop_duplicates()
            .where(lambda w: w.str.isalpha())
            .dropna()
        )
    ].query("group == @i and ~is_cultural").groupby(
        ["tagger", "lowercase_word"]
    ).count().word.rename(
        "N"
    ).groupby(
        "lowercase_word"
    ).max().reset_index().query(
        "lowercase_word.str.isalpha() and lowercase_word.str.len() > 2"
    ).sort_values(
        "N", ascending=False
    ).to_csv(
        f"out/not_in_cultural_{i}.csv", index=False
    )

# %%
files = glob.glob("books/txt_clean/*.txt")
texts = {f[16:-4]: open(f).read() for f in files}
titles = texts.keys()
sents = {
    title: [
        len(nltk.tokenize.word_tokenize(sent))
        for sent in nltk.tokenize.sent_tokenize(texts[title])
    ]
    for title in titles
}
# %%
pandas.DataFrame(
    itertools.chain.from_iterable(
        [zip(itertools.repeat(k), v) for k, v in sents.items()]
    ),
    columns=["title", "len"],
).to_csv("out/sent_len.csv", index=False)

# %%
words = {
    title: collections.Counter(
        map(lambda w: w.lower(), nltk.tokenize.word_tokenize(texts[title]))
    ).items()
    for title in titles
}
# %%
word_df = (
    pandas.DataFrame(
        [(k, w, c) for k, count in words.items() for w, c in count],
        columns=["title", "word", "count"],
    )
    .sort_values(["title", "count"], ascending=[True, False])
    .query("word.str.isalpha() and word.str.len() > 2 and word not in @stopwords")
)

# %%
with pandas.ExcelWriter("out/words.xlsx") as writer:
    for t in word_df.title.unique():
        word_df[word_df.title == t].to_excel(writer, sheet_name=t, index=False)

# %%
capital_words = (
    pandas.DataFrame(
        [
            (k, w, c)
            for k, count in {
                title: collections.Counter(
                    filter(
                        lambda w: w[0].isupper(),
                        nltk.tokenize.word_tokenize(texts[title]),
                    )
                ).items()
                for title in titles
            }.items()
            for w, c in count
        ],
        columns=["title", "word", "count"],
    )
    .sort_values(["title", "count"], ascending=[True, False])
    .query("word.str.isalpha()")
)


with pandas.ExcelWriter("out/capital_words.xlsx") as writer:
    for t in capital_words.title.unique():
        capital_words[capital_words.title == t].to_excel(
            writer, sheet_name=t, index=False
        )

# %%
capital_words.query(
    "not(title.str.contains('Essays_and_Reviews') or title.str.contains('On_Opera')) and not title.str[-1].str.isdigit()"
).groupby("word").sum().reset_index().sort_values("count", ascending=False).to_csv(
    "out/capital_no_cultural.csv", index=False
)


# %%
most_used_nosw_all = (
    (
        df.query("word.str.isalpha() and word.str.len() > 2 and word not in @stopwords")
        .groupby(["title", "group", "tagger", "tag", "lowercase_word"])
        .count()
        .word.rename("N")
        .reset_index()
        .sort_values(
            ["title", "tag", "tagger", "N"], ascending=[True, True, True, False]
        )
    )[["title", "group", "tag", "lowercase_word", "N"]]
    .groupby(["title", "group", "tag", "lowercase_word"])
    .max()
    .sort_values(["title", "tag", "N"], ascending=[True, True, False])
    .reset_index()
)

with pandas.ExcelWriter("out/most_used_nosw_grouped_by_tagger_all.xlsx") as writer:
    for t in most_used_nosw_all.title.unique():
        most_used_nosw_all[most_used_nosw_all.title == t].to_excel(
            writer, sheet_name=t, index=False
        )

# %%
most_used_no_essay_nosw = (
    df.query("word.str.isalpha() and word.str.len() > 2 and word not in @stopwords")
    .query("is_cultural == False")
    .groupby(["group", "tagger", "tag", "lowercase_word"])
    .count()
    .word.rename("N")
    .reset_index()
    .groupby(["group", "tag", "lowercase_word"])
    .max()
    .sort_values(["tag", "group", "N"], ascending=[True, True, False])
    .reset_index()[["tag", "group", "lowercase_word", "N"]]
)

with pandas.ExcelWriter("out/most_used_no_cultural_nosw.xlsx") as writer:
    for t in most_used_no_essay_nosw.tag.unique():
        most_used_no_essay_nosw[most_used_no_essay_nosw.tag == t].to_excel(
            writer, sheet_name=t, index=False
        )

# %%
