print("entering in loop")
for i in range(1, 10):
    
    if i == 7:
        break
    else:
        print(i)
print("exited from loop")
print("jay shree Ram !")





numbers = [4, 8, 12, 15, 20, 25]

for n in numbers:
    if n == 15:
        break
    print(n)



sum = 0
n = 1

while True:
    sum += n
    if sum >= 100:
        break
    n = n + 1

print("The final sum is:", sum)
