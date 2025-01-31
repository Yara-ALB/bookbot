def get_book_text(path):
    with open ("books/frankenstein.txt") as f:
        return f.read()

def count_characters(text):
    lowered_text = text.lower()
    counts = {}
    
    for c in lowered_text: 
        if c.isalpha():
            if c in counts :
                counts[c] += 1
            else :
                counts[c] = 1
    return counts

def sort_character_counts(counts):
    # Convert dictionary to list of dictionaries
    chars_list = []
    for char, count in counts.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort by count in descending order
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    return chars_list

def print_report(word_count, char_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char_dict in char_counts :
        print(f"The '{char_dict}' character was found {char_dict['count']} times")
    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    word_count = len(text.split())
    char_counts = count_characters(text)
    
    sorted_chars = sort_character_counts(char_counts)
    
    print_report(word_count, sorted_chars)

if __name__ == "__main__":
    main()

