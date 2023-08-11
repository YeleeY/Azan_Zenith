from playsound import playsound

audio_file =  "Azan (Hijaz).mp3"
azan = AudioSegment.from_file(audio_file)
play(azan)
