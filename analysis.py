# %%
import pandas
import seaborn

# %%
df = (
    pandas.read_csv("freq.csv", index_col=[0, 1], skiprows=[0, 2])
    .reset_index()
    .rename(columns={"tag": "title", "level_1": "tagger"})
)

# %%
seaborn.relplot(
    data=df.melt(["title", "tagger"])
    x="value",
    y="title",
    hue="tagger",
    col="variable",
    col_wrap=1,
    aspect=3,
    facet_kws={"sharey": True, "sharex": False},
).savefig("out/freq_by_type.pdf")

# %%
df.melt(["title", "tagger"]).groupby(["variable", "title"])["value"].aggregate(
    ["min", "median", "mean", "max"]
).sort_values(["variable", "median"], ascending=[True, False]).to_csv("out/freq_by_type.csv")

# %%
df2 = pandas.read_csv("data.csv.zip")

# %%
df2.groupby(["title", "tagger", "tag", "word"]).count().sort_values(
    ["title", "tag", "tagger", "Unnamed: 0"], ascending=[True, True, True, False]
).groupby(["title", "tagger", "tag"]).head(20).reset_index(drop=False).to_csv("out/most_used.csv", index=False)
# %%
df2['splitted'] = df2.title.str[-1].str.isdigit()
df2['is_essay'] = (df2.title == 'Essays_and_Reviews')
# %%
df_books = df2[~df2.splitted].groupby(['title', 'word']).count()["Unnamed: 0"].rename("N").reset_index(drop=False)
df_unique = df_books.merge(df_books.groupby('word').count().query('title == 1').reset_index(), on='word')[['word', 'title_x', 'N_x']].sort_values(['title_x', 'N_x'], ascending=[True, False])
df_unique[df_unique.word.str.isalpha()].to_csv('out/unique_words.csv', index=False)

# %%
df_essays = df2[~df2.splitted].groupby(['is_essay', 'word']).count()["Unnamed: 0"].rename("N").reset_index(drop=False)
df_not_in_essays = df_essays[~df_essays.is_essay]
df_not_in_essays = df_not_in_essays[df_not_in_essays.word.isin(pandas.merge(df_essays, df_essays[df_essays.is_essay], on='word', how='left').groupby('word').count().query("N_x == 1").reset_index(drop=False).word)].sort_values("N", ascending=False)
df_not_in_essays[df_not_in_essays.word.str.isalpha()].to_csv('out/not_in_essays.csv', index=False, header=False)
# %%
