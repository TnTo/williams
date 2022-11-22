# %%
import collections
import glob
import nltk
import pandas

# %%
files = glob.glob("books/txt_clean/*.txt")
texts = {f[16:-4]: open(f).read() for f in files}
titles = texts.keys()

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
capital_words["split"] = capital_words.title.str[-1].str.isdigit()
capital_words["group"] = 0
capital_words.loc[capital_words.split, "group"] = pandas.to_numeric(
    capital_words[capital_words.split].title.str[-1]
)
capital_words["is_essay"] = capital_words.title.str.contains("Essays_and_Reviews")

# %%
with pandas.ExcelWriter("out/capital_words_by_period.xlsx") as writer:
    for t in capital_words.group.sort_values().unique():
        capital_words[capital_words.is_essay & (capital_words.group == t)][
            ["word", "count"]
        ].to_excel(writer, sheet_name=f"essay_{t}", index=False)
        capital_words[(~capital_words.is_essay) & (capital_words.group == t)].groupby(
            "word"
        ).sum().reset_index().sort_values("count", ascending=False)[
            ["word", "count"]
        ].to_excel(
            writer, sheet_name=f"not_essay_{t}", index=False
        )

# %%
with pandas.ExcelWriter("out/names_by_period.xlsx") as writer:
    for t in capital_words.group.sort_values().unique():

        capital_words[
            capital_words.is_essay
            & (capital_words.group == t)
            & capital_words.word.isin(
                pandas.read_excel("in/Authors cited in Essays and Reviews.xlsx").word
            )
        ][["word", "count"]].sort_values(
            ["count", "word"], ascending=[False, True]
        ).to_excel(
            writer, sheet_name=f"essay_{t}", index=False
        )

        capital_words[
            (~capital_words.is_essay)
            & (capital_words.group == t)
            & capital_words.word.isin(
                pandas.read_excel("in/Authors cited in Academic Work.xlsx").word
            )
        ].groupby("word").sum().reset_index().sort_values("count", ascending=False)[
            ["word", "count"]
        ].to_excel(
            writer, sheet_name=f"not_essay_{t}", index=False
        )
