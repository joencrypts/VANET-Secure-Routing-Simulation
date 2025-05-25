import matplotlib.pyplot as plt
import pandas as pd

def plot_hash_times(hash_times):
    data = []
    for k, times in hash_times.items():
        for t in times:
            data.append({"Hash": k, "Time": t})
    df = pd.DataFrame(data)
    df.boxplot(column="Time", by="Hash", showmeans=True)
    plt.title("Hash Computation Times")
    plt.suptitle("")
    plt.show()

def plot_speeds(vehicles, steps, dt):
    import numpy as np
    time = [i * dt for i in range(steps)]
    for v in vehicles:
        plt.plot(time, [v.speed] * steps, label=v.id)
    plt.title("Vehicle Speeds")
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.legend()
    plt.show()

def plot_positions(vehicles, steps, dt):
    for v in vehicles:
        x, y = [], []
        for _ in range(steps):
            v.move(dt)
            x.append(v.position[0])
            y.append(v.position[1])
        plt.plot(x, y, label=v.id)
    plt.title("Vehicle Positions")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()
