"""A simple implementation of VAD that thresholds on sound power."""

import numpy as np


class SimpleVoiceActivityDetector:
    def __init__(self, threshold=3e-4, frame_rate=16000):
        """
        Initializes the SimpleVoiceActivityDetector with a threshold.

        Args:
            threshold (float, optional): Minimum audio power to include.
        """
        self.threshold = threshold
        self.frame_rate = frame_rate

    def __call__(self, audio_frame):
        """
        Determines if the given audio frame contains speech by comparing the audio power against
        the threshold.

        Args:
            audio_frame (np.ndarray): The audio frame to be analyzed for voice activity. It is expected to be a
                                      NumPy array of audio samples.

        Returns:
            bool: True if the speech probability exceeds the threshold, indicating the presence of voice activity;
                  False otherwise.
        """
        frame_size = audio_frame.flatten().shape[0]
        if not frame_size:
            return False
        return audio_frame.dot(audio_frame) / frame_size > self.threshold
