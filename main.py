(
lambda *_: 0
)(
sys := __import__('sys'),
re := __import__('re'),
functools := __import__('functools'),

e := lambda msg: [f() for f in [print(f"\u001b[41m fatal \u001b[0m {msg}"), exit(1)]],
remove_falsy := lambda iterable: [x for x in iterable if x],

code := (lambda f: [f.read(), f.close()][0].replace("\n", "").split(";"))(open(sys.argv[1] if sys.argv[1:] else e("What file do you want to open?"), "r")),

valid_tokens := list('"(){}+-*/%= '),
tokenize_vars := {
    "acc": "",
    "is_in_string": False
},
tokenize := lambda line: [token for token in functools.reduce(lambda a, c: a + c, remove_falsy([
    [[[
        j for j in [
            tokenize_vars["acc"].strip() if tokenize_vars["acc"] != "" else None, x
        ] if j], tokenize_vars.__setitem__("acc", "")][0]

    if x in valid_tokens and not tokenize_vars.__getitem__("is_in_string") or (tokenize_vars.__getitem__("is_in_string") and x == '"')
    else tokenize_vars.__setitem__("acc", tokenize_vars["acc"] + x),

    tokenize_vars.__setitem__("is_in_string", not tokenize_vars["is_in_string"]) if x == '"' else 0]

    [0] for x in list(line)
]) + [[
    [tokenize_vars.__getitem__("acc"), tokenize_vars.__setitem__("acc", ""), tokenize_vars.__setitem__("is_in_string", False)][0]
    ]]) if token != " "],

lex := lambda s: [tokenize(line) for line in s],

a := [print(",".join(l)) for l in lex(code)]


)
