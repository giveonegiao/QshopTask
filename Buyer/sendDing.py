import json
import requests

url="https://oapi.dingtalk.com/robot/send?access_token=2d227acf9a074f360d4f1c6988b700d34a661455daf338fb030e6c10ad054d34"


headers={
    "Content-Type":"application/json",
    "Charset":"utf-8"
}

requests_data={
    "msgtype": "text",
    "text": {
        "content": "百因必有果，你的报应就是我"
    },
    "at": {
        "atMobiles": [
        ],
        "isAtAll": True
    }

}
sendData = json.dumps(requests_data)

response = requests.post(url = url,headers = headers, data = sendData)

content = response.json()

print(content)
