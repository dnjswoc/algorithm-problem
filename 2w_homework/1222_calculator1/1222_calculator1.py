import sys
sys.stdin = open('input.txt')

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
plus = {'+': 1}


def postfix(ep):
    stack = []
    result = []
    for ex in ep:
        if ex in num:
            result += [ex]
            continue
        if ex in plus.keys():
            while 0:
                pass
    pass


def calculator(ep):

    pass


for _ in range(10):
    N = int(input())
    expression = input()
    print(f'{N}')
