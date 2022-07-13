from abc import ABC, abstractmethod
import os

import nltk
import spacy
from stanfordcorenlp import StanfordCoreNLP


class AbstractTagger(ABC):
    @abstractmethod
    def tag_sent(self, sent: str) -> list[tuple[str, str]]:
        pass


class NLTKTagger(AbstractTagger, ABC):
    def __init__(self) -> None:
        nltk.download("punkt")
        nltk.download("universal_tagset")

    def tag_sent(self, sent: str) -> list[tuple[str, str]]:
        return [
            w
            for w in nltk.tag._pos_tag(
                nltk.tokenize.word_tokenize(sent), "universal", self.tagger, "eng"
            )
        ]


class NLTKPerceptronTagger(NLTKTagger):
    def __init__(self) -> None:
        super().__init__()
        nltk.download("averaged_perceptron_tagger")
        self.tagger = nltk.tag.perceptron.PerceptronTagger()


class NLTKHunposTagger(NLTKTagger):  # Not working without hunpos binary
    def __init__(self) -> None:
        super().__init__()
        os.system(
            "mkdir -p data && cd data && if [ ! -f en_wsj.model ] && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/hunpos/en_wsj.model.gz && gzip -d en_wsj.model.gz"
        )
        self.tagger = nltk.tag.hunpos.HunposTagger("data/en_wsj.model")


class SpacyTagger(AbstractTagger):

    mapping = {
        "NUM": "NUM",
        "DET": "DET",
        "NOUN": "NOUN",
        "ADP": "ADP",
        "SPACE": "SPACE",
        "PROPN": "NOUN",
        "VERB": "VERB",
        "SCONJ": "CONJ",
        "AUX": "VERB",
        "PART": "PRT",
        "PRON": "PRON",
        "ADJ": "ADJ",
        "PUNCT": ".",
        "CCONJ": "CONJ",
        "X": "X",
        "ADV": "ADV",
        "SYM": "X",
        "INTJ": "PRT",
    }

    def __init__(self) -> None:
        try:
            self.tagger = spacy.load("en_core_web_lg")
        except:
            spacy.cli.download("en_core_web_lg")
            self.tagger = spacy.load("en_core_web_lg")

    def tag_sent(self, sent: str) -> list[tuple[str, str]]:
        return [(w.text, self.mapping[w.pos_]) for w in self.tagger(sent)]


class StanfordTagger(AbstractTagger):
    def __init__(self) -> None:
        os.system(
            "cd data && [ ! -f stanford-corenlp-latest.zip ] && wget https://huggingface.co/stanfordnlp/CoreNLP/resolve/main/stanford-corenlp-latest.zip && unzip stanford-corenlp-latest"
        )
        self.nlp = StanfordCoreNLP(r"data/stanford-corenlp-4.4.0")

    def tag_sent(self, sent: str) -> list[tuple[str, str]]:
        return [
            (word, nltk.tag.mapping.map_tag("en-ptb", "universal", tag))
            for (word, tag) in self.nlp.pos_tag(sent)
        ]
