# n = int(input())
# arr = map(int, input().split())
# new = list(set(arr))
# new.sort(reverse = True)
# print(new[1])
# def swap_case(s):
#     new = ''
#     for i in range(len(s)):
#         if s[i].isupper():
#             new = new + s[i].lower()
#         elif s[i].islower():
#             new = new + s[i].upper()
#         else:
#             new = new + s[i]
#     return new
#
# def count_substring(string,sub_string):
#     count = 0
#     if sub_string in string:
#         count +=1
#     return count
# s = 'ABCDCDC'
# ss ='CDC'
# print(count_substring(s,ss))

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        elif num_vowels != 0 and num_vowels % 2 != 0:
            score += 1
    return score
x = ['programming','is','awesome']
print(score_words(x))


