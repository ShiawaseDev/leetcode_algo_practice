def lengthOfLongestSubstring(s):
    letters = set()
    result = 0
    left_letter_id = 0
    for right_letter_id in range(len(s)):
        while s[right_letter_id] in letters:
            letters.remove(s[left_letter_id])
            left_letter_id += 1
        letters.add(s[right_letter_id])
        if right_letter_id - left_letter_id + 1 > result:
            result = right_letter_id - left_letter_id + 1
    return result

