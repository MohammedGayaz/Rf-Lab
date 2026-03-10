import numpy as np


class SignalGenerator:

    def __init__(self, fs):
        """
        fs: sampling frequency
        """
        self.fs = fs

    def time_axis(self, duration):
        """
        Generate time axis
        """
        ts = 1 / self.fs    # sampling peroid 
        t = np.arange(0, duration, ts)
        return t

    def sine(self, frequency, amplitude=1, phase_deg=0, duration=1):
        """
        Generate a Sine Wave.

        Parameters
        ----------
        frequency   : float - Hz
        amplitude   : float - Vlots 
        phasae deg  : float - degrees
        duration    : float - seconds

        Return
        ------
        t       : time axis
        signal  : amplitude values
        """
        phase_rad = np.deg2rad(phase_deg)
        t = self.time_axis(duration)
        signal = amplitude * np.sin(
            2 * np.pi * frequency * t + phase_rad
        )

        return t, signal 

    def cosine(self, frequency, amplitude=1, phase_deg=0, duration=1):
        """
        Generate a Cosine wave.
        
        parameters
        ----------
        frequency   : float - Hz
        amplitude   : float - volts
        phase       : float - degrees
        duration    : float - seconds

        Return
        ------
        t       : time - ndarray[t]
        signal  : amplitude - ndarray
        """
        phase_rad = np.deg2rad(phase_deg)
        t = self.time_axis(duration)
        signal = amplitude * np.cos(
            2 * np.pi * frequency * t + phase_rad
        )

        return t, signal
