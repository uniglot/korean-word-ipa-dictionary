"""Wiktionary IPA crawler for Korean language."""
import sys

from bs4 import BeautifulSoup as bs
import requests


def crawl_kowiktionary(word):
    """Crawl and parse the Wiktionary page for a word."""
    response = requests.get('https://ko.wiktionary.org/wiki/{}'.format(word))
    html = bs(response.text, 'html.parser')
    first_heading = html.find('h1', {'id': 'firstHeading'}).get_text()
    span_ipa = html.find('span', {'class': 'IPA'})
    if not span_ipa:
        ipa_text = '<EMPTY>'
    else:
        ipa_text = span_ipa.find('span', {'class': 'IPA'}).get_text()[1:-1]
    return first_heading, ipa_text


def main(filename):
    """Command-line interface."""
    ko_dict = open(filename, 'r')
    output_file = open('out_'+filename, 'a')
    first_line = True
    num_line = 0
    curr_line = 1
    successed = 0
    failed = 0
    for line in ko_dict:
        try:
            if first_line:
                num_line = int(line)
                first_line = False
                continue
            entry, ipa = crawl_kowiktionary(line.strip())
            output_file.write('{} {}\n'.format(entry, ipa))
            print('{} - {} * {}/{} ({}%)'.format(entry, ipa, curr_line, num_line, int(100 * curr_line / num_line)))
            curr_line += 1
            successed += 1
        except AttributeError:
            print('Fail on this entry.')
            curr_line += 1
            failed += 1
    print('\n\n\nSUMMARY')
    print('Success: {} / Fail: {} / Percentage: {}%'.format(successed, failed, 100 * successed / (successed + failed)))
    ko_dict.close()
    output_file.close()

# MAIN
if __name__ == '__main__':
    if sys.argv[1][-3:] != 'txt':
        print('Wrong file format.')
    else:
        main(sys.argv[1])
