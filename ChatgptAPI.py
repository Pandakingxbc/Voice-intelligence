import requests
import json
import whisper

url = "https://oa.api2d.net/v1/chat/completions"
msg = []
jsonBody = {}
question = '你好'
background = '输入可能会出错，需要你自行纠正并理解。要求输出口语化，并加入一些语气词。你的回复尽量简短'
isMem = True
'input your own authorization, since it need money'

def rquestChatGpt(text):
    question = text
    msg.append({'role': 'system', 'content': background})
    msg.append({'role': 'user', 'content': question})
    jsonBody["model"] = "gpt-3.5-turbo-0613"
    jsonBody['messages'] = msg
    jsonBody['safe_mode'] = False
    jsonBody['max_tokens'] = 100
    payload = json.dumps(jsonBody)
    headers = {
        'Authorization': 'input your own authorization, since it need money',
        'User-Agent': 'Apifox/1.0.0 (https://openai.api2d.net)',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)
    response = response['choices'][0]['message']['content']
    if isMem == True:
        msg.append({'role': 'assistant', 'content': response})
    else:
        msg.clear()
        msg.append({'role': 'system', 'content': background})
    return response


def ClearMemory():
    msg.clear()
    msg.append({'role': 'system', 'content': background})


def SetMemory(flag=True):
    global isMem
    isMem = flag


def SetBackGround(str):
    global background
    background = str