# LOD-Fishes
## Fish Emoji Scraper

This project scrapes the Luxembourgish Online Dictionary (lod.lu) for words containing fish emojis (🐠, 🐟, and 🐡) in their lemmas using their API. The resulting data is stored in a JSON file called `fish_urls.json`.

## How it works

The script sends requests to the lod.lu API to fetch all the entries in the dictionary, page by page. It then searches for lemmas containing any of the specified fish emojis (🐠, 🐟, or 🐡). When a lemma with a fish emoji is found, the script logs the URL, lemma, and an ID for the entry.

## JSON Structure

The output JSON file, `fish_urls.json`, has the following structure:

```json
[
  {
    "id": 0,
    "url": "https://lod.lu/artikel/{lod_id}",
    "lemma": "A 🐠"
  },
  {
    "id": 1,
    "url": "https://lod.lu/artikel/{lod_id}",
    "lemma": "Aacht 🐟"
  },
  ...
]
```

Each item in the JSON file represents an entry with a fish emoji in its lemma. The item has the following properties:

* id: A unique integer ID for the entry, starting from 0.
* url: The URL of the entry, formatted as https://lod.lu/artikel/{lod_id}.
* lemma: The lemma of the entry containing the fish emoji. 

## How to use

1. Ensure you have Python installed on your system.
2. Run the script using python main.py in your terminal or command prompt.
3. The script will fetch the data from the API, process it, and store the results in a fish_urls.json file.
4. Check the fish_urls.json file for the scraped data.
