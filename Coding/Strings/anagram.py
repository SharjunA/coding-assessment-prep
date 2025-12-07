from collections import Counter

def is_anagram(a: str, b: str) -> bool:
    # Normalize: remove spaces, lowercase
    a_clean = a.replace(" ", "").lower()
    b_clean = b.replace(" ", "").lower()
    
    return Counter(a_clean) == Counter(b_clean)

str1 = "Listen"
str2 = "Silent"
print(f"Are '{str1}' and '{str2}' anagrams? {is_anagram(str1, str2)}")