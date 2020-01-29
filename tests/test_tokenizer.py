import tokenizer

strings = [
    "hello here is an easy string",
    "hello here's a slightly harder string",
    "hi ... what's up, this is tough. sup",
    "\\newline, this should be\ndifficult",
    "\\newline, this should be.\ndifficulter",
    "hello\\newlinesup dawg"
]

for s in strings:
    print("\n\n")
    print(s)
    tokens = tokenizer.tokenize(s, special_tokens={"\\newline"})
    print(tokens)
