def count_vowels(s):

    vowels = "aeiou AEIOU" #대문자 소문자 포함 출력 가능
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


text = input("문자열을 입력하세요: ")
print(count_vowels(text))  # 문자를 입력 받았을시에 출력은: 3
