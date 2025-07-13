import matplotlib.pyplot as plt
from random import choice

class RandomWalk:

    def __init__(self, points):
        self.points=points
        self.x=[0]
        self.y=[0]

    def fill_walk(self):
        while len(self.x)<self.points:
            x_direction=choice([1, -1])
            x_distance=choice([0, 1, 2, 3, 4])
            x_step=x_direction*x_distance
            y_direction=choice([1, -1])
            y_distance=choice([0, 1, 2, 3, 4])
            y_step=y_direction*y_distance
            if x_step==0 and y_step==0:
                continue
            x=self.x[-1]+x_step
            y=self.y[-1]+y_step
            self.x.append(x)
            self.y.append(y)

if __name__ == "__main__":
    points=int(input("Points: "))
    rw=RandomWalk(points)
    rw.fill_walk()
    plt.style.use("classic")
    fig, ax=plt.subplots()
    ax.scatter(rw.x, rw.y, c=rw.y, cmap=plt.cm.viridis, edgecolors="none", s=1)
    plt.show()