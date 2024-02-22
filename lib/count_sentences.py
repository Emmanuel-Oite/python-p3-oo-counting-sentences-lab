class MyString:
    def __init__(self):
        # Initialize the value property with an empty string by default
        self.value = ''

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value into sentences based on periods and filter out empty strings
        sentences = [sentence for sentence in self.value.split('.') if sentence.strip()]
        # Return the count of non-empty sentences
        return len(sentences)


