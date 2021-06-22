<h3>build process:</h3>
這個final HW大致上是做Gmail API 的動作，我預設的情況是繳交作業，能夠上傳圖案，檔案之類的。
最重要的便是關於Gmail API的存取要求，才能使用外部裝置來傳送mail
我必須進入GOOGLE，取得印用程式密碼，這在程式中會運用在登入我的帳號
<br>
<img width="623" alt="1" src="https://user-images.githubusercontent.com/86303137/122943355-8937c780-d3a9-11eb-84e2-b3bde120df29.png">
<br>
<img width="503" alt="2" src="https://user-images.githubusercontent.com/86303137/122943724-d7e56180-d3a9-11eb-8279-eb2dd3a40691.png">
<br>

<h3>Introduction:</h3>
我原本是想要運用mail這個功能，來實現大量寄信給很多人，有點類似寄大量廣告郵件那樣，不過我目前找不到方法去實現如何獲取大量的郵件地址，且也不方便打饒陌生人，那麼只有用來寄送作業，或是請假附上證明文件的功用。
<br>

<h3>Details of the approach:</h3>
<img width="503" alt="2" src="https://user-images.githubusercontent.com/86303137/122943724-d7e56180-d3a9-11eb-8279-eb2dd3a40691.png">
<br>
這部分是信件的標題!!!
<img width="346" alt="螢幕擷取畫面 2021-06-22 222721" src="https://user-images.githubusercontent.com/86303137/122944424-6659e300-d3aa-11eb-90dd-c6210fd67bbe.png">
<br>
寫入寄件人和收件人
<img width="375" alt="4" src="https://user-images.githubusercontent.com/86303137/122944433-68bc3d00-d3aa-11eb-81dd-ecdcde2f608e.png">
<br>
這部分能夠管理我要寄送的文字內容，圖片以及夾帶附件
<img width="530" alt="5" src="https://user-images.githubusercontent.com/86303137/122944696-9ef9bc80-d3aa-11eb-8f29-7f6a498823f7.png">
<br>
最後整合content，寄出郵件
<img width="274" alt="6" src="https://user-images.githubusercontent.com/86303137/122945273-0dd71580-d3ab-11eb-817d-b34123f248bf.png">

<h3>Results:</h3>
這是我測試出來的結果，
寄信人和收件人都是我自己，能清楚的看到Title(繳交作業)、內文(姓名)、圖片以及檔案
![8](https://user-images.githubusercontent.com/86303137/122947087-783c8580-d3ac-11eb-9d66-acb4e26e9fda.jpg)


<h3>References:</h3>
https://developers.google.com/gmail/api/guides/sending
https://webb99.pixnet.net/blog/post/348000605-%E5%9C%A8-python-%E4%BD%BF%E7%94%A8-gmail-api-%E7%99%BC%E4%BF%A1
https://www.runoob.com/python/python-email.html
