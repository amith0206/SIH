import re
import nltk
from nltk.corpus import stopwords
import spacy
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from string import punctuation
from bs4 import BeautifulSoup

#nltk.download('punkt')

# Loading English language model using the full package name
nlp = spacy.load('E:\python311\Lib\site-packages\spacy\en_core_web_sm-3.7.0.tar\en_core_web_sm-3.7.0\en_core_web_sm\en_core_web_sm-3.7.0')

text="If you also want to send a message to someone in Hindi language from mobile, then now it can be done easily.For this, you often surfine fiercely on the Internet, so that options of Hindi keyboard apps can be found.However, typing on the Hindi keyboard has a lot of difficulty.In such a situation, in this report, we are going to tell you about some special keyboard apps, with the help of which you can easily send a text message in Hindi"

def text_cleaning(text):
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'[^\w\s]', '', text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc]
    stop_words = set(stopwords.words('english'))
    cleaned_text = [token for token in tokens if token not in stop_words]
    return cleaned_text

    # stop = stopwords.words('english')
    # punc = list(punctuation)
    # bad_tokens = stop + punc                     #remove because they dont carry any significant meaning
    # lemma = WordNetLemmatizer()                       #reduce complex words to their root form
    # tokens = word_tokenize(text)                     #splitting into individual words or tokens
    # word_tokens = [t for t in tokens if t.isalpha()]
    # clean_token = [lemma.lemmatize(t.lower()) for t in word_tokens if t not in bad_tokens]      #make lower case and check if word in word_tokens and not in bad_tokens
    # return " ".join(clean_token)


newtext=text_cleaning(text)
print(newtext)