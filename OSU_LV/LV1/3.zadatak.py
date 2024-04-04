nums = []

while(1):
    print("Unesite b1roj:")
    user_input = input()
    if(user_input == "Done"):
        break
    try:
        num = float(user_input)
        nums.append(num)
    except ValueError:
        print("Krivi unos")
        continue

total = 0
for num in nums:
    total += num

print("Ukupno brojeva:" + str(len(nums)) + " \nProsjek: " + str(total/len(nums)) + " \nNajmanji broj: " + str(min(nums)) + " \nNajveci broj: " + str(max(nums)))

for num in sorted(nums):
    print(num)