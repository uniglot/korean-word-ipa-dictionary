"""Phoneme format converter from IPA to X-SAMPA format."""
import re


RULEBOOK = "lookup-tables/ipa2sampa.rule"


def is_hangul(word):
    """Check whether the given word is Hangul or not."""
    pattern = r"[가-힣]+"
    return bool(re.match(pattern, word))


class Converter():
    """IPA to X-SAMPA Converter."""
    rules = {}

    def __init__(self, rulebook=RULEBOOK):
        rulebook_file = open(rulebook, "r")
        for rule in rulebook_file:
            symbols = rule.strip().split(" ")
            if len(symbols) == 1:
                self.rules[symbols[0]] = ""
            else:
                self.rules[symbols[0]] = symbols[1]
        rulebook_file.close()

    def subst_ipa(self, source: str) -> str:
        """Substitute IPA symbols to the corresponding X-SAMPA notations."""
        result = ""
        for letter in source.strip():
            if letter == "/":
                continue
            x_sampa = self.rules.get(letter)
            if x_sampa or x_sampa == "":
                result += x_sampa
            else:
                result += letter
        return result

    def subst_dict(self, source: str):
        """Substitute every IPA symbol in a word-IPA dictionary."""
        word2ipa = open(source, "r")
        out = open("out_"+source, "w")
        for entry in word2ipa:
            words = entry.strip().split(" ")
            print(words)
            keyword, result, result_homonym = "", "", ""
            homonym = False
            for word in words:
                if is_hangul(word):
                    keyword = word
                elif word == "~":
                    homonym = True
                elif homonym:
                    result_homonym = self.subst_ipa(word)
                else:
                    result = self.subst_ipa(word)
            out.write(f"{keyword} {result}\n")
            if homonym:
                out.write(f"{keyword}(2) {result_homonym}\n")
        word2ipa.close()
        out.close()
