import pandas as pd

def analyzeWords(words):
    """
    Analyze a Pandas.Series of words to generate various metrics.

    Arguments:
        words (pd.Series): Series of words to analyze.

    Returns:
        dict: Dictionary containing various metrics.
    """
    # Initialize metrics
    letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    max_char = 0
    size_counts = {}
    oo_words = []
    words_6plus = []


    for word in words:
        word = str(word).lower()  # Ensure consistent casing
        first_letter = word[0] if word else ""
        word_len = len(word)

        # Count words by first letter
        if first_letter.isalpha():
            letter_counts[first_letter] += 1

        # Track the longest word length
        max_char = max(max_char, word_len)

        # Count words by size
        size_counts[word_len] = size_counts.get(word_len, 0) + 1

        # Extract words that contain 'oo' and those that contain 6 or more letters
        oo_words = words[words.str.contains("oo")]
        words_6plus = words[words.str.len() >= 6].str.lower()

    metrics = {
        "letter_counts": letter_counts,
        "max_char": max_char,
        "size_counts": size_counts,
        "oo_count": len(oo_words),
        "oo_words": oo_words,
        "words_6plus": words_6plus,
        "words_6plus_count": len(words_6plus)
    }

    return metrics


if __name__ == "__main__":
    words_df = pd.read_csv('words.csv')
    words_series = words_df['x']
    metrics = analyzeWords(words_series)

    print("Letter Counts (per alphabet letter):")
    print(metrics['letter_counts'])
    print("\nMax Word Length:", metrics['max_char'])
    print("\nSize Counts (word lengths):")
    print(metrics['size_counts'])
    print("\nNumber of words with 'oo':", metrics['oo_count'])
    print("\nWords with 'oo':")
    print(metrics['oo_words'])  # Display first few words with 'oo'
    print("\nWords with 6 or more characters:")
    print(metrics['words_6plus'])  # Display first few long words
    print("\nNumber of words with 6 or more characters:", metrics['words_6plus_count'])