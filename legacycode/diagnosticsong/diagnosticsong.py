# (c) 2016 o355.
# Should still mainly work.

print("")
cmd = ""
print("This program downloads a .wav file (that's completely harmless) from my website (owenthe.ninja), and we recommend you lower your computer volume.")
print("(so when the song plays, you get the best experience)")
print("If you want to really see what's going on, check the code (GitHub, local file). And you'll see nothing much, honestly.")
print("If you'd like to quit, do Control+C in the Python window.")
print("Starting in 5 seconds.")
time.sleep(5)
print("Doing stuff. Please wait!")
diagnosticsong_filecheck = os.path.isfile('assets//song.wav')
def diagnosticsong_songplay():
    print("Importing necessary libraries...")
    try:
        import pyaudio
    except ImportError:
        print("Yikes! pyaudio isn't installed. Please install it to run this program!")
        print("Restarting PyTerm...")
        pterm_restart()
    try:
        import wave
    except ImportError:
        print("Yikes! wave isn't installed. Please install it to run this program!")
        print("Restarting PyTerm...")
        pterm_restart()
    print("Now playing the song...")
    chunk = 1024
    f = wave.open(r"assets//song.wav","rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output = True)
    data = f.readframes(chunk)
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)
                            
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Hope the joke was a little funny at best ;)")
    print("Terminating now, keep the file assets//song.wav so you don't have to download the song again!")
    print("Returning to PyTerm.")
if diagnosticsong_filecheck == False:
    print("Importing necessary libraries...")
    try:
        import urllib.request
    except ImportError:
        print("Yikes! urllib.request isn't installed. Please install it to run this program!")
        continue
    try:
        import shutil
    except ImportError:
        print("Yikes! shutil isn't installed. Please install it to run this program!")
        continue
    print("Downloading the song...")
    with urllib.request.urlopen('http://owenthe.ninja/ptermstuff/song.wav') as response, open('assets//song.wav', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    diagnosticsong_songplay()
    continue
elif diagnosticsong_filecheck == True:
    diagnosticsong_songplay()
    continue
continue
