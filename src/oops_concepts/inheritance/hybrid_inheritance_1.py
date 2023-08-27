class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        self.tokens = text.split() # Splitting the Words


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        super().__init__(text)
        self.word_count = len(self.tokens) # Getting the token counts


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        super().__init__(text)
        self.vocab = set(self.tokens) # Getting the unique tokens


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        super().__init__(text)



if __name__=="__main__":
    td = TextDescriber('row row row your boat')

    print(f'Words:{td.tokens}')
    print('--------------------')
    print(f'Unique Words:{td.vocab}')
    print('---------------------')
    print(f'Total Word Count:{td.word_count}')