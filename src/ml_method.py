from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

class MLMethod:
    def __init__(self):
        self.summarizer = TextRankSummarizer()

    def generate_summary(self, text):
        parser = PlaintextParser.from_string(text,Tokenizer("english"))
        
        summary = self.summarizer(parser.document,10)
        text_summary=""

        for sentence in summary:
            text_summary+=str(sentence)

        return text_summary