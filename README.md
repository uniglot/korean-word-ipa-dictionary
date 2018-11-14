# Korean Word-IPA Dictionary

## 1. Getting List of Word Entries

From [the latest Kowiktionary dump](https://dumps.wikimedia.org/kowiktionary/20181101/), I got the list of every word entry in main namespace.
From this list, I filtered out all entries which is not written in Hangul, and stored the Korean word entries in the file `kodict_entry.txt`.

## 2. Crawlling

I ran `crawl.py` on 11 subsets of `kodict_entry.txt`, which consist of 6000 words (except the last one), simultaneously.
After the crawlling processes are all completed, I appended the results and deleted entries with empty IPA.
