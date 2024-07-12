import sounddevice
from scipy.io.wavfile import write
from playsound import playsound

print("Welcome! I am a voice recorder...")
while True:
    second=int(input("Enter the time in second : ").strip())
    fs=44100
    print("Recording Started... Speak!!")
    recorded_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    file=input("Enter the file name (example : voice1.wav): ")
    write(file,fs,recorded_voice)
    choice=input("Do you wanna record voice once more ? (Yes / No) : ")
    if choice.lower() == "no":
        break

def listenVoice(file):
    playsound(f"C:\\Users\\Biswajit Nag\\OneDrive\\Desktop\\python\\{file}")

temp=input("Do you wanna listen voice now (Yes / No) : ").strip()
if temp.lower() == "no":
    temp=False
else:
    temp=True

while temp:
    file=input("Enter the file name whom you wanna listen to : ")
    listenVoice(file)
    choice=input("Do you wanna listen more voices ? (Yes / No) : ")
    if choice.lower().strip() == "no":
        print("Thanks for using me... Come again")
        break