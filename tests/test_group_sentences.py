import tokenizer

strings = [
    "hello here is an easy string. How are you today?",
    "\n\nWhat's up dawg? I am so happy! Today I turn 8.\n\n",
    "We need a sentence with some newlines.\n\nWhat's up dawg?",
    "hi ... what's up, this is tough. sup",
    "\\newline, this should be\ndifficult. Right?",
    "\\newline, this should be.\ndifficulter. right righto!",
    "hi\nProf. hello here's a slightly harder string, Dr. Grant. Dr. grant.",
    "hi\n\nprof. kindle, how are yo? Mrs. windsy, here's a slightly harder string, Dr. Grant. Dr. grant.\n\nprof. kindle, how are you?",
    ]

for s in strings:
    print("\n\n")
    print(s)
    sentences = tokenizer.group_sentences(s)
    print(sentences)
