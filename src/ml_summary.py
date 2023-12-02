from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


class MLSummary:
    def __init__(self):
        self.summarizer = TextRankSummarizer()

    def generate_summary(self, text, lang):
        if lang == "eng":
            parser = PlaintextParser.from_string(text, Tokenizer("english"))
        else:
            parser = PlaintextParser.from_string(text, Tokenizer("french"))

        summary = self.summarizer(parser.document, 5)
        text_summary = ""

        for sentence in summary:
            text_summary += str(sentence)

        return text_summary
