# WEB 03 - CSRF

## Lab 01: CSRF vulnerability with no defenses

![](image-1.png)

Vul ở chức năng thay đổi email


![](image.png)

Quan sát:
- Phiên đăng nhập được lưu trong cookie 
- Form change email không có giá trị csrf

=> có thể thực hiện được csrf (Bài lab này không có bất kỳ biện pháp bảo vệ csrf nào, vậy nên không cần test gì nhiều)

Tấn công:

B1: Bắt request thay đổi email:

![](image-2.png)

email thay đổi thành công có status code response: 302

B2: Sử dụng Generate CSRF Poc

![](image-3.png)

B3: Mở exploit-server, paste csrf poc vừa được generate vào body, ấn store và deliver exploit to victim

![](image-4.png)

<hr>

## Lab 02: CSRF where token validation depends on request method

![](image-5.png)

Vul ở chức năng thay đổi email

Quan sát:

![](image-6.png)

Bắt request load form
- Phiên nằm trong Cookie
- Khi send liên tiếp request ta thấy value csrf không đổi => csrf phụ thuộc vào phiên

Bắt request change email

![](image-7.png)

- Thay đổi method từ POST => GET

![](image-8.png)

- Kết quả đều trả về <b>302 found</b>

Tấn công:

Sử dụng Generate CSRF Poc với method GET

![](image-9.png)

Copy HTML và paste vào body của exploit-server

![](image-10.png)

![](image-11.png)

<hr>

## Lab 03: CSRF where token validation depends on token being present

VUL: Lab này tồn tại lỗ hổng tại chức năng thay đổi email, server không kiểm tra logic khi mã csrf được truyền vào là rỗng

Khi có mã csrf:

![](image-12.png)

>Kết quả 302 FOUND

Khi không có mã csrf

![](image-13.png)

>Kết quả cũng trả về 302 FOUND

Tấn công:

Sử dụng Generate Csrf Poc với tham số đầu vào không có mã csrf

![](image-14.png)

Copy HTML -> Paste vào body

![](image-15.png)

Store và Deliver exploit to victim

![](image-16.png)

<hr>

## Lab 04: CSRF where token is not tied to user session

Mã CSRF không bị ràng buộc với phiên của user

Lỗ hổng nằm ở vị trí thay đổi email

Có thể thấy khi bắt request show form change email, mã csrf bị thay đổi sau mỗi lần request => mã CSRF không bị ràng buộc với phiên của user => với mọi mã csrf được trả về và chưa dùng để request lần nào đều hợp lệ với mọi phiên của mọi user

request 1:

![](image-17.png)

request 2:

![](image-18.png)

Tấn công:

Dùng mã csrf của attacker (mã csrf này chưa được sử dụng) đưa vào form và gửi cho victim submit form đó 

Lẫy mã csrf lần đầu:

![](image-19.png)

Sử dụng Generate Csrf Poc

![](image-20.png)

Copy HTML -> Paste vào body

![](image-21.png)

Store và Deliver exploit to victim

![](image-22.png)

<hr>

## Lab 05: CSRF where token is tied to non-session cookie

Trong lab này, mã csrf bị ràng buộc bởi csrfKey trong cookie nhưng csrfKey lại không bị ràng buộc với phiên của user

Tấn công:

Lấy csrf-key và csrf của attacker chèn vào request và để victim submit

![](image-23.png)

Mã csrf chính là parameter có thể dễ dàng thay đổi

Nhưng csrfKey lưu trong cookie, để có thể thay đổi csrfKey ta cần tìm thêm 1 lỗ hổng khác cho phép thay đổi cookie của user. Lỗ hổng đó nằm ở vị trí tìm kiếm

![](image-24.png)

Những gì tìm kiếm sẽ được set vào cookie qua biến <b>LastSearchTerm</b>

Vậy việc cần làm là ngắt dòng để chèn thêm 1 cookie nữa chứa csrfKey

![](image-25.png)

Triển khai: Generate Csrf Poc

![](image-26.png)

![](image-27.png)

## Lab 06: CSRF where token is duplicated in cookie

Mã csrf trên form change email được xác thực bằng cách so sánh với mã csrf trong cookie, khi 2 chuỗi giống nhau => csrf token valid. 2 chuỗi không giống nhau => csrf token invalid

Và việc mã csrf khi thay đổi tùy ý mà vẫn thành công chứng tỏ mã csrf không phụ thuộc vào phiên

![](image-28.png)

Tương tự như <a href="#lab-05-csrf-where-token-is-tied-to-non-session-cookie">Lab 05</a> Lỗ hổng cho phép thay đổi csrf trong cookie tại chức năng search

![](image-29.png)

Sử dụng Generate Csrf Poc

![](image-30.png)

![](image-31.png)

![](image-32.png)

<hr>

## Lab 07: SameSite Lax bypass via method override

Lỗ hổng cho phép ghi đè method request

Thay vì submit form thì chỉ cần click vào link của attack

Trước:

![](image-33.png)

Sau:

![](image-34.png)

Solve:

![](image-35.png)

![](image-36.png)

<hr>

## Lab 08: SameSite Strict bypass via client-side redirect

Lab này được đặt SameSite Strict trong cookie kể từ khi login, không cho phép gửi cookie ra ngoài SameSite

Tại chức năng change email cho phép method GET

![](image-37.png)

Sau khi comment 1 bài viết, sẽ được redirect tới <b>/post/comment/confirmation</b>

![](image-38.png)

Đọc source của <b>/post/comment/confirmation</b> phát hiện sử dụng nối chuỗi => có thể Path traversal tới chức năng change email (vì cùng method GET) để thay đổi email

![](image-39.png)

Solve:

![](image-40.png)

![](image-41.png)

<hr>

## Lab 09: SameSite Strict bypass via sibling domain

