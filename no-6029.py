# 16진수를 입력받아 8진수(octal)로 출력해보자.
num = input()
hexN = int(num, 16)
print("%o" % hexN)
# 참고
# 16진수 및 n진수 입력 방법
# int(n,16) 이렇게 int의 두 번째 인자에 원하는 진수 입력
