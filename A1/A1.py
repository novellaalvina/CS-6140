# Statistical Inference
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def print_avg(title, avg):
        print(f"{title} | Expected number of k random trials in order to have a collision: {avg}")

def plot(x,y, title):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("number of trials required, k")
    plt.ylabel("fraction of experiments that succeeded (a collision) after k trials")
    plt.show()

## QUESTION 1: BIRTHDAY PARADOX

# Generate random numbers in the domain [n] until two have the same value. 
# How many random trials did this take? We will use k to represent this value.
def q1a(n):
    k = 0
    same = False
    e_lst = np.zeros(n)

    while same == False:
        i = random.randint(0,n-1)
        if e_lst[i] == 0:
            e_lst[i] = 1
            k += 1
        else:
            same = True
    
    return k

# Repeat the experiment m = 500 times, and record for each time how many random trials this took. 
# Plot this data as a cumulative density plot 
# where the x-axis records the number of trials required k, 
# the y-axis records the fraction of experiments that succeeded (a collision) after k trials. 
# The plot should show a curve that starts at a y value of 0, and increases as k increases, and eventually reaches a y value of 1.
def q1bc(m,n):
    start = time.time()

    k_lst = []

    for i in range(m):
        k_lst.append(q1a(n))

    x = np.sort(k_lst)
    y = np.arange(m)/m

    end = time.time()
# Empirically estimate the expected number of k random trials in order to have a collision. That is, add up all values k, and divide by m.
    avg = np.sum(k_lst)/m

    print("time ", end-start)
    return x, y, avg

# Show a plot of the run time as you gradually increase the parameters n and m. 
# (For at least 3 fixed values of m between 500 and 10,000, plot the time as a function of n.) 
# You should be able to reach values of n = 1,000,000 and m = 10,000.
def q1d(m_lst, n_lst):
    time_lst = []
    colours = ['r', 'orange', 'y', 'blue', 'green', 'brown']

    for m in m_lst:
        t_lst = []
        for n in n_lst:
            start = time.time()
            print("m", m, "n", n)
            q1bc(int(m),int(n))
            end = time.time()
            t_lst.append(end-start)
            print(end-start)
        time_lst.append(t_lst)

    print(time_lst)

    for i,m in enumerate(m_lst):
        plt.plot(n_lst,time_lst[i], color=colours[i], label=f"m = {m}")

    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("domain size, n")
    plt.ylabel("run time in seconds")
    plt.title("Birthday Paradox")

    # Adding legend, which helps us recognize the curve according to it's colour
    plt.legend()
    
    # To load the display window
    plt.show()

## QUESTION 2: COUPON COLLECTOR

# Generate random numbers in the domain [n] until every value i ∈ [n] has had one random number equal to i. 
# How many random trials did this take? We will use k to represent this value. 
def q2a(n):    
    n_lst = np.arange(n)
    # i_lst = np.arange(n)
    # i_lst.fill(-1)
    i_lst = set()
    k = 0

    # start = time.time()
    while len(i_lst) != n:
        i = random.randint(0,n-1)
        i_lst.add(i)
        k += 1
        # np.sort(i_lst)
    # end = time.time()
    # print("time", end-start)

    return k

# Repeat step A for m = 500 times, and for each repetition record the value k of how many random trials we required to collect all values i ∈ [n]. 
# Make a cumulative density plot as in 1.B.
def q2bc(m, n):
    start = time.time()
    k_lst = []

    for i in range(m):
        k_lst.append(q2a(n))

    x = np.sort(k_lst)
    y = np.arange(m)/m

    end = time.time()
# Empirically estimate the expected number of k random trials in order to have a collision. That is, add up all values k, and divide by m.
    avg = np.sum(k_lst)/m

    print("time", end-start)
    return x, y, avg

# Show a plot of the run time as you gradually increase the parameters n and m. 
# (For at least 3 fixed values of m between 500 and 5,000, plot the time as a function of n.) 
# You should be able to reach n = 20,000 and m = 5,000.
def q2d(m_lst, n_lst):
    time_lst = []
    colours = ['r', 'orange', 'y', 'blue', 'green', 'brown']

    for m in m_lst:
        t_lst = []
        for n in n_lst:
            start = time.time()
            print("m", m, "n", n)
            q2bc(int(m),int(n))
            end = time.time()
            t_lst.append(end-start)
            print(end-start)
        time_lst.append(t_lst)

    print(time_lst)

    for i,m in enumerate(m_lst):
        plt.plot(n_lst,time_lst[i], color=colours[i], label=f"m = {m}")

    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("domain size, n")
    plt.ylabel("run time in seconds")
    plt.title("Coupon Collector")

    # Adding legend, which helps us recognize the curve according to it's colour
    plt.legend()
    
    # To load the display window
    plt.show()

# Run the program
def main():
    title = "Birthday Paradox"
    n = 10000
    m = 500

    x, y, avg = q1bc(m,n)
    plot(x, y, title)
    print_avg(title, avg)

    n = 10**6
    n_lst = np.array(np.linspace(1, n, 50))
    m_lst = np.array(np.linspace(500, 10000, 5))
    print("m", m_lst)
    print(n_lst)
    q1d(m_lst, n_lst)

    title = "Coupon Collector"
    n = 1000
    m = 500

    x, y, avg = q2bc(m, n)
    plot(x, y, title)
    print_avg(title, avg)

    n = 6000
    m_lst = np.array(np.linspace(500, 5000, 5))
    n_lst = np.array(np.linspace(1, n, 30))
    print("m", m_lst)
    print("n", n_lst)
    q2d(m_lst, n_lst)

if __name__ == "__main__":
    main()
