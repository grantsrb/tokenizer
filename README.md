# Tokenizer
A lightweight tokenizer with a fair degree of flexibility.

# Features
* `tokenize`: From a single string, creates a list of tokens delimeted by a custom set of characters. Delimeters are not counted as tokens. Punctuation and whitespace characters are treated as individual tokens. Default delimeter is a single space
* `group_sentences`: From a single string, creates a list of sentences delimeted by a custom set of characters. Sentences are defined by the delimeter followed by a whitespace character. Handles abbreviations by assuming all abbreviations are single, capital characters. Handles titles by enumerating the possible titles of interest.

# Setup
Open a terminal session and type the following:
```
    $ git clone https://github.com/grantsrb/tokenizer
    $ cd tokenizer
    $ pip3 install --user -e .
```
