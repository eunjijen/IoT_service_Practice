import sounddevice as sd
import soundfile as sf
from io import BytesIO

fs = 44100 # sample rate
seconds = 3   # durations of recording

myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
sd.wait()

mem_wav = BytesIO()
sf.write('output.wav', myrecording, fs) # Save as WAV file
mem_wav.seek(0)

# mem_wav 전송
