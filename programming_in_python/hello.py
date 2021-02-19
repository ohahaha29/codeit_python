# 코멘트(주석): 복잡한 코드 설명, 하다가 만 부분 표시, 다른 개발자들과 소통
print("Hello world!")

# 변수
kitkat = 190
oreos = 502
pringles = 292
twix = 135.9
cheetos = 485

# 다양한 과자 조합
print(kitkat + oreos * 2)
print(cheetos * 4)
print(pringles + oreos + twix)
print(pringles * 3 + oreos * 2)

# 함수
def hello():
    print("hello")
    print("welcome to codeit")
hello();

# 파라미터
def hello(name):
    print("hello")
    print(name)
    print("welcome to codeit")
hello("chris");

# 여러 개의 파라미터
def print_sum(a, b, c):
    print(a + b)
    print(a + b + c)
    print(a * b * c)
print_sum(10, 7, 9)