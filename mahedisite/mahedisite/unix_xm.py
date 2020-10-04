var = [19, 71, 70, 83, 29, 69, 31, -10, 0, -5]
prime_number= []
i = 0
k = 0
t = 0
counter = 0
for i in range(0, 10):
    if var[i] > 1:
        for j in range(2, var[i]):
            if var[i] % j == 0:
                break
        else:
            prime_number.insert(k, var[i])
    k = +1
    if var[i] < 0:
        counter += 1
        t = t + var[i]
print("Answer to the Question of A:", prime_number)
average = t / counter
print("Answer to the Question of B:", average)


