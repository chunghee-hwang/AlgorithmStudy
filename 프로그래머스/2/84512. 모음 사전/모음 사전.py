nexts = {"A": "E", "E": "I", "I": "O", "O": "U"}
def up(word):
    if word[-1] == "U":
        return up(word[: len(word) - 1])
    else:
        last = word[-1]
        word = word[: len(word) - 1] + nexts[last]
        return word
def solution(word):
    dp = ["A"]
    while dp[-1] != "UUUUU":
        w = dp[-1]
        n = len(w)
        last = w[-1]
        if n != 5:
            next = w + "A"
        else:
            if last != "U":
                next = w[: n - 1] + nexts[last]
            else:
                next = up(w)
        dp.append(next)
    return dp.index(word) + 1