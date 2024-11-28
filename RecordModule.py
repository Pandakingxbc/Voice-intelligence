import pyaudio
import wave
import keyboard

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
FILE = 'question.mp3'
press = 'space'


def setPressKey(key):
    global press
    press = key


def Record(file):
    FILE = file
    p = pyaudio.PyAudio()  # 初始化
    print('Recording ON, press ' + press + ' to stop Recording')

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # 创建录音文件
    frames = []
    while True:
        if keyboard.is_pressed(press):
            break
        data = stream.read(CHUNK)
        frames.append(data)  # 开始录音

    print("Recording OFF")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(FILE, 'wb')  # 保存
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()