(
lambda *_: print(code)
)(
sys := __import__('sys'),
re := __import__('re'),
functools := __import__('functools'),

reserved_words := ['let', 'const', 'function', 'for', 'while', 'if'],
e := lambda msg: [f() for f in [print(f"\u001b[41m fatal \u001b[0m {msg}"), exit(1)]],

code := (lambda f: [f.read(), f.close()][0].replace("\n", "").split(";"))(open(sys.argv[1] if sys.argv[1:] else e("What file do you want to open?"), "r")),

valid_tokens := list("\"(){}+-*/%="),
tokenize_vars := {
    "acc": ""
},
tokenize := lambda line: functools.reduce(lambda a, c: a + c, [x for x in [
    [[j for j in [
         tokenize_vars["acc"] if tokenize_vars["acc"] != 0 else None, x
        ] if j], tokenize_vars.__setitem__("acc", "")][0]
    if x in valid_tokens
    else tokenize_vars.__setitem__("acc", tokenize_vars["acc"] + x)
    for x in list(line)
] if x] + [[
    [tokenize_vars.__getitem__("acc"), tokenize_vars.__setitem__("acc", "")][0]
    ]]),

lex := lambda s: [tokenize(line) for line in s],

a := print(lex(code))

)
