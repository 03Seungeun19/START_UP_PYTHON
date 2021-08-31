#성적분류기


name=input("이름을 입력하세요 :")
sub_1=input(("과목1을 입력하세요 :"))
sub_2=input(("과목2를 입력하세요 :"))
sub_3=input(("과목3을 입력하세요 :"))

score1=int(input("{} 성적을 입력하세요 :".format(sub_1)))
score2=int(input("{} 성적을 입력하세요 :".format(sub_2)))
score3=int(input("{} 성적을 입력하세요 :".format(sub_3)))

if score1 >=90:
    grade1=("A")
elif score1 >=80 :
    grade1=("B")
else :
    grade1=("C")


if score2 >=90:
    grade2=("A")
elif score2 >=80 :
    grade2=("B")
else :
    grade2=("C")

if score3 >=90:
    grade3=("A")
elif score3 >=80 :
    grade3= ("B")
else :
    grade3=("C")

print("---------<성적표>---------")
print(f"이름: {name.upper()}")
print(sub_1,"등급:", grade1)
print(sub_2,"등급:", grade2)
print(sub_3,"등급:", grade3)
