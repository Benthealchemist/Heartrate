
def live_plotter(ts,bpm,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(ts,bpm,'-o',alpha=0.8)
        #update plot label/title
        plt.ylabel('BPM')
        plt.title('Title: {Graphing of BPM through time}'.format(identifier))
        plt.show()

    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(bpm)
    # adjust limits if new data goes beyond bounds
    if np.min(bpm)<=line1.axes.get_ylim()[0] or np.max(bpm)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(bpm)-np.std(bpm),np.max(bpm)+np.std(bpm)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(0.1)

    # return line so we can update it again in the next iteration
    return line1
