from functools import reduce 
from itertools import combinations
import sys

# for fast input
r = sys.stdin.readline
# prime number finder

def prime_find(n):
    
    nums = set(range(2,n+1))
    primes = []
    while nums:
        num = nums.pop()
        primes.append(num)
        nums -= set([n for n in nums if n%num==0])
    return primes


def sub_mul_extractor(target_numbers, target_primes):
    ### key: 약수의 개수(Y), value: X
    dic_XY = dict()

    while target_numbers:
        # 하나씩 까서
        target_number = target_numbers.pop()
        target_number_origin = target_number #출력 땜에 ... 개선 필요

        # 소인수분해
        divisors = [1]
        for p in target_primes:
            while target_number % p == 0:
                divisors.append(p)
                target_number = target_number//p

        # 약수 리스트 구하기
        ## 중복 -> 개선 필요
        coms = []
        for r in range(1, len(divisors)):
            coms += list(combinations(divisors, r))
        submul = set([reduce((lambda x, y: x * y), com) for com in set(coms)])

        # dict에 넣어주기
        dic_XY[len(submul)] = dic_XY.get(len(submul), []) + [target_number_origin]
        # target number의 약수는 볼 필요 없으니 제거
        target_numbers -= submul
    
    return dic_XY

    
def main():
    while True:
        M, N = map(int, r().split())
        if M == N == 0: break
        
        
        target_numbers = set(range(M, N+1))
        target_primes = prime_find(int(N**0.5))
        dic_XY = sub_mul_extractor(target_numbers, target_primes)
        Y = max(dic_XY.keys())
        X = max(dic_XY[Y])
        print(X, Y)

if __name__=="__main__":
    main()