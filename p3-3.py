# 연습문제 3-3: 영어 모음 개수 반환 (공백 제외)
def count_vowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    text = input("문자열을 입력하세요: ")
    print(count_vowel(text))
