# fuzz.py
# This file fuzzes KubeSec-master

import parser

def fuzzValues():
    unexpected_inputs = [1, "abc", True, "/", "./environment.yml"]
    for input in unexpected_inputs:
        try:
            if parser.checkIfWeirdYAML(input) != True:
                print("invalid")
        except Exception as e:
            print(e)

    unexpected_inputs = [dict(test="pass"), 1, "abv", True, dict(test1="fail")]
    for input in unexpected_inputs:
        try:
            print(parser.keyMiner(input, "pass"))
        except Exception as e:
            print(e)
    unexpected_inputs = [
        {"test": "pass", "test1": "fail"},
        dict(test1=True),
        1,
        "abd",
        False,
    ]
    for input in unexpected_inputs:
        try:
            print(parser.getValuesRecursively(input))
        except Exception as e:
            print(e)

    unexpected_inputs = [1, "helmvalues", True, "/", "./environment.yml"]
    for input in unexpected_inputs:
        try:
            if parser.checkIfValidHelm(input) != True:
                print("invalid")
            else:
                print("valid")
        except Exception as e:
            print(e)

    unexpected_inputs = [5, "asdv", "/", "./environment.yml"]
    for input in unexpected_inputs:
        try:
            if parser.checkParseError(input) != True:
                print("invalid")
            else:
                print("valid")
        except Exception as e:
            print(e)


def simpleFuzzer():
    fuzzValues()


if __name__ == "__main__":
    simpleFuzzer()
