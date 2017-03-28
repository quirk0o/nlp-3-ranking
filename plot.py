import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from zipf import *


def fit(func, xdata, ydata):
    popt = curve_fit(func, xdata, ydata)
    return popt


def plot_func(xdata, ydata, color, label=None):
    plt.plot(xdata, ydata, color, label=label)


def plot_most_common(xdata, ydata, labels):
    xdata = xdata[:100]
    ydata = ydata[:100]
    labels = labels[:100]

    plt.subplot(211)

    plot_func(xdata, ydata, 'r')
    plt.xticks(xdata, labels, rotation=90)


def plot_ranking(xdata, ydata):
    plt.subplot(212)

    plot_func(xdata, ydata, 'r', label="Ranking")


def plot_zipf(xdata, ydata):
    plt.subplot(212)

    zopt, zcov = fit(zipf, xdata, ydata)
    plot_func(xdata, [zipf(x, zopt[0]) for x in xdata], 'g', label="Zipf")


def plot_mandelbrot(xdata, ydata):
    plt.subplot(212)

    mopt, mcov = fit(mandelbrot, xdata, ydata)
    p, d, b = mopt
    plot_func(xdata, [mandelbrot(x, p, d, b) for x in xdata], 'b', label="Mandelbrot")


def plot_stats(ranking):
    xdata = np.array(range(1, len(ranking) + 1))
    ydata = np.array(map(lambda x: x[1], ranking))
    labels = np.array(map(lambda x: x[0], ranking))

    plt.figure(1)
    plot_most_common(xdata, ydata, labels)
    plot_ranking(xdata, ydata)
    plot_zipf(xdata, ydata)
    plot_mandelbrot(xdata, ydata)

    plt.yscale('log')
    plt.ylim(ymin=0.0)
    plt.legend()
