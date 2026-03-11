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
    
    def square(self, frequency, amplitude=1, phase_deg=0, duration=1):
        """
        Generate square wave    # signum function

        parameters
        ----------
        frequency   : float - Hz
        amplitude   : float - volts
        phase_deg   : float - degrees
        duration    : float - seconds

        return
        ------
        t       : ndarray - time axis
        signal  : ndarrry - amplitude values
        """
        phase_rad = np.deg2rad(phase_deg)
        t = self.time_axis(duration)
        # signal = amplitude * np.sign(
        #     np.sin(
        #         2 * np.pi * t * frequency + phase_rad
        #     )
        # )

        # is np.where return +1 if sin > 0 or -1 if sin is 0 no in between values
        signal = amplitude * np.where(
            np.sin(2 * np.pi * t * frequency + phase_rad) > 0 , +1 , -1
        )


        return t, signal

    def triangle(self, frequency, amplitude = 1, phase_deg = 0, duration = 1):
        """
        Generate a triangle wave

        parameters
        ----------
        frequency   : float - Hz
        amplitde    : float - volts
        phase_deg   : float - degrees
        duration    : float - seconds

        return 
        ------
        t       : ndarray - time axis
        signal  : ndarray - amplitude values
        """
        phase_rad = np.deg2rad(phase_deg)
        t = self.time_axis(duration)

        signal = amplitude * ( 2 * np.arcsin(
            np.sin(2 * np.pi * frequency * t + phase_rad)
        )/np.pi)

        return t, signal
        
    def noise(self, amplitude = 1, duration = 1, mean = 0):
        """
        Generate noise

        parameters
        ----------
        amplitude   : float - volts
        duartion    : float - seconds

        Return
        ------
        t       : ndarray - time axis
        signal  : ndarray - noise array
        """
        t = self.time_axis(duration)
        noise = mean + amplitude * np.random.randn(len(t))

        return t, noise
    
    # def noise_sine(self, frequency, amplitude= 1, phase_deg = 0, duration = 1):
    #     t, sine = self.sine(frequency, duration)
    #     t, noise = self.noise(duration)
    #     signal = sine+noise

    #     return t, signal

