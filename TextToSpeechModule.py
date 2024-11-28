import requests
import json
import pyttsx3
from zhconv import convert


def TTS(input, type):
    url = "https://oa.api2d.net/v1/audio/speech"
    msg = []
    jsonBody = {}
    jsonBody["model"] = "tts-1"
    jsonBody['input'] = input
    jsonBody['voice'] = 'alloy'
    jsonBody['response_format'] = type
    payload = json.dumps(jsonBody)
    headers = {
        'Authorization': 'Bearer <fk229685-beJr0tzoQ3GASVO33m8CNQx4a4HCf2oR>',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    file = open('response.' + type, 'wb')
    file.write(response.content)
    file.close()
    # print(response.text)
    return response.content


def TTSLocal(text, language, rate, volume, filename, sayit=0):
    # 参数说明: 六个重要参数,阅读的文字,语言(0-英文/1-中文),语速,音量(0-1),保存的文件名(以.mp3收尾),是否发言(0否1是)
    text = convert(text, 'zh-hans')  # 转换字符串为简中
    engine = pyttsx3.init()  # 初始化语音引擎
    engine.setProperty('rate', rate)  # 设置语速
    # 速度调试结果:50戏剧化的慢,200正常,350用心听小说,500敷衍了事
    engine.setProperty('volume', volume)  # 设置音量
    voices = engine.getProperty('voices')  # 获取当前语音的详细信息
    if int(language) == 0:
        engine.setProperty('voice', voices[0].id)  # 设置第一个语音合成器 #改变索引，改变声音。0中文,1英文(只有这两个选择)
    elif int(language) == 1:
        engine.setProperty('voice', voices[1].id)
    if int(sayit) == 1:
        engine.say(text)  # pyttsx3->将结果念出来
    elif int(sayit) == 0:
        print("那我就不念了哈")
    engine.save_to_file(text, filename)  # 保存音频文件
    print(filename, "保存成功")
    engine.runAndWait()  # pyttsx3结束语句(必须加)
    engine.stop()  # pyttsx3结束语句(必须加)