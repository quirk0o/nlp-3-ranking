import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def plot_func(xdata, ydata, color):
    plt.plot(xdata, ydata, color)


def plot_stats(ranking):
    data = [(rank, word, frequency) for rank, (word, frequency) in enumerate(ranking)]
    xdata, labels, ydata = zip(*data)
    plot_func(xdata, ydata, 'r')
    plt.xticks(xdata, labels, rotation=90)

    # zopt = fit(zipf, ranks, frequencies)
    # plot_func(map(lambda x: zipf(x, zopt[0]), ranks), ranks, 'g')

    # mopt = fit(mandelbrot, ranks, frequencies)
    # plot_func(map(lambda x: mandelbrot(x, mopt[0], mopt[1], mopt[2]), ranks), ranks, 'b')
