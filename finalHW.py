import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import content

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("leokypss95020@gmail.com", "vmbzdkncydjrdrmf")  #寄件者gmail,應用程式密碼
        content = MIMEMultipart()

        subject = '繳交作業'                        #Title
        subject=Header(subject, 'utf-8').encode()
        content["subject"] = subject

        content["from"] = "leokypss95020@gmail.com"     #寄件人
        content["to"] = "leokypss95020@gmail.com"       #收件人

        content.attach(MIMEText('吳歷軒'))  # 郵件純文字內容

        content.attach(MIMEImage(Path("299556.jpg").read_bytes()))  # 寄送圖片

        sendfile = open(r'1.py', 'rb').read()                       #夾帶附件
        annex = MIMEText(sendfile, 'base64', 'utf-8')
        annex["Content-Type"] = 'application/octet-stream'
        annex.add_header('Content-Disposition', 'attachment', filename='HW.txt') #能改檔案名稱
        content.attach(annex)

        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)