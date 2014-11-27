from __future__ import print_function
__author__ = 'easy as pie labs'
import numpy as np


def save_to_file(data, file_name, mode='a'):
    """
    saves the data to the file
    :param data: the data to save
    :param file_name: name of the file
    :param mode: file saving mode ('a' = append ....)
    :return:
    """
    f = open(file_name, mode)
    for item in data:
        print(str(item), file=f)
    f.close()



def profiling_bar_chart(plot_times, plot_labels):
    """
    plots a bar chart of times
    :param plot_times: times per execution
    :param plot_labels: labels
    :return:
    """
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ## necessary variables
    ind = np.arange(len(plot_times)) # the x locations for the groups
    width = 0.5 # the width of the bars

    ## the bars
    date_bars = ax.bar(ind, plot_times, width)

    # axes and labels
    ax.set_xlim(-width, len(ind)+width)
    ax.set_ylim(0.15, 0.18)
    ax.set_ylabel('time in ms per 10k checks')
    ax.set_title("blocks, threads")

    xTickMarks = plot_labels
    ax.set_xticks(ind+width)

    xtickNames = ax.set_xticklabels(xTickMarks)

    plt.setp(xtickNames, rotation=90, fontsize=10)

    plt.savefig("block_threads_bars.png")
    plt.show()

