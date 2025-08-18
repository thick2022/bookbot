def word_count(text: str) -> int:
    return len(text.split())

def char_count(text: str) -> dict[str, int]:
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(counts_dict: dict[str, int]) -> list[tuple[str, int]]:
    items = list(counts_dict.items())
    items.sort(key=lambda kv: kv[1], reverse=True)
    return items

