from playsound import playsound

# Play the audio file
audio_file = "path_to_your_audio_file.wav"  # Replace with the actual path
playsound(audio_file)


audio_file =  "Azan (Hijaz).mp3"
azan = AudioSegment.from_file(audio_file)
play(azan)
