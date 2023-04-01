import requests
import json

def main():
    base_url = "https://lod.lu/api/lb/entries?type=all&items_per_page=100&page="
    fish_emojis = ["🐠", "🐡", "🐟"]
    page = 1
    logged_items = []
    entry_id = 0

    while True:
        url = base_url + str(page)
        response = requests.get(url)
        data = json.loads(response.text)

        if not data["items"]:
            break

        for item in data["items"]:
            lemma = item["lemma"]
            lod_id = item["lod_id"]

            if any(emoji in lemma for emoji in fish_emojis):
                logged_item = {
                    "id": entry_id,
                    "url": f"https://lod.lu/artikel/{lod_id}",
                    "lemma": lemma
                }
                logged_items.append(logged_item)
                print(f"Logged ID: {logged_item['id']} URL: {logged_item['url']} with Lemma: {logged_item['lemma']}")
                entry_id += 1

        page += 1

    log_items(logged_items)

def log_items(logged_items):
    with open("fish_urls.json", "w") as log_file:
        json.dump(logged_items, log_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
