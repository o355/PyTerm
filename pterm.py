exeversion = False
# ;)
#Python Terminal - v2.0-indev
#THIS IS AN INDEV BUILD. EXPECT BROKEN AND UNTESTED STUFF.

#LEAVE THIS PART IN FOR CREDITS, AND YOU ARE FREE TO DO WHATEVER UNDER THE LICENSE:
#originally found on GitHub: github.com/o355/pyterm
#fully coded and designed by o355.
#(c) 2016 under the MIT license.

#This part is for checking essential components of PyTerm. It gets 100% handled.
#Beyond here is just importing stuff for the functions of PyTerm.
print("Python Terminal - Version 2.0 (In Development)")
print("Built on INDEV VERSION")
print("Starting up...")
print("Beginning pre-load...")
print("Pre-Load | Importing time...")
#We now handle importing with a try/handle.
#Before we import sys we have to raise the error, instead of sys.exit().
try:
    import time
except ImportError:
    raise ImportError("You don't have time! Please install time to run PyTerm.")
print("Pre-Load | Imported time!")
print("Pre-Load | Starting clock for load time/uptime...")
entireload = time.time()
print(round(time.time() - entireload,4), "| Pre-load complete, clock for load time/uptime loaded!")
print(round(time.time() - entireload,4), "| Now converting variable entireload from a float into an int through variable entireload_int...")
entireload_int = int(time.time() - entireload)
print(round(time.time() - entireload,4), "| Operation completed. Output from type(entireload_int):", type(entireload_int))
print(round(time.time() - entireload,4), "| Importing sys...")
try:
    import sys
except ImportError:
    raise ImportError("You don't have sys! Please install sys to run PyTerm.")
print(round(time.time() - entireload,4), "| Imported sys!")
print(round(time.time() - entireload,4), "| Importing gmtime from time...")
try:
    from time import gmtime
except ImportError:
    print("You don't have gmtime! Please install gmtime to run PyTerm.")
    sys.exit()
print(round(time.time() - entireload,4), "| Imported gmtime from time!")
print(round(time.time() - entireload,4), "| Importing os...")
try:
    import os
except ImportError:
    print("You don't have os! Please install os to run PyTerm.")
    sys.exit()
print(round(time.time() - entireload,4), "| Imported os!")
print(round(time.time() - entireload,4), "| Importing strftime from time...")
try:
    from time import strftime
except ImportError:
    print("You don't have strftime! Please install strftime to run PyTerm.")
    sys.exit()
print(round(time.time() - entireload,4), "| Imported strftime from time!")
print(round(time.time() - entireload,4), "| Importing platform...")
try:
    import platform
except ImportError:
    print("You don't have platform! Please install strftime to run PyTerm.")
    sys.exit()
print(round(time.time() - entireload,4), "| Imported platform!")
print(round(time.time() - entireload,4), "| Defining functions...")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)
def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.035)

def pterm_restart():
    exec(open(restart_prog).read())
print(round(time.time() - entireload,4), "| Defined functions: print_slow, print_fast!")
print(round(time.time() - entireload,4), "| Defining 4 variables...")
done = False
greeting2 = "Welcome to PyTerm,"
note1 = ""
note2 = ""
print(round(time.time() - entireload,4), "| Defined 4 variables!")
print(round(time.time() - entireload,4), "| Defining 3 functions, 3 variables, and reading/closing 3 files...")

greet = open('assets\\essential\\greeting.txt')
greeting = greet.read()
greet.close()

usernme = open('assets\\essential\\username.txt')
username = usernme.read()
usernme.close()

nme = open('assets\\essential\\name.txt')
name = nme.read()
nme.close()

print(round(time.time() - entireload,4), "| Defined 2 functions, 2 variables, and read/closed 2 files!")
print(round(time.time() - entireload,4), "| Defining 16 variables...")
note3 = ""
note4 = ""
note5 = ""
note6 = ""
note7 = ""
cmd = ""
promptver = "@pyterm-2.0-indev:~$ "
promptver2 = "pyterm-2.0-indev:~$ "
print(round(time.time() - entireload,4), "| Defined 8 of 17 varibles...")
place = ""
drink = ""
feeling = ""
num1 = ""
instructor = ""
action = ""
tell = ""
st = True
restart_prog = 'pterm.py'
print(round(time.time() - entireload,4), "| Defined 17 variables!")
print(round(time.time() - entireload,4), "| Defining version variables...")
help_ver = "2.0"
restart_ver = "1.0"
ping_ver = "0ms"
alwayssave_ver = "NUL"
uptime_ver = "1.0"
ascii_ver = "1.0.1"
time_ver = "1.0.1"
timer_ver = "1.1.1"
salesbuster_ver = "3.1-legacy"
notes_ver = "5.0"
coolthingz_ver = "1.3.3.7"
poem_ver = "1.3"
about_ver = "1.7"
farmstate_ver = "2.0.1-legacy"
setup_ver = "2.1"
shutdown_ver = "1.1"
madlibs_ver = "1.0"
textadventure_ver = "1.0.2"
cpubench_ver = "4.0"
vercheck_ver = "1.0"
sysinfo_ver = "1.0"
diagnosticsong_ver = "1.0"
clock_ver = "1.0"
print(round(time.time() - entireload,4), "| Defined version variables!")
print(round(time.time() - entireload,4), "| Defining version data variables...")
version = "2.0-indev"
aboutversion = "2.0 In Dev"
build = "no"
buildnumber = "no"
builddate = "no"
buildtype = "indev build"
lts_build = False
stable_build = False
beta_build = False
dev_build = True
print(round(time.time() - entireload,4), "| Startup finished! Welcome to PyTerm!")
print("")
print(greeting + " " + username + "!")
print("You are running PyTerm version " + version)
print("This is a beta build, and will be unfinished and unstable.")
print("The current date is", strftime("%A, %B %d, %Y. The time is %I:%M %p"))
print("Enter a command in the prompt below. Type help for help.")
while not done:
    cmd = input(username + promptver).lower()
    if cmd == "help":
        print(round(time.time() - entireload,4), "| Launching program: Help (version " + help_ver + ")")
        print("")
        print("PyTerm Commands:")
        print("help - Lists this command.")
        print("about - Lists information about this Python Terminal.")
        print("restart - Restarts PyTerm. Legendary.")
        print("shutdown - Shuts down the terminal.")
        print("madlibs - A little fun mad libs.")
        print("(BROKEN UNTIL BETA 4) setup - Sets up Python Terminal for you")
        print("notes - Launches the notes program")
        print("ascii - ASCII Art")
        print("farmstate - Prints out a poem about State Farm")
        print("poem - Prints out a Python poem")
        print("textadventure - You venture into Shia's forest. It doesn't end well.")
        print("salesbuster - Launches you into a great game called Sales Buster.")
        print("uptime - Best way to check your uptime of PyTerm.")
        print("(COMING IN BETA 5) securenotes - Notes, but somewhat more secure.")
        print("(COMING IN BETA 5) lock - Locks PyTerm.")
        print("(COMING IN BETA 6) reset - Resets PyTerm.")
        print("(COMING IN BETA 6) oldprograms - Old programs!")
        print("(COMING IN BETA 7) whattypeofbuildisthisbuildofpyterm - ")
        print("--- Diagnostic Tools --- ")
        print("cpubench - Benchmarks your CPU, now highly improved!")
        print("diagnosticsong - A very diagnostic song.")
        print("vercheck - Lists all program versions that are included with PyTerm.")
        print("sysinfo - Prints system information.")
        print("ping - I'm pretty sure this tool helps you fix network issues. Not sure honestly.")
        cmd = ""
        continue
    elif cmd == "diagnosticsong":
        print(round(time.time() - entireload,4), "| Launching program: Diagnostic Song (version " + diagnosticsong_ver + ")")
        print("")
        cmd = ""
        print("This program downloads a .wav file (that's completely harmless) from my website (owenthe.ninja), and we recommend you lower your computer volume.")
        print("(so when the song plays, you get the best experience)")
        print("If you want to really see what's going on, check the code (GitHub, local file). And you'll see nothing much, honestly.")
        print("If you'd like to quit, do Control+C in the Python window.")
        print("Starting in 5 seconds.")
        time.sleep(5)
        print("Doing stuff. Please wait!")
        diagnosticsong_filecheck = os.path.isfile('assets//diagnosticsong//song.wav')
        def diagnosticsong_songplay():
            print("Importing necessary libraries...")
            try:
                import pyaudio
            except ImportError:
                print("Yikes! pyaudio isn't installed. Please install it to run this program!")
                continue
            try:
                import wave
            except ImportError:
                print("Yikes! wave isn't installed. Please install it to run this program!")
                continue
            print("Now playing the song...")
            chunk = 1024
            f = wave.open(r"assets//diagnosticsong//song.wav","rb")
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
            print("Terminating now, keep the file assets//diagnosticsong//song.wav so you don't have to download the song again!")
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
            with urllib.request.urlopen('http://owenthe.ninja/ptermstuff/song.wav') as response, open('assets//diagnosticsong//song.wav', 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            diagnosticsong_songplay()
            continue
        elif diagnosticsong_filecheck == True:
            diagnosticsong_songplay()
            continue
        continue
    elif cmd == "sysinfo":
        print(round(time.time() - entireload,4), "| Launching program: System Information (version " + sysinfo_ver + ")")
        print("")
        cmd = ""
        print("Predefining a few variables, this shouldn't take long.")
        sysinfo_system = platform.system()
        sysinfo_release = platform.release()
        sysinfo_version = platform.version()
        print("System information:")
        print("Machine type: " + platform.machine())
        print("Computer name: " + platform.node())
        print("Processor name: " + platform.processor())
        print("OS information: " + sysinfo_system + " " + sysinfo_release + " (version " + sysinfo_version + ")")
        print("OS specific information:")
        #Only tested on win32/debian (aka linux).
        if sys.platform.startswith('linux'):
            print(str(platform.linux_distribution(full_distrubiton_name=1)))
            print("Key: Distribution Name, Version, ID (codename) of the version")
            continue
        elif sys.platform.startswith('win32'):
            print(str(platform.win32_ver()))
            print("Key: Release, Version, Service Pack, OS type (multi/single procesor) and Debugging Code check")
            continue
        elif sys.platform.startswith('darwin'):
            print(str(platform.mac_ver()))
            print("Key: Release, Version, Dev Stage, Non Release Version, Machine")
            continue
        else:
            print("Can't get detailed information for your operating system.")
            print("But that's pretty rad you're using an uncommon OS ;)")
            continue
        continue
    elif cmd == "vercheck":
        print(round(time.time() - entireload,4), "| Launching program: Veriable Check (version " + vercheck_ver + ")")
        print("")
        cmd = ""
        print("Printing versions for all PyTerm programs...")
        print("Help: version " + help_ver)
        print("Restart: version " + restart_ver)
        print("Ping: version " + ping_ver)
        print("Always Save: version " + alwayssave_ver)
        print("Uptime: version " + uptime_ver)
        print("ASCII: version " + ascii_ver)
        print("Time: version " + time_ver)
        print("Timer: version " + timer_ver)
        print("Sales Buster: version " + salesbuster_ver)
        print("Notes: version " + notes_ver)
        print("Cool Thingz: version " + coolthingz_ver)
        print("Poem: version " + poem_ver)
        print("About: version " + about_ver)
        print("Farm State: version " + farmstate_ver)
        print("Setup: version " + setup_ver)
        print("Shut Down: version " + shutdown_ver)
        print("Mad Libs: version " + madlibs_ver)
        print("Text Adventure: version " + textadventure_ver)
        print("CPU Bench: version " + cpubench_ver)
        print("Version Check: version " + vercheck_ver)
        print("System Information: version " + sysinfo_ver)
        print("Diagnostic Song: version " + diagnosticsong_ver)
        print("Clock: version " + clock_ver)
        print("Done!")
        continue
    elif cmd == "restart":
        restart_ver = "1.0"
        print(round(time.time() - entireload,4), "| Launching program: Restart (version " + restart_ver + ")")
        print("")
        print("Restarting PyTerm...")
        exec(open(restart_prog).read())
    elif cmd == "ping":
        ping_ver = "0ms"
        print(round(time.time() - entireload,4), "| Launching program: Ping (version " + ping_ver + ")")
        try:
            from random import randint
        except ImportError:
            print("Sorry! randint isn't installed. Please install randint to run this program!")
            continue
        print("")
        ping_score = 0
        ping_mistakes = 0
        ping_loop = False
        while not ping_loop:
            ping_int = randint(0, 3)
            ping_input = input("Do you ping, or do you pong? ").lower()
            if (ping_input == "ping" and ping_int == 0):
                print("Your ball went missing.")
                print("Your score:", ping_score)
                break
            elif (ping_input == "ping" and ping_int == 1):
                print("Hurrah! Let's keep pinging.")
                ping_score = ping_score + 1
                continue
            elif (ping_input == "ping" and ping_int == 2):
                print("The song Bring Me to Life plays in the background...")
                print("Your score:", ping_score)
                break
            elif (ping_input == "ping" and ping_int == 3):
                print("Hurrah! Let's keep pinging.")
                ping_score = ping_score + 1
                continue
            elif (ping_input == "pong" and ping_int == 0):
                print("Hurrah! Let's keep ponging.")
                ping_score = ping_score + 1
                continue
            elif (ping_input == "pong" and ping_int == 1):
                print("Error 500.")
                print("Your score:", ping_score)
                break
            elif (ping_input == "pong" and ping_int == 2):
                print("Hurrah! Let's keep ponging.")
                ping_score = ping_score + 1
                continue
            elif (ping_input == "pong" and ping_int == 3):
                print("Creative message for why you lost goes here.")
                print("Your score:", ping_score)
                break
            elif ping_mistakes == 10:
                print("Stop making so many mistakes.")
                print("")
                break
            else:
                print("Did you read the instructions?")
                ping_mistakes = ping_mistakes + 1
                print("")
                continue
        continue
    elif cmd == "alwayssave":
        alwayssave_ver = "NUL"
        print(round(time.time() - entireload,4), "| Launching program: Always Save (version " + alwayssave_ver + ")")
        print("")
        print("That's what happened to me.")
        print("I was working on PyTerm, in IDLE for Python.")
        print("Forced off my computer, thanks to Windows Updates.")
        print("When I logged back in, PyTerm was about 50,000 NULs.")
        print("So, now, everything gets saved to GitHub.")
        print("I ask you to always save. In multiple locations.")
        print("Please do.")
        print("A PSA from me.")
        cmd = ""
        continue
    elif cmd == "uptime":
        uptime_ver = "1.0"
        print(round(time.time() - entireload,4), "| Launching program: Uptime (version " + uptime_ver + ")")
        print("")
        entireload_int = int(time.time() - entireload)
        m, s = divmod(entireload_int, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print(strftime("%H:%M:%S") + " up %d days, %02d:%02d:%02d" % (d, h, m, s))
        cmd = ""
        continue
    elif cmd == "ascii":
        print(round(time.time() - entireload,4), "| Launching program: ASCII Art (version " + ascii_ver + ")")
        print("")
        print("The original ASCII art from startup.")
        print("You served us extremely well.")
        print("|===========| |           |")
        print("|           |  |         |")
        print("|           |   |       |")
        print("|           |    |     |  ")
        print("|           |     |   |")
        print("|           |      | |")
        print("|           |       |")
        print("|============       |")
        print("|                   |")
        print("|                   |")
        print("|                   |")
        print("|    P Y T H O N    |")
        print("|                   |")
        print("|                   |")
        print("|                   |")
        print("")
        print("=============================")
        print("|    \                      |")
        print("|     \                     |")
        print("|      \                    |")
        print("|       \                   |")
        print("|        \                  |")
        print("|         |                 |")
        print("|        /                  |")
        print("|       /                   |")
        print("|      /                    |")
        print("|     /    T E R M I N A L  |")
        print("|    /     ---------------  |")
        print("   " + version + "           ")
        print("=============================")
    elif cmd == "time":
        print(round(time.time() - entireload,4), "| Launching program: Current Time (version " + time_ver + ")")
        print("")
        print("Time will be unsupported in Beta 3.")
        print("Here is the current time:")
        print(strftime("%A, %B %d, %Y, %I:%M:%S %p"))
        cmd = ""
        continue
    elif cmd == "clock":
        print(round(time.time() - entireload,4), "| Launching program: Clock (version " + clock_ver + ")")
        print("")
        cmd = ""
        if sys.platform.startswith('win32'):
            print("Here is a lovely clock. Press Enter to head back to PyTerm.")
            try:
                import msvcrt
            except ImportError:
                print("msvcrt isn't installed. Install it to view this pretty clock!")
                continue
            while True:
                print(strftime("%A, %B %d, %Y, %I:%M:%S %p"), end="\r")
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 13:
                        print("")
                        break
        else:
            print("Support for Linux coming soon.")
            continue
        continue
    elif cmd == "timer":
        print(round(time.time() - entireload,4), "| Launching program: Timer (version " + timer_ver + ")")
        print("")
        print("Welcome to Timer!")
        print("Please input the amount of seconds (up to 1 decimal place) you want the timer to run below. Didn't mean to open up timer? Just input 0.")
        timer_secs = input("timer_secs-userinput@timer-prgm-" + promptver2)
        timer_secs = float(timer_secs)
        print("Starting timer. Timer will display how many seconds are left every 0.1 seconds.")
        timer_loop = False
        while not timer_loop:
            if timer_secs > 0:
                print(round(timer_secs, 2), "seconds remain.", end="\r")
                timer_secs = timer_secs - 0.1
                time.sleep(0.1)
                continue
            else:
                print("Beep boop beep! Timer is up.")
                break
    elif cmd == "salesbuster":
        print("Launching program: Legacy Notice for Program: Sales Buster (version " + salesbuster_ver + ")")
        print("")
        print("The program Sales Buster is unsupported.")
        print("You can find the old code in the folder:")
        print("legacycode\\salesbuster\\")
        print("Sales Buster was unsupported due to the lack of remaining knowledge on PyGame.")
        print("We're sorry for any issues this may have caused.")
        continue
    elif cmd == "coolthingz":
        print(round(time.time() - entireload,4), "| Launching program - Coolthingz (version " + coolthingz_ver + ")")
        print("")
        print("Fun fact: PyTerm (What was first known to be Gaming Terminal) was founded at a tech camp.")
        print("Fun fact: I made the entire base for PyTerm (basically the initial games and commands, and the style for how extra commands/games would be added) in around a day, 4-5 hours. The instructor was VERY impressed.")
        print("Fun fact: I think my instructor got pissed at me for going ham on my project")
        print("Fun fact: Python has been the only language I've gone after, and for one reason: It's simple. REALLY simple. 3 figures well paid.")
        print("Fun fact: I took a Unity and Java class later. Java is complex, and I don't know if I forgot Unity")
        print("Fun fact: Out of the 3 weeks that I scheduled for tech camp, I thought Python would be the most boring, I didn't look forward to it. Well look where it got me...")
        print("Fun fact: On the last day of camp (family presentations day), a Tornado Warning was issued during family presentations, and the power went out at the college were it was at.")
        print("The warning was issued at 3:40pm and we had to evacuate to a room 20 feet away that didn't have windows. On the way out back home trees were down and there was some local flooding")
        print("Fun fact: During that tornado warning, my good friend was going to his car in the worst of it, and his umbrella flew away. He said visibility was about 10 feet.")
        print("Fun fact: PyTerm was made (and still is made) with only a basic knowledge of how Python works, and Stack Overflow. I kid you not.")
        print("Fun fact: Originally, PyTerm was going to be named Gaming Terminal, in which you would launch games from the terminal. PyTerm has 3 games, but obviously got many other functions.")
        print("I ended up wanting to spruce up the terminal by adding some Linux-like commands, since I had a decent basic knowledge of Linux then (after my MC server switched to a VPS in late April 2016).")
        print("Fun fact: Once, the master indev build of PyTerm got corrupted. I lost a lot of progress. 8 hours, to be exact. PyTerm was 50,000 NUL NUL NULs. Such, the indev branch was created.")
        print("FYI: I don't have a Minecraft server anymore. I ask you NOT to spam my GitHub inbox with the question: What's the IP to ur MC server!!!!1???!!!")
        print("Fun fact: The old ASCII text was made in Notepad, and then I copy & pasted the print("" suffix and "") to the ASCII text afterwards.")
        prin
        cmd = ""
        continue
    elif cmd == "notes":
        print(round(time.time() - entireload,4), "| Launching program - Notes (version " + notes_ver + ")")
        print("")
        print("Notes has been redone now using a filesystem system. It's cool.")
        print("Welcome to Notes!")
        notes_done = False
        while not notes_done:
            print("Would you like to open, edit, clear, or exit?")
            notes_start = input("notes_start-userinput@notes-prgm-" + promptver2).lower()
            if notes_start == "open":
                notes_open = False
                while not notes_open:
                    print("Which note would you like to open? Enter a number between 1 and 10 (for note 1, note 2, etc.). Enter cancel to cancel.")
                    notes_open_input = input("notes_open_input-userinput@notes-prgm-" + promptver2).lower()
                    if notes_open_input == "1":
                        notes_n1 = open('assets\\notes\\note1.txt')
                        print("Note 1 output:")
                        print(notes_n1.read())
                        notes_n1.close()
                        break
                    elif notes_open_input == "2":
                        notes_n2 = open('assets\\notes\\note2.txt')
                        print("Note 2 output:")
                        print(notes_n2.read())
                        notes_n2.close()
                        break
                    elif notes_open_input == "3":
                        notes_n3 = open('assets\\notes\\note3.txt')
                        print("Note 3 output:")
                        print(notes_n3.read())
                        notes_n3.close()
                        break
                    elif notes_open_input == "4":
                        notes_n4 = open('assets\\notes\\note4.txt')
                        print("Note 4 output:")
                        print(notes_n4.read())
                        notes_n4.close()
                        break
                    elif notes_open_input == "5":
                        notes_n5 = open('assets\\notes\\note5.txt')
                        print("Note 5 output:")
                        print(notes_n5.read())
                        notes_n5.close()
                        break
                    elif notes_open_input == "6":
                        notes_n6 = open('assets\\notes\\note6.txt')
                        print("Note 6 output:")
                        print(notes_n6.read())
                        notes_n6.close()
                        break
                    elif notes_open_input == "7":
                        notes_n7 = open('assets\\notes\\note7.txt')
                        print("Note 7 output:")
                        print(notes_n7.read())
                        notes_n7.close()
                        break
                    elif notes_open_input == "8":
                        notes_n8 = open('assets\\notes\\note8.txt')
                        print("Note 8 output:")
                        print(notes_n8.read())
                        notes_n8.close()
                        break
                    elif notes_open_input == "9":
                        notes_n9 = open('assets\\notes\\note9.txt')
                        print("Note 9 output:")
                        print(notes_n9.read())
                        notes_n9.close()
                        break
                    elif notes_open_input == "10":
                        notes_n10 = open('assets\\notes\\note10.txt')
                        print("Note 10 output:")
                        print(notes_n10.read())
                        notes_n10.close()
                        break
                    elif notes_open_input == "cancel":
                        print("Aborted. Returning to program main menu.")
                        break
                    else:
                        print("Not a valid option.")
                        continue
            elif notes_start == "edit":
                notes_edit = False
                while not notes_edit:
                    # This program has to break unification, for obvious reasons. A warning is provided, don't hate. Now you will hate since I put this comment here.
                    print("Which note would you like to edit? Enter a number between 1 and 10 (for note 1, note 2, etc.). Enter cancel to cancel.")
                    notes_edit_input = input("notes_edit_input-userinput@notes-prgm-" + promptver2).lower()
                    if notes_edit_input == "1":
                        notes_n1fn = "assets\\notes\\note1.txt"
                        print("Edit Note 1 in the empty prompt below.")
                        notes_n1write = input("")
                        with open(notes_n1fn, 'a') as out:
                            out.write(notes_n1write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "2":
                        notes_n2fn = "assets\\notes\\note2.txt"
                        print("Edit Note 2 in the empty prompt below.")
                        notes_n2write = input("")
                        with open(notes_n2fn, 'a') as out:
                            out.write(notes_n2write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "3":
                        notes_n3fn = "assets\\notes\\note3.txt"
                        print("Edit Note 3 in the empty prompt below.")
                        notes_n3write = input("")
                        with open(notes_n3fn, 'a') as out:
                            out.write(notes_n3write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "4":
                        notes_n4fn = "assets\\notes\\note4.txt"
                        print("Edit Note 4 in the empty prompt below.")
                        notes_n4write = input("")
                        with open(notes_n4fn, 'a') as out:
                            out.write(notes_n4write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "5":
                        notes_n5fn = "assets\\notes\\note5.txt"
                        print("Edit Note 5 in the empty prompt below.")
                        notes_n5write = input("")
                        with open(notes_n5fn, 'a') as out:
                            out.write(notes_n5write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "6":
                        notes_n6fn = "assets\\notes\\note6.txt"
                        print("Edit Note 6 in the empty prompt below.")
                        notes_n6write = input("")
                        with open(notes_n6fn, 'a') as out:
                            out.write(notes_n6write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "7":
                        notes_n7fn = "assets\\notes\\note7.txt"
                        print("Edit Note 7 in the empty prompt below.")
                        notes_n7write = input("")
                        with open(notes_n7fn, 'a') as out:
                            out.write(notes_n7write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "8":
                        notes_n8fn = "assets\\notes\\note8.txt"
                        print("Edit Note 8 in the empty prompt below.")
                        notes_n8write = input("")
                        with open(notes_n8fn, 'a') as out:
                            out.write(notes_n8write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "9":
                        notes_n9fn = "assets\\notes\\note9.txt"
                        print("Edit Note 9 in the empty prompt below.")
                        notes_n9write = input("")
                        with open(notes_n9fn, 'a') as out:
                            out.write(notes_n9write + '\n')
                            out.close()
                            break
                        break
                    elif notes_edit_input == "10":
                        notes_n10fn = "assets\\notes\\note10.txt"
                        print("Edit Note 10 in the empty prompt below.")
                        notes_n10write = input("")
                        with open(notes_n10fn, 'a') as out:
                            out.write(notes_n10write + '\n')
                            out.close()
                            break
                        break
                    elif ninputedit2 == "cancel":
                        print("Aborted.")
                        break
                    else:
                        print("Not a valid option.")
                        continue

            elif notes_start == "clear":
                print("Clearing notes permanently deletes any data within a note.")
                print("Please be aware of this.")
                print("Which note would you like to delete? Enter a number between 1 and 10 (1 for Note 1, etc.), or enter cancel to cancel.")
                notes_clear = False
                while not notes_clear:
                    notes_clear_input = input("notes_clear_input-userinput@notes-prgm-" + promptver2).lower()
                    if notes_clear_input == "1":
                        notes_fName1 = "assets\\notes\\note1.txt"
                        open(notes_fName1, 'w').close()
                        print("Note 1 cleared.")
                        break
                    elif notes_clear_input == "2":
                        notes_fName2 = "assets\\notes\\note2.txt"
                        open(notes_fName2, 'w').close()
                        print("Note 2 cleared.")
                        break
                    elif notes_clear_input == "3":
                        notes_fName3 = "assets\\notes\\note3.txt"
                        open(notes_fName3, 'w').close()
                        print("Note 3 cleared.")
                        break
                    elif notes_clear_input == "4":
                        notes_fName4 = "assets\\notes\\note4.txt"
                        open(notes_fName4, 'w').close()
                        print("Note 4 cleared.")
                        break
                    elif notes_clear_input == "5":
                        notes_fName5 = "assets\\notes\\note5.txt"
                        open(notes_fName5, 'w').close()
                        print("Note 5 cleared.")
                        break
                    elif notes_clear_input == "6":
                        notes_fName6 = "assets\\notes\\note6.txt"
                        open(notes_fName6, 'w').close()
                        print("Note 6 cleared.")
                        break
                    elif notes_clear_input == "7":
                        notes_fName7 = "assets\\notes\\note7.txt"
                        open(notes_fName7, 'w').close()
                        print("Note 7 cleared.")
                        break
                    elif notes_clear_input == "8":
                        notes_fName8 = "assets\\notes\\note8.txt"
                        open(notes_fName8, 'w').close()
                        print("Note 8 cleared.")
                        break
                    elif notes_clear_input == "9":
                        notes_fName9 = "assets\\notes\\note9.txt"
                        open(notes_fName9, 'w').close()
                        print("Note 9 cleared.")
                        break
                    elif notes_clear_input == "10":
                        notes_fName10 = "assets\\notes\\note10.txt"
                        open(notes_fName10, 'w').close()
                        print("Note 10 cleared.")
                        break
                    elif notes_clear_input == "cancel":
                        print("Aborted.")
                        break
                    else:
                        print("Not a valid option.")
                        continue
            elif notes_start == "exit":
                print("Now exiting notes.")
                break
    elif cmd == "poem":
        print(round(time.time() - entireload,4), "| Launching program: Poem (version " + poem_ver + ")")
        print("")
        poem_file = open('assets\\poem\\poem.txt')
        print(poem_file.read())
        poem_file.close()
        continue
    elif cmd == "about":
        print(round(time.time() - entireload,4), "| Launching program: About PyTerm (version " + about_ver + ")")
        print("")
        print("Python Terminal (PyTerm)")
        print("Version " + aboutversion)
        print("Coded in Python 3.2 and 3.5")
        print("Build date: " + builddate)
        print("Build number: " + buildnumber)
        print("Build type: " + buildtype)
        cmd = ""
        continue
    elif cmd == "farmstate":
        print("Launching program: Legacy Notice for Program: Farmstate (version " + farmstate_ver + ")")
        print("")
        print("The program Farmstate is unsupported.")
        print("You can find the old code in the folder:")
        print("legacycode\\farmstate")
        print("We're sorry for any issues this may have caused.")
        continue
    elif cmd == "setup":
        print("Launching program: Setup PyTerm (version " + setup_ver + ")")
        print("")
        print("Setup will be overhauled soon, to write to files.")
        print("So that happened.")
        continue
    elif cmd == "shutdown":
        print("Launching program: Shutdown PyTerm (version " + shutdown_ver + ")")
        print("")
        print("Shutting down...")
        cmd = ""
        sys.exit()
    elif cmd == "madlibs":
        print("Launching program: Mad Libs (version " + madlibs_ver + ")")
        print("")
        print_slow("\nWelcome to Mad Libs!")
        print_slow("\nPlease type in a name")
        madlibs_name = input("madlibs_name-userinput@madlibs-prgm-" + promptver2)
        print_slow("\nPlease type in a place")
        madlibs_place = input("madlibs_place-userinput@madlibs-prgm-" + promptver2)
        print_slow("\nPlease type in a drink")
        madlibs_drink = input("madlibs_drink-userinput@madlibs-prgm-" + promptver2)
        print_slow("\nPlease type in a feeling")
        madlibs_feeling = input("madlibs_feeling-userinput@madlibs-prgm-" + promptver2)
        print_slow("\nPlease enter a number")
        madlibs_num1 = input("madlibs_num1-userinput@madlibs-prgm-" + promptver2)
        print_slow("\nPlease enter an instructor from somewhere")
        madlibs_instructor = input("madlibs_instructor-userinput@madlibs-prgm-" + promptver2)
        print_slow("\nPlease enter an action you would take")
        madlibs_action = input("")
        print_slow("\nPlease enter something you would tell another person")
        madlibs_tell = input("")
        print_slow("\nYour Mad Libs is finished. We're now making your Mad Libs.")
        print_slow("\nYou were with Xan. You were walking with Xan. Xan says to you: Hey, " + name + ", want to go somewhere? You say: Sure! Let's go to " + place + "! Xan says, Maybe while we are there, we should get a drink of " + drink + ". You said: That sounds " + feeling + "!")
        print_slow("\nAbout " + num1 + " hours later...")
        print_slow("\nYou were still walking with Xan. All of a sudden, a random " + instructor + " comes out of the middle of nowhere! You " + action + ". " + instructor + " says to you: Hey, " + name + ", watcha doin with Xan? You respond with " + tell + ". " + instructor + " says to you: Oh, ok! Sounds cool! Have fun!")
        print_slow("\nAnd " + name + " and Xan went happily ever after into the sunset.")
        cmd = ""
        print("\nExiting Mad Libs, thanks for playing.")
        continue
    elif cmd == "textadventure":
        print("")
        textadventure = False
        #Unification breaks here (as all the vars are prefixed with ta_ and not textadventure_.
        #Like I'm going through 40 variables to fix that? no.
        print("Launching program: Text Adventure (version " + textadventure_ver + ")")
        print("")
        print_slow("\nWelcome to the adventures of a person walking through a forest, that being you. How cool.")
        print_slow("\nTo exit, at any text prompt, type exit. Exiting will NOT stop pyterm, just restart it.")
        print_slow("\nInputs are now case insensitive.")
        print_slow("\nSelect your character name here:")
        ta_charname = input("ta_charname-userinput@textadventure-prgm-" + promptver2)
        print_slow("\nAlright, " + ta_charname + "! Let's get started.")
        print_slow("\nYou find yourself in a forest. You sit on the ground, after sleeping for an entire night. What do you do now?")
        print_slow("\nYour options: Keep sitting on the ground, Get up and walk around")
        print_slow("\nWhat do you do?")
        ta_d1 = input("ta_d1-userinput@textadventure-prgm-" + promptver2).lower()

        while not textadventure:
            if ta_d1 == "keep sitting on the ground":
                print_slow("\nYou just keep sitting there. You fall asleep after waking up.")
                print_slow("\nYou wake up 30 minutes later.")
                print_slow("\nIn front of you, is Shia LeBeouf.")
                print_slow("\nWhat do you do now?")
                print_slow("\nYour options: Run for your life, Try to meet Shia LaBeouf")
                ta_2 = False
                print_slow("\nWhat do you do")
                ta_d2 = input("ta_d2-userinput@textadventure-prgm-" + promptver2).lower()
                while not ta_2:
                    if ta_d2 == "run for your life":
                        print_slow("\nYou run really fast. Shia LaBeouf tries to keep up with you, but fails.")
                        print_slow("\nAfter a little walking, you stumble upon a human trail, and know it's the trail you came on.")
                        print_slow("\nYet, there's a catch. You forgot which way you went to get here. What do you do now?")
                        print_slow("\nYour options: Go left on the trail, Go right on the trail")
                        ta_4 = False
                        print_slow("\nWhat do you do?")
                        ta_d4 = input("ta_d4-userinput@textadventure-prgm-" + promptver2).lower()
                        while not ta_4:
                            if ta_d4 == "go left on the trail":
                                print_slow("\nYou start heading left on the trail. You hike for about 6 hours.")
                                print_slow("\nAfter following the trail for about 6 hours, you finally get back to your car. It's 2pm.")
                                print_slow("\nYou made it out of Shia's forest. Good job.")
                                print("\nThis story has ended. To exit this program, PyTerm must be restarted.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            elif ta_d4 == "go right on the trail":
                                print_slow("\nYou begin hiking. But, you keep going up and up. You realize, this isn't the right way to go.")
                                print_slow("\nYou're running low on water and food, yet, there seems to be another trail that might go down the mountain.")
                                print_slow("\nWhat do you do now?")
                                print_slow("\nYour options: Turn around, Take the other trail.")
                                ta_5 = False
                                print_slow("\nWhat do you do?")
                                ta_d5 = input("ta_d5-userinput@textadventure-prgm-" + promptver2).lower()
                                while not ta_5:
                                    if ta_d5 == "turn around":
                                        print_slow("\nYou turn around, and head down the mountain.")
                                        print_slow("\nAfter 8 hours of intense hiking, you finally make it to your car.")
                                        print_slow("\nYou made it out of Shia's forest. Good job.")
                                        print("\nThis story has ended. To exit this program, PyTerm must be restarted.")
                                        print("Now restarting...")
                                        time.sleep(1)
                                        exec(open(restart_prog).read())
                                    elif ta_d5 == "take the other trail":
                                        print_slow("\nYou start taking the other trail. After 2 hours of upwards climbing, you start getting sleepy, and are very thirsty.")
                                        print_slow("\nYou decide to take a rest. Due to dehydration, you pass away in your sleep.")
                                        print_slow("\nYou died in Shia's forest.")
                                        print_slow("\nThe end.")
                                        print("\nThis story has ended. To exit this program, PyTerm must be restarted.")
                                        print("Now restarting...")
                                        time.sleep(1)
                                        exec(open(restart_prog).read())
                                    elif ta_d5 == "exit":
                                        print("Now exiting this program. To do so, PyTerm must be restarted.")
                                        print("Now restarting...")
                                        time.sleep(1)
                                        exec(open(restart_prog).read())
                                    else:
                                        print("Not a valid option. Options are: Turn around, Take the other trail")
                                        continue
                            elif ta_d4 == "exit":
                                print("Now exiting this program. To do so, PyTerm must be restarted.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            else:
                                print("Not a valid option. Options are: Go left on the trail, Go right on the trail.")
                    elif ta_d2 == "try to meet shia labeouf":
                        print_slow("\nYou say Hi to Shia LaBeouf. He says hi back.")
                        print_slow("\nShia decides to take you into his cabin. You walk with him.")
                        print_slow("\nShia makes you some pancakes. You talk with Shia for some time.")
                        print_slow("\nYou ask Shia for a trail map of the area, since you want to go back home. He agrees.")
                        print_slow("\nYou receive the trail map, but you notice something. It's a little out of date. You think it should have your trail back.")
                        print_slow("\nYour options: Use the trail map to get home, Ask if Shia has a newer trail map.")
                        ta_7 = False
                        print_slow("\nWhat do you do?")
                        ta_d7 = input("ta_d7-userinput@textadventure-prgm-" + promptver2).lower()
                        while not ta_7:
                            if ta_d7 == "use the trail map to get home":
                                print_slow("\nYou start to use the trail map to get home. As it turns out, the trail map contains all the trails needed to get home.")
                                print_slow("\nAfter an intense 5 hour hike going down the mountain, you finally get back to your car.")
                                print_slow("\nYou made it out of Shia's forest. Good job.")
                                print("\nThis story has ended. To quit this program, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            if ta_d7 == "ask if shia has a newer trail map":
                                print_slow("\nYou ask Shia for a newer trail map. He says that the map he gave you was the newest one.")
                                print_slow("\nHe said that there haven't been any trails made up in the forest for 8 years.")
                                print_slow("\nYou begin to follow the trails back to the trailhead. After 5 hours, you finally get back to your car.")
                                print_slow("\nYou made it out of Shia's forest. Good job.")
                                print("\nThis story has ended. To quit this program, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                    elif ta_d2 == "exit":
                        print("Now exiting this program. To do so, PyTerm must be restarted.")
                        print("Now restarting...")
                        time.sleep(1)
                        exec(open(restart_prog).read())
                    else:
                        print_slow("Not a valid option. Options are: Run for your life, Try to meet Shia LaBeouf.")

            elif ta_d1 == "get up and walk around":
                print_slow("\nYou feel a bit tired, but nonetheless, you get up and start walking")
                print_slow("\nYou stumble upon a little house that looks to have electricity and has the lights on.")
                print_slow("\nWhat do you do now?")
                print_slow("\nYour options: Follow the electricity line, try to go into the cabin")
                ta_3 = False
                print_slow("\nWhat do you do?")
                ta_d3 = input("ta_d3-userinput@textadventure-prgm-" + promptver2).lower()
                while not ta_3:
                    if ta_d3 == "follow the electricity line":
                        print_slow("\nYou follow the electricity line. You keep walking for hours on hours")
                        print_slow("\nAbout 3 hours later, you finally find a road where the electricity line heads to.")
                        print_slow("\nBut, here's the catch! It goes two ways. Which way do you go?")
                        print_slow("\nYour options: Go left, Go right")
                        ta_6 = False
                        print_slow("\nWhat do you do?")
                        ta_d6 = input("ta_d6-userinput@textadventure-prgm-" + promptver2).lower()
                        while not ta_6:
                            if ta_d6 == "go left":
                                print_slow("\nYou head left on the road. After a short amount of walking, you stumble upon a trailhead. And you see your car!")
                                print_slow("\nYou safely made it out of Shia's forest. Good job.")
                                print("\nThis story has ended. To quit this program, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            elif ta_d6 == "go right":
                                print_slow("\nYou start heading right on the road. After about 30 minutes. You see a sign for the trailhead you were just on.")
                                print_slow("\nAfter a little pondering, you start heading towards where the trailhead sign goes.")
                                print_slow("\nAfter another 30 minutes, you finally stumble upon the trailhead for the trail.")
                                print_slow("\nAnd just like that, you see your car.")
                                print_slow("\nYou safely made it out of Shia's forest. Good job.")
                                print("\nThis story has ended. To quit this program, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            elif ta_d6 == "exit":
                                print("\nNow exiting this program. To do so we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            else:
                                print("Not a valid option. Options are: Go left, Go right")
                    elif ta_d3 == "try to go into the cabin":
                        print_slow("\nYou head towards the cabin. You open the cabin door. And it's open.")
                        print_slow("\nRight at the kitchen table, eating some pancakes, you see Shia LaBeouf.")
                        print_slow("\nInternally, you freak out, but not externally. You need to do something.")
                        print_slow("\nYour options: Try to meet Shia LaBeouf, Quietly exit the cabin.")
                        ta_8 = False
                        print_slow("\nWhat do you do?")
                        ta_d8 = input("ta_d8-userinput@textadventure-prgm-" + promptver2).lower()
                        while not ta_8:
                            if ta_d8 == "try to meet shia labeouf":
                                print_slow("\nYou walk up to Shia LaBeouf, and you talk with Shia for a bit.")
                                print_slow("\nAs it turns out, Shia was a nice person. Shia accepts you into his family.")
                                print_slow("\nYou now live with Shia LaBeouf.")
                                print("\nThis story has ended. To quit this program, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            elif ta_d8 == "quietly exit the cabin":
                                print_slow("\nYou attempt to quietly exit the cabin. But...")
                                print_slow("\nShia LaBeouf catches you try to exit the cabin.")
                                print_slow("\nYou begin to have a conversation with Shia. Shia likes you.")
                                print_slow("\nShia accepts you into his family. You now live with Shia LaBeouf.")
                                print("\nThis story has ended. To quit this program, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            elif ta_d8 == "exit":
                                print_slow("\nNow exiting the program. To do so, we need to restart PyTerm.")
                                print("Now restarting...")
                                time.sleep(1)
                                exec(open(restart_prog).read())
                            else:
                                print_slow("\nThat's not a valid option. Options are: Try to meet with Shia LaBeouf, Quietly exit the cabin")
                    elif ta_d3 == "exit":
                        print_slow("\nNow exiting the program. To do so, we need to restart PyTerm.")
                        print("Now restarting...")
                        time.sleep(1)
                        exec(open(restart_prog).read())
                    else:
                        print("\nNot a valid option. Options are: Follow the electricity line, Try to go into the cabin.")
                        break

            elif ta_d1 == "exit":
                print_slow("\nNow exiting this program. Since this is the first loop, no restart is required!")
                break
            else:
                print("\nThat's not a valid option! Options are: Keep sitting on the ground, Get up and walk around")
                continue
    elif cmd == "cpubench":
        print("Launching program: CPU Bench (version " + cpubench_ver + ")")
        print("")
        print("Welcome to CPU Bench.")
        print("This test is comprised of your computer finding prime numbers.")
        print("We can run a very short, short, normal, or long test.")
        print("Which test would you like to run?")
        cpubench_benchselect = input("cpubench_benchselect-userinput@cpubench-prgm-" + promptver2).lower()
        if cpubench_benchselect == "very short":
            cpubench_start = 0
            cpubench_end = 10000
            cpubench_totaltime = time.time()
            print("Now starting...")
            for cpubench_num in range(cpubench_start,cpubench_end + 1):
                if cpubench_num > 1:
                    for i in range(2,cpubench_num):
                        if (cpubench_num % i) == 0:
                            break
                    else:
                        print("Now benchmarking... Elapsed time:", round(time.time() - cpubench_totaltime,4), "seconds. Prime found:", cpubench_num, end='\r')
            print("")
            print("Done! The benchmark took", round(time.time() - cpubench_totaltime,4), "seconds.")
            print("Baselines:")
            print("1.6416 seconds on an Intel Core i7 4650U")
            print("1.1354 seconds on an Intel Core i7 3615QM")
            print("1.2441 seconds on an Intel Pentium E5800")
            print("?? on an Intel Pentium 4")
            continue
        elif cpubench_benchselect == "short":
            cpubench_start = 0
            cpubench_end = 50000
            cpubench_totaltime = time.time()
            print("Now starting...")
            for cpubench_num in range(cpubench_start,cpubench_end + 1):
                if cpubench_num > 1:
                    for i in range(2,cpubench_num):
                        if (cpubench_num % i) == 0:
                            break
                    else:
                        print("Now benchmarking... Elapsed time:", round(time.time() - cpubench_totaltime,4), "seconds. Prime found:", cpubench_num, end='\r')
            print("")
            print("Done! The benchmark took", round(time.time() - cpubench_totaltime,4), "seconds.")
            print("Baselines:")
            print("30.5881 seconds on an Intel Core i7 4650U")
            print("22.1646 seconds on an Intel Core i7 3615QM")
            print("24.9308 seconds on an Intel Pentium E5800")
            print("?? on an Intel Pentium 4")
            continue
        elif cpubench_benchselect == "normal":
            cpubench_start = 0
            cpubench_end = 200000
            cpubench_totaltime = time.time()
            print("Now starting...")
            for cpubench_num in range(cpubench_start,cpubench_end + 1):
                if cpubench_num > 1:
                    for i in range(2,cpubench_num):
                        if (cpubench_num % i) == 0:
                            break
                    else:
                        print("Now benchmarking... Elapsed time:", round(time.time() - cpubench_totaltime,4), "seconds. Prime found:", cpubench_num, end='\r')
            print("")
            print("Done! The benchmark took", round(time.time() - cpubench_totaltime,4), "seconds.")
            print("Baselines:")
            print("?? on an Intel Core i7 4650U")
            print("306.5036 seconds on an Intel Core i7 3615QM")
            print("343.3961 seconds on an Intel Pentium E5800")
            print("?? on an Intel Pentium 4")
            continue
        elif cpubench_benchselect == "long":
            cpubench_start = 0
            cpubench_end = 500000
            cpubench_totaltime = time.time()
            print("Now starting...")
            for cpubench_num in range(cpubench_start,cpubench_end + 1):
                if cpubench_num > 1:
                    for i in range(2,cpubench_num):
                        if (cpubench_num % i) == 0:
                            break
                    else:
                        print("Now benchmarking... Elapsed time:", round(time.time() - cpubench_totaltime,4), "seconds. Prime found:", cpubench_num, end='\r')
            print("")
            print("Done! The benchmark took", round(time.time() - cpubench_totaltime,4), "seconds.")
            print("Baselines:")
            print("1764.9318 seconds on an Intel Core i7 4650U")
            print("1773.7427 seconds on an Intel Core i7 3615QM")
            print("1936.0202 seconds on an Intel Pentium E5800")
            print("?? on an Intel Pentium 4")
            continue
        else:
            print("Not a valid option. Valid options are: very short, short, normal, long")
            
            
        
    else:
        print("Not a valid command. Type in help to list all commands.")
