from collections import Counter

def check_and_build_palindrome(word):
    letter_counts = Counter(word)
    odd_count = sum(count % 2 for count in letter_counts.values())

    if odd_count > 1:
        return "Из данного слова невозможно составить палиндром"
    else:
        palindrome = ""
        middle_char = ""

        for letter, count in letter_counts.items():
            palindrome += letter * (count // 2)
            if count % 2 == 1:
                middle_char = letter

        return palindrome + middle_char + palindrome[::-1]
