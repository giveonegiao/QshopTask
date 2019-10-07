import smtplib
from email.mime.text import MIMEText

#构建邮件格式
subject="杨钊的学习邮件"
content="""
今天晚上七点交数学作业。
"""
sender="yzaifr@163.com"
recver="""1241141909@qq.com,
652253074@qq.com
"""
password="yz970507"

message=MIMEText(content,"plain","utf-8")
    #内容
    #内容类型
    #编码格式
message["Subject"]=subject
message["From"]=sender
message["To"]=recver

#发送邮件
smtp=smtplib.SMTP_SSL("smtp.163.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())
    #发送人
    #接收人 需要是一个列表[]
    #发送邮件  as_string是一种类似json的封装方式，目的是为了在协议上传输邮件
smtp.close()