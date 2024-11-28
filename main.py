import RecordModule
import ChatgptAPI
import TextToSpeechModule
import SpeechToTextModule
import keyboard
from playsound import playsound


# 利用api2d接口实现的chatgpt语音对话，其中文本转语音是使用whisper库离线转的，而回复以及语音转文本则是使用了api2d的接口
if __name__ == '__main__':
    press = 'alt'
    confirmPress = 'enter'
    mode = 'debug mode'
    # 本地语音只支持中英文
    # 使用本地语音节省经费，但效果不如OPENAI
    isUseLocalSpeaker = "true"
    text = ''
    background = '输入给你的文字是通过其他语音转文本模型识别的，可能会出错，需要你自行纠正并理解，你输出的文字会转换为语音。要求输出口语化，并加入一些语气词'
    ChatgptAPI.SetBackGround(background)

    ChatgptAPI.SetMemory(flag=False)
    if mode == 'debug mode':
        print('press ' + press + ' to recording')
        while True:
            if keyboard.is_pressed(press):
                RecordModule.setPressKey(press)
                RecordModule.Record('question.mp3')
                text = SpeechToTextModule.STT('question.mp3')
                print('question:')
                print(text)
                if mode == 'debug mode':
                    text = input("修正内容：") or text
                    print(text)
                text = ChatgptAPI.rquestChatGpt(text)
                print('response:')
                print(text)
                if isUseLocalSpeaker == "true":

                    #  TextToSpeechModule.TTS(text, 'mp3')

                    # 本地文本转语音
                    TextToSpeechModule.TTSLocal(text=text, language=0, rate=300, volume=1, filename="respones.mp3",
                                                sayit=1)
                else:
                    TextToSpeechModule.TTS(text, 'mp3')
                    playsound('response.mp3')
                print('press ' + press + ' to recording')
            elif keyboard.is_pressed('esc'):
                break
    elif mode == 'text mode':
        while True:
            text = input("内容：") or text
            print(text)
            if text == 'esc':
                break
            text = ChatgptAPI.rquestChatGpt(text)
            print('response:')
            print(text)