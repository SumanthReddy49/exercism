def mutate_string(string, position, character):
    s=list(string)
    s[position]=character
    return "".join(s)
