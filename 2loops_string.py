'''
Utilização de recursividade

'''


p = "PAULA"

for i in range(len(p)):
    letra = p[i]
    for j in range(len(p) + 1):
        substring = p[i:j]
        if len(substring) != 0:
            print(substring)

print()


s = p

def subs(i, s):
    if i <= len(s):
        for j in range(i, len(s)+1):
            print(s[i:j])
        subs(i+1, s)


subs(0,s)


def subs(i,j,s):
    if i < len(s):
        print(s[i:j])
        if j < len(s):
            subs(i, j+1, s)
        else:
            subs(i+1, i+1, s)

subs(0,0,s)
