import spacy
import re
from rake_nltk import Rake 
import yake

class KeywordsSummarizer:
    def __init__(self):
        self.tokenizer = spacy.load("en_core_web_md")

    def generate_summary(self, text, lang):
        max_ngram_size = 3
        deduplication_threshold = 0.9
        numOfKeywords = 20
        if lang == "eng":
            language = "en"
        else:
            language = "fr"
        
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(text)
        #text = self.__clean_text(text)
        # doc = self.tokenizer(text)
        # keywords = []
        # ents = doc.ents
        # for i in ents:
        #     if len(i.text)>3 and len(re.findall("\d", i.text))==0:
        #         keywords.append(i.text)
        for i, j in enumerate(keywords):
            keywords[i] = j[0]
        return "\n".join(set(keywords))
    
    def __clean_text(self, text):
        text = re.sub('[^A-zàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ.,!?:\']', ' ', text)
        return text
