import string

def tokenize(main_string, delimeters={" "},
                          special_tokens={"\\newline",'\n'},
                          split_digits=False):
    """
    Returns a list of tokens delimeted by the strings contained in the
    delimeters set. Punctuation and whitespace characters are treated
    as individual tokens. Delimeters are not counted as tokens.

    Multiple delimeters in a row are counted as a single delimeter.

    string: str
        Some string to be tokenized
    delimeters: set of str
        the delimeters to be used for tokenization
    special_tokens: set of str
        strings that should be treated as individual tokens. Cannot
        contain delimeting characters.
    split_digits: bool
        if true, strings of digits will be split into individual 
        digit tokens 0-9
    """
    tokens = []
    s = ""
    for i,char in enumerate(main_string):
        if s in special_tokens:
            if split_digits and s.isdigit():
                for c in s:
                    tokens.append(c)
            else:
                tokens.append(s)
            s = ""
        
        if char in delimeters:
            if len(s) > 0:
                if split_digits and s.isdigit():
                    for c in s:
                        tokens.append(c)
                else:
                    tokens.append(s)
            s = ""

        elif char.isalnum() or char=="_" or char=="<" or char==">":
            s += char
        elif char in string.whitespace:
            if len(s) > 0:
                if split_digits and s.isdigit():
                    for c in s:
                        tokens.append(c)
                else:
                    tokens.append(s)
            tokens.append(char)
            s = ""
        else:
            if len(s) > 0 and s[-1] != "\\":
                if split_digits and s.isdigit():
                    for c in s:
                        tokens.append(c)
                else:
                    tokens.append(s)
                s = ""
            if char == "\\":
                s += char
            else:
                tokens.append(char)
    if len(s) > 0:
        tokens.append(s)
    return tokens

def group_sentences(document, delimeters={".","!","?"},
                  titles={"dr","mr","mrs","ms","prof"}):
    """
    Groups a document string into a list of sentence strings.
    Sentences are defined by an argued delimeter followed by a
    whitespace character. Handles abbreviations by assuming all
    abbreviations are single, capital characters.

    Input:
        document: str
        delimeters: set of str
            end of sentence characters.
        titles: set of str
            enumerated titles that should be considered.
    Returns:
        sentences: list of str
            a list of all of the sentences in the document.
    """
    sentences = []
    running_s = document[0]
    document = document[1:]
    for i,c in enumerate(document[:-2]):
        running_s += c
        if c in delimeters:
            prob_dec = not document[i+1].isspace()
            other = (not document[i+2].isupper())
            other = other and not document[i-1].isalnum()
            prob_abbrev = document[i-1].isupper()
            prob_title =check_if_title(running_s[:-1],titles)
            if not(prob_dec or prob_abbrev or prob_title or other):
                running_s = running_s.strip()
                if len(running_s) > 0:
                    sentences.append(running_s)
                running_s = ""
    running_s = (running_s+document[-2:]).strip()
    if len(running_s) > 0:
        sentences.append(running_s)
    return sentences

def check_if_title(s, titles):
    """
    A helper function to check if the last word in the string is
    contained within a set of strings.

    s: str
        the string to determine if the last sequence of characters,
        delimeted by whitespace, is in the set `titles`
    titles: set of str
        the titles that need to be compared against
    """
    prob_title = False
    for ws_char in string.whitespace:
        splt = s.strip().split(ws_char)
        idx = -1 if len(splt) > 1 else 0
        title_str = splt[idx].strip().lower()
        prob_title = prob_title or title_str in titles
    return prob_title

def get_sent_arr(document, start_token="<START>",
                           stop_token="<STOP>",
                           delimeters={".","!","?"},
                           titles={"dr","mr","mrs","ms","prof"}):
    """
    Groups a document string into a list of sentence strings and then
    puts them into a matrix with a set sequence length.
    Sentences are defined by an argued delimeter followed by a
    whitespace character. Handles abbreviations by assuming all
    abbreviations are single, capital characters.

    Input:
        document: str
        seq_len: int or None
            if None is argued, the seq_len takes on the value of the
            longest sentence length in the document. Otherwise sentences
            that exceed the seq_len are broken into multiple segments
            each with a start and stop token at the start and end of
            the segments respectively.
        start_token: str
            the token value that should be placed at the beginning of
            each sentence
        stop_token: str
            the token value that should be placed at the end of
            each sentence
        delimeters: set of str
            end of sentence characters.
        titles: set of str
            enumerated titles that should be considered.
    Returns:
        tok_list: list of lists of str
            the result is a 2 dimensional matrix in which each entry in
            the row dimension is a sequence of tokens making up a
            sentence in that row.
    """
    sent_list = group_sentences(document,delimeters=delimeters,
                                         titles=titles)
    tok_list = []
    for i,sent in enumerate(sent_list):
        sent = start_token + " " + sent + " " + stop_token
        toks = tokenize(sent)
        tok_list.append(toks)
    return tok_list

