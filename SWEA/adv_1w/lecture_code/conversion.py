# 10진수 정수 입력
N = int(input())
N_2, N_8, N_16 = N, N, N

hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

# 입력 받은 수를 2진수로 변환
binary = []
while N_2 >= 2:
    binary.append(str(N_2 % 2))
    N_2 //= 2
binary.append(str(N_2))
while len(binary) % 4 != 0:
    binary.append('0')
print(''.join(binary[::-1]))

# 입력 받은 수를 8진수로 변환
octal = []
while N_8 >= 8:
    octal.append(str(N_8 % 8))
    N_8 //= 8
octal.append(str(N_8))
print(''.join(octal[::-1]))

# 입력 받은 수를 16진수로 변환
hexadecimal = []
while N_16 > 0:
    hex_rem = N_16 % 16
    if hex_rem in hex_dict.keys():
        hex_rem = hex_dict[hex_rem]
    elif hex_rem <= 9:
        hex_rem = str(hex_rem)
    hexadecimal.append(hex_rem)
    N_16 //= 16
print(''.join(hexadecimal[::-1]))

# 하나의 함수로
def conversion():
    pass
