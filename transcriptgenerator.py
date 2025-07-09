import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr
import os
import tkinter as tk
from tkinter import filedialog




def generateAudio(filePath):
    video = mp.VideoFileClip(filePath)

    audioFile = video.audio
    audioFile.write_audiofile("audio.wav")

    audio = AudioSegment.from_file("audio.wav")
    chunkMS = 60 * 1000  # 60 Seconds
    chunks = make_chunks(audio, chunkMS)
    return chunks


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)
#filePath = "COMP261_2025_Lecture on 23_05_2025 (Fri)_default_054980a2.mp4"
filePath = file_path
fileName = file_path.split("/")[-1]

print(filePath)

audio = generateAudio(filePath)

os.makedirs("audioChunks", exist_ok=True)

print("initlaizing recognizer")
recognizer = sr.Recognizer()

with open("transcripts/Transcript_" + fileName + ".txt", "w", buffering=1) as file:
    print("Opened file")
    for i, chunk in enumerate(audio):
        chunk_filename = f"audioChunks_{i}.wav"
        chunk_path = os.path.join("audioChunks", chunk_filename)
        chunk.export(chunk_path, format="wav")

        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data)
                print(f"Chunk {i}: {text}")
                file.write("Minute" + str(i) + ": " + text + "\n")
            except sr.UnknownValueError:
                print(f"Chunk {i}: Could not understand audio / No Audio")
            except sr.RequestError as e:
                print(f"Chunk {i}: Could not request results from Google - API error")

"""
print("getting source")
with sr.AudioFile("audio.wav") as source:
    data = recognizer.record(source)

print("Googling source data")
text = recognizer.recognize_google(data)

print(text)

"""
