#2주차 이론실습-2

sentence = input("이름을 입력해 주세요: ")
print(sentence)

#슬라이싱-첫번째 글자, 마지막 글자, 3~6 알파벳 (사람기준)
print(sentence[0])
print(sentence[-1])
print(sentence[2:6])


#문자열 연산
print(sentence+sentence)
print(sentence,sentence)
print(sentence*3)

word = sentence + sentence
word2 = sentence*3
print(word)
print(word2)
'''
문자열 관련 함수
'''
print("<문자열 관련 함수>")
print(sentence.count('u'))
print(sentence.lstrip())
print(sentence.rstrip())
print(sentence.strip())
print(sentence.upper())
print(sentence.lower())
print(sentence.index('u'))
print(sentence.replace('u','a'))
