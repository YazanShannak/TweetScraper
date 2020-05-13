import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def parse_hashtags_mentions(text):
    hashtags = re.findall('#\w+', text)
    hashtags = [hashtag[1:].lower() for hashtag in hashtags]
    mentions = re.findall("@\w+", text)
    mentions = [mention[1:] for mention in mentions]
    words = text.split(" ")
    clean_text = " ".join([word for word in words if len(word) > 0 and not word.startswith("#") and not word.startswith("@")])
    clean_text = "".join(re.findall("[\w\s]", clean_text))
    clean_text = re.sub("\s{2,}", " ", clean_text)
    return clean_text, hashtags, mentions

def clean_text(text:str) -> str:
    text, _, _  = parse_hashtags_mentions(text)
    image_clean = re.sub("pic.[\w/.]+", "", text)
    punctionation_clean = re.sub("""[!?.'"-]""", "", image_clean)
    numbers_clean = re.sub("\d", "", punctionation_clean)
    skip_clean = re.sub("\\n|\\t", " ", numbers_clean)
    link_clean = re.sub("https.+", "", skip_clean)
    return link_clean.lower()

def clean_stopwords(text:str) -> str:
    stop_words = stopwords.words("english")
    tokens = text.split(" ")
    clean = [token for token in tokens if token not in stop_words]
    return " ".join(clean)

def stem_tweet(text:str) -> str:
    stemmer = PorterStemmer()
    tokens = text.split(" ")
    stemmed = [stemmer.stem(token) for token in tokens]
    return " ".join(stemmed)

def process_all_text(text:str)->str:
    clean = clean_text(text)
    return clean_stopwords(clean)

def get_polarity(text:str) -> float:
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)