"""
You are given a non-empty string S consisting of N characters.
In this problem we consider only strings that consist of lower-case
"""

def solution(S):
    words = S.split(" ")
    for i in range(len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)

solution("we test coders")