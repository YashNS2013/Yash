def count_vowels_and_consonants(s): 
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonant:
            consonant_count += 1

    return vowel_count, consonant_count




print(count_vowels_and_consonants("shree Ram!"))  