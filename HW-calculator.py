# p = frequency of the dominant allele in the population
# q = frequency of the recessive allele in the population
# p**2 = percentage of homozygous dominant individuals
# q**2 = percentage of homozygous recessive individuals
# 2pq = percentage of heterozygous individuals
pop_dom = int(input("Population of dominant? "))
pop_rec = int(input("Population of recessive? "))
population = int(input('What is the total population? ')) or (pop_dom + pop_res)
pknown = input("Is the frequency of the dominant allele in the population known?y/n ")
if pknown == "y":
    pnfknown = input("Do you know the frequency of the dominant allele?y/n ")
    if pnfknown == "y":
        p = float(input("What is the frequency of the dominant allele in the population? "))
    elif pnfknown == "n":
        p = pop_dom/ population
    q = 1- p
    print('p = ' + str(round(p, 2)))
    print('q = ' + str(round(q, 2)))    
if pknown == "n":
    print('Then  we will use the recessive frequency and trace it back :)')
    qnfknown = input('Do you know the frequency of the recessive allele?y/n ')
    if qnfknown == "y":
        q = float(input("What is the frequency of the recessive "))
    elif qnfknown == "n":
        q = pop_rec/population
    p = 1 - q
    print('p = ' + str(round(p, 2)))
    print('q = ' + str(round(q, 2))) 
Homop, Homoq = (p ** 2), (q ** 2)
hetero_pq = 2 * p * q 

print('Percentage of Homozygous dominant individuals is ' + str(round(Homop, 2)))
print('Percentage of Homozygous recessive individuals is ' + str(round(Homoq, 2)))
print('Percentage of Heterozygous individuals is ' + str(round(hetero_pq, 2)))      


assert p + q == 1
assert Homop + hetero_pq + Homoq