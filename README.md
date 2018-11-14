# Korean Word-IPA Dictionary

## 1. Getting List of Word Entries

From [the latest Kowiktionary dump](https://dumps.wikimedia.org/kowiktionary/20181101/), I got the list of every word in main namespace.
After getting this list, I filtered out all entries which are not written in Hangul, and stored Korean word entries in the file `kodict_entry.txt`.

## 2. Crawlling

By running `crawl.py` simultaneously on 11 subsets of `kodict_entry.txt`, which consist of 6000 words (except the last one), I extracted IPA information, forming a word-IPA dictionary for Korean language.
After the crawlling processes are all completed, I appended the results in alphabetical order, and deleted entries with no extracted IPA.

## 3. Converting IPA to X-SAMPA

From any word-IPA dictionary files, you can convert it to word-X-SAMPA dictionary.

```python
from convert import Converter

conv = Converter()
conv.subst_dict(<NAME_OF_DICT>)
```
