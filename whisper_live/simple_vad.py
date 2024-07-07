"""Simple implementation of VAD which just looks at audio power."""

import numpy as np

class SimpleVoiceActivityDetector:
    def __init__(self, threshold: float = 0):
        """
        Initializes the SimpleVoiceActivityDetector.
        """
        self.threshold = threshold

    def __call__(self, audio_frame):
        """
        Determines if the given audio frame contains speech by comparing the detected speech probability against
        the threshold.

        Args:
            audio_frame (np.ndarray): The audio frame to be analyzed for voice activity. It is expected to be a
                                      NumPy array of audio samples.

        Returns:
            bool: True if the speech probability exceeds the threshold, indicating the presence of voice activity;
                  False otherwise.
        """
        power = np.dot(audio_frame, audio_frame) / audio_frame.flatten().shape[0]
        print('audio power:', power)
        return power > self.threshold
