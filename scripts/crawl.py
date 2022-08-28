"""Wiktionary IPA crawler for Korean language."""
import sys

from bs4 import BeautifulSoup as bs
import requests


WIKTIONARY_URL = "https://ko.witionary.org/wiki"


def crawl_kowiktionary(word):
    """Crawl and parse the Wiktionary page for a word."""
    response = requests.get(f"{WIKTIONARY_URL}/{word}")
    html = bs(response.text, "html.parser")
    first_heading = html.find("h1", {"id": "firstHeading"}).get_text()
    span_ipa = html.find("span", {"class": "IPA"})
    if not span_ipa:
        ipa_text = "<EMPTY>"
    else:
        ipa_text = span_ipa.find("span", {"class": "IPA"}).get_text()[1:-1]
    return first_heading, ipa_text


def main(filename):
    """Command-line interface."""
    ko_dict = open(filename, "r")
    output_file = open("out_"+filename, "a")
    first_line = True
    num_line = 0
    curr_line = 1
    succeeded = 0
    failed = 0
    for line in ko_dict:
        try:
            if first_line:
                num_line = int(line)
                first_line = False
                continue
            entry, ipa = crawl_kowiktionary(line.strip())
            output_file.write(f"{entry} {ipa}\n")
            print(f"{entry} - {ipa} * {curr_line}/{num_line} ({int(100 * curr_line / num_line}%)")
            curr_line += 1
            succeeded += 1
        except AttributeError:
            print("Fail on this entry.")
            curr_line += 1
            failed += 1
    print("\n\n\nSUMMARY")
    print(f"Success: {succeeded} / Fail: {failed} / Percentage: {100 * succeeded / (succeeded + failed)}%"
    ko_dict.close()
    output_file.close()

# MAIN
if __name__ == "__main__":
    if sys.argv[1][-3:] != "txt":
        print("Wrong file format.")
    else:
        main(sys.argv[1])
