import matplotlib.pyplot as plt
from random import randint
random_no_list = []
random_no_dict = {}
for i in range(0, 10001):
    random = randint(0, 10)
    if random not in random_no_dict.keys():
        random_no_dict[random] = 1
    elif random in random_no_dict.keys():
        random_no_dict[random] += 1
for times_chosen in random_no_dict.values():
    random_no_list.append(times_chosen)
plt.style.use("classic")
fig, ax = plt.subplots()
ax.set_xlabel("No's to choose")
ax.set_ylabel("Times Chosen")
ax.plot(random_no_list)
ax.scatter(x = list(i for i in range(0,11)), y = random_no_list, s = 100)
plt.show()