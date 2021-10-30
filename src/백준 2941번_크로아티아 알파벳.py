croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

giveword = input("예제를 입력하세요: ")

for alphabet in croatia:
    giveword = giveword.replace(alphabet, '!')

print("크로아티아 알파벳 개수 : ", len(giveword))
