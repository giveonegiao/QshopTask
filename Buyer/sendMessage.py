import requests
url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"#来自干文档
#APIID
account="C66356113"
#APIKEY
password="da6834a4eda93bd7caa9611565010fcd"
mobile="17863113269"
content="您的验证码是：666666。请不要把验证码泄露给其他人。"
headers={
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
data={
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
response=requests.post(url,headers = headers,data=data)
print(response.content.decode())