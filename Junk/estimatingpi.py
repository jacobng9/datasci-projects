import random 
import matplotlib.pyplot as plt


def estimating_pi(num_points):
    circle_points = 0
    square_points = 0

    x_data = []
    y_data = []
    plt.ion()
    fig, ax = plt.subplots()
    
    for i in range(num_points):
        x = random.random()
        y = random.random()

        if x ** 2 + y**2 <= 1:
            circle_points += 1
        square_points += 1
        if square_points != 0:
            pi_estimated = 4 * circle_points / square_points
            print(pi_estimated)
        plt.plot(num_points, pi_estimated)

        x_data.append(i)
        y_data.append(pi_estimated)

        ax.set_xlim(0,num_points)
        ax.set_ylim(0, 4)

        plt.draw()
        plt.pause(0.05)
    plt.ioff()
    plt.show()

estimating_pi(1000)