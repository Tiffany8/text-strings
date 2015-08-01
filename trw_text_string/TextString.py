 #!/usr/bin/python
 # coding= utf8

""" This module describes the class TextString."""

import re

__version__ = '0.0.4'

class TextString(object):
    """TextString class creates instances of text string objects for the
    purpose of retrieving bigrams (or word pairs) that occur more than
    once in the string."""

    def __init__(self, string):
        """Constructor for this TextString class."""

        confirmed_string = self._string_confirmation(string)
        self.string = confirmed_string

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<TextString string: %s>" % (self.string)

    def get_word_pairs(self):
        """
        Prints out pairs of bigrams with instances greater than two.

        Returns:
            Print a list of triplets. Each triplet is a pair of words and
            a count, and returns the list of word pairs with occurance.

        Example(s):
            >>> text_string_object = TextString("Is this? This is; indeed.")
            >>> text_string_object.get_word_pairs()
            is, this: 2

            >>> text_string_object = TextString("5")
            >>> text_string_object.get_word_pairs()
            No word pairs occured more than once.

            Not optimized to recognize characters outside of ordinal range(128)
            >>> text_string_object = TextString("Is Università a place? A place. Università is.")
            >>> text_string_object.get_word_pairs()
            a, place: 2
            is, universit: 2
        """

        string = self.string
        sentence_list = self._tokenize_sentences(string)
        word_pair_dict = {}
        for sentence in sentence_list:
            word_list = self._tokenize_words(sentence)
            word_pair_dict = self._create_word_pairs(word_list, word_pair_dict)

        word_pair_list = self._word_pair_instance_more_than_one(word_pair_dict)
        self._print_word_pair_list(word_pair_list)

    @staticmethod
    def _string_confirmation(astring):
        """
        Confirm that input is a string.

        Args:
            astring (string): String from which word pairs will be generated.

        Return:
            If astring is a string, then returns that string, else, an error is
            raised.

        Example(s):
            >>> TextString._string_confirmation("Is this? This is, indeed.")
            'Is this? This is, indeed.'

            >>> TextString._string_confirmation(5)
            Input should be a string.
        """

        try:
            astring.split()
        except AttributeError:
            print "Input should be a string."
        else:
            return astring

    @staticmethod
    def _tokenize_sentences(astring):
        """
        Splits string into lists of sentences based on punctuation.

        Args:
            astring (string): String from which word pairs will be generated.

        Return:
            Returns a list of sentences.

        Example(s):
            >>> TextString._tokenize_sentences("Is this? This is, indeed.")
            ['Is this?', 'This is, indeed.']

            >>> TextString._tokenize_sentences("Is this, this is, indeed.")
            ['Is this, this is, indeed.']
        """
        regex_pattern = re.compile(r'([a-zA-ZÀ-ÿ][^\.!?]*[\.!?])', re.M)
        sentence_list = regex_pattern.findall(astring)
        # print "sentence tokenizer: ", sentence_list
        return sentence_list

    @staticmethod
    def _strip_punctuation(astring):
        """
        Strip string of punctuation.

        Args:
            astring (string): A string, in this case, consisting of one sentence.

        Returns:
            Returns a string without sans punctuation.

        Example(s):
            >>> astring = "Is this, this is, indeed."
            >>> TextString._strip_punctuation(astring)
            'Is this this is indeed'

            >>> astring = "Is this"
            >>> TextString._strip_punctuation(astring)
            'Is this'
        """

        string_no_punctuation = re.sub(ur"[^\w\d'\s]+", '', astring)
        # print "stripped punc: ", string_no_punctuation
        return string_no_punctuation

    @staticmethod
    def _tokenize_words(one_sentence_string):
        """
        Strips a sentence of punctuation and splits into a list of words.

        Args:
            one_sentence_string (string): A string comprised of one sentence.

        Returns:
            Returns a list of the words in the sentence sans punctuation.

        Example(s):
            >>> TextString._tokenize_words("This is, indeed.")
            ['This', 'is', 'indeed']
        """

        string_no_punctuation = TextString._strip_punctuation(one_sentence_string)
        word_list = string_no_punctuation.split()
        # print "word tokenizer: ", word_list
        return word_list

    @staticmethod
    def _create_word_pairs(word_list, word_pair_dict):
        """
        Iterate through sentence word list and add bigrams as
        a tuple to the dictionary with bigram instances as value.

        Args:
            word_list (list): list of words from a sentence
            word_pair_dict (dictionary): dictionary to which bigrams are added

        Returns:
            Returns a dictionary consisting of bigrams in a tuple as keys and
            number of instances as values.

        Example(s):
            >>> word_list = ["This", "is", "indeed"]
            >>> word_pair_dict = {}
            >>> TextString._create_word_pairs(word_list, word_pair_dict)
            {('this', 'is'): 1, ('is', 'indeed'): 1}
        """

        for index in range(len(word_list) - 1):
            word_pair = (word_list[index].lower(), word_list[index + 1].lower())
            word_pair_rev = (word_list[index + 1].lower(), word_list[index].lower())
            if word_pair_dict.get(word_pair):
                word_pair_dict[word_pair] = word_pair_dict.get(word_pair, 0) + 1
            elif word_pair_dict.get(word_pair_rev):
                word_pair_dict[word_pair_rev] = word_pair_dict.get(word_pair_rev, 0) + 1
            else:
                word_pair_dict[word_pair] = 1

        return word_pair_dict

    @staticmethod
    def _word_pair_instance_more_than_one(word_pair_dict):
        """
        Iterate through dictionary items and append word pairs
        where key value is greater than 1 to a list.

        Args:
            word_pair_dict (dictionary): Dictionary with key value pairs of bigram
            tuples and number of instances, respectively.

        Returns:
            If there are instances of bigrams that occur >1, a list tuples of
            those bigrams and their instance is returned.

        Example(s):
            >>> word_pair_dict = {('this', 'is'): 1, ('is', 'indeed'): 1}
            >>> TextString._word_pair_instance_more_than_one(word_pair_dict)
            []

            >>> word_pair_dict = {('this', 'is'): 1, ('is', 'indeed'): 2}
            >>> TextString._word_pair_instance_more_than_one(word_pair_dict)
            [(('is', 'indeed'), 2)]
        """
        word_pair_list = []
        for word_pair in word_pair_dict.items():
            if word_pair[1] > 1:
                word_pair_list.append(word_pair)
        return word_pair_list

    @staticmethod
    def _print_word_pair_list(word_pair_list):
        """
        Print the word pair list with instances greater than 1 to console.

        Args:
            word_pair_list (list): list of tuples consisting of tuple of bigram
            and the number of instances

        Returns:
            Prints out the bigrams with instance number.

        Example(s):
            >>> word_pair_list = [(('is', 'indeed'), 2)]
            >>> TextString._print_word_pair_list(word_pair_list)
            is, indeed: 2

            >>> word_pair_list = []
            >>> TextString._print_word_pair_list(word_pair_list)
            No word pairs occured more than once.
        """
        if word_pair_list:
            for word_pair in word_pair_list:
                print "%s: %d" % (", ".join(word_pair[0]), word_pair[1])
        else:
            print "No word pairs occured more than once."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
