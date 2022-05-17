def greet(lang):
    if lang == "es":
        return "Hello English"
    elif lang == "fr":
        return "Hello France"
    elif lang == "Bang":
        return "I am Bengali"
    else:
        print("Every Language is Important")


print(greet("es"))
print(greet("fr"))
print(greet("Bang"))
print(greet("a"))