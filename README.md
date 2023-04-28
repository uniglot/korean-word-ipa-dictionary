# Korean Word-IPA Dictionary

### Notice 2 (28 Apr, 2023)

Sorry, I just realized that I'm a weary lazy procrastinator.

I restructured the codebase earlier, but I've got no notable updates yet. I'll do remaining things maybe... within September?

### Notice (19 Aug, 2022)

I'm going to refactor the entire code soon and add a CI pipeline to keep the dictionary updated!

I'll put efforts to get it done within September.

## 1. Getting List of Word Entries

From [the latest Kowiktionary dump](https://dumps.wikimedia.org/kowiktionary/latest/), I got the list of every word in main namespace.
After getting this list, I filtered out all entries which are not written in Hangul, and stored Korean word entries in the file `kodict_entry.txt`.

## 2. Crawling

By running `crawl.py` simultaneously on 11 subsets of `kodict_entry.txt`, which consist of 6000 words (except the last one), I extracted IPA information, forming a word-IPA dictionary for Korean language.
After the crawling processes are all completed, I appended the results in alphabetical order, and deleted entries with no extracted IPA.

## 3. Converting IPA to X-SAMPA

From any word-IPA dictionary files, you can convert it to word-X-SAMPA dictionary.

```python
from convert import Converter

conv = Converter()
conv.subst_dict(<NAME_OF_DICT>)
```

## 4. Licenses

You can make use of the **results** of scripts (i.e., .dict files and kodict_entry.txt file) under [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). You can use the **scripts** under MIT License.
