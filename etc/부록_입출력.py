n=int(input())

data = list(map(int, input().split()))

m, n, k  = map(int, input().split())

# 여러줄을 입력받을때는 readline()을 사용하는 것이 더 빠름.
import sys
data = sys.stdin.readline().rstrip() # rstrip은 엔터 문자 지워줌.
