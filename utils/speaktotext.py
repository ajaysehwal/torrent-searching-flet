import speech_recognition as sr

class SpeechToText:
    def __init__(self, noise_duration=1, energy_threshold=300, pause_threshold=0.2):
        """Initialize the recognizer with ambient noise duration, energy threshold, and pause threshold."""
        self.recognizer = sr.Recognizer()
        self.noise_duration = noise_duration
        self.recognizer.energy_threshold = energy_threshold
        self.recognizer.pause_threshold = pause_threshold

    def listen_and_recognize(self):
        """Captures and recognizes speech from the microphone, returning recognized text."""
        try:
            with sr.Microphone() as source:
                self._adjust_for_noise(source)
                print("Listening... Please speak clearly.")
                audio = self.recognizer.listen(source)
                return self._recognize_speech(audio)
        except sr.RequestError as e:
            print("API error or no internet connection:", e)
            return None
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def _adjust_for_noise(self, source):
        """Calibrates the recognizer to account for background noise."""
        print("Calibrating for ambient noise... Please wait.")
        self.recognizer.adjust_for_ambient_noise(source, duration=self.noise_duration)

    def _recognize_speech(self, audio):
        """Recognizes speech using Google's API and handles errors gracefully."""
        try:
            # Using Google's Web Speech API
            text = self.recognizer.recognize_google(audio)
            print("Recognized Speech:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"API error; check your internet connection. Error: {e}")
            return None
