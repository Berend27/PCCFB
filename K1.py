# Kapitel 1 Final Boss
# 3 Water containers, each can hold 15 liters,
# but they have 12, 7, and 0 liters of water in them
# respectively. Make them all have the same amount.

container1 = 12
container2 = 7
container3 = 0

# find the average
# which is the amount that will go into each one
sum = container1 + container2 + container3
average = sum / 3

print(f"There are now {average:.2f} liters in each container.")