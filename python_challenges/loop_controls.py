# using loop control statements to check the status of execution in a loop

legends_ages = (1978, 1963, 1984, 1947, 1938, 1934, 1959, 1956)

dict1 = dict(zip(legends_NBA, legends_ages))  # zip function pairs two iterables legends_NBA and legends_age and returns
                                               # a dictionary

print(dict1)


for x in dict1:
    if dict1[x] == min(dict1.values()):
        print(f'{x} is the oldest of NBA players')
        continue    # continue does not execute beyond the keyword but keeps on repeating the loop till end
    print(f"{x} was born in {dict1[x]}")

for x in dict1:
    if dict1[x] == min(dict1.values()):
        print(f'{x} is the oldest of NBA players')
        break    # break statement stops the execution and also terminates the loop
    print(f"{x} was born in {dict1[x]}")

for x in dict1:
    if dict1[x] == min(dict1.values()):
        print(f'{x} is the oldest of NBA players')
        pass    # pass acts as a place holder and executes the code that follows it and also runs the loop till end
    print(f"{x} was born in {dict1[x]}")
