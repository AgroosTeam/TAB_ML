from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import nltk
nltk.download('stopwords')


class TextCleaner:
    @staticmethod
    def clear_text(text):
        # Remove all not utf-8 symbols from text
        result = str(text).encode(
            'utf-8', errors='ignore'
        ).decode('utf-8')

        text = re.sub('[^a-zA-Z]', ' ', result)
        text = text.lower()
        text = text.split()
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        text = [ps.stem(word) for word in text if word not in set(all_stopwords)]
        text = ' '.join(text)
        return text
