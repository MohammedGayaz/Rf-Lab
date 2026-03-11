import matplotlib.pyplot as plt

class Plotter:

    @staticmethod
    def plot_time(t, signal, title="Signal", xlabel="Time (s)", ylabel="Amplitude"):
        """
        Plot a signal in time domain.

        Parameters
        ----------
        t       : ndarray - time axis
        signal  : ndarray - amplitude values
        title   : plot title
        """

        plt.figure(figsize=(10,4))
        plt.plot(t, signal)
        plt.title(title)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.grid(True)
        plt.tight_layout()
        plt.show()


    @staticmethod
    def plot_multiple(t, signals, labels=None, title="Signals"):
        """
        Plot multiple signals on same graph.

        Parameters
        ----------
        t       : time axis
        signals : list of signals
        labels  : list of labels
        """

        plt.figure(figsize=(10,4))

        for i, signal in enumerate(signals):
            if labels:
                plt.plot(t, signal, label=labels[i])
            else:
                plt.plot(t, signal)

        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")

        if labels:
            plt.legend()

        plt.grid(True)
        plt.tight_layout()
        plt.show()
