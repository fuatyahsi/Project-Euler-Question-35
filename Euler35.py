def is_prime(num):
    prime =True
    if num == 1 or num == 0: prime = False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            prime=False
    return prime
def circular(t:set):
    circle = True
    for i in t:
        if not is_prime(i):circle = False
    return circle

solution_set_circular = {2}
for i in range(1,1000000,2):
    if is_prime(i):
        set_circular = set()
        number = str(i)
        if len(str(i))==1: solution_set_circular.add(i)
        for j in range(len(str(i))-1):
            number = (number[-1]+number)[:len(number)]
            set_circular.add(i)
            set_circular.add(int(number))
        if circular(set_circular):
            for i in set_circular:
                solution_set_circular.add(i)

print(len(solution_set_circular),solution_set_circular)





