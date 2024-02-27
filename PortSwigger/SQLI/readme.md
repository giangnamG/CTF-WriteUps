# WEB 01: SQL Injection

## Lab 01: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

![](image.png)

## Lab 02: SQL injection vulnerability allowing login bypass

![](image-1.png)

## Lab 03: SQL injection attack, querying the database type and version on Oracle

![](image-2.png)

## Lab 04: SQL injection attack, querying the database type and version on MySQL and Microsoft

![](image-3.png)

## Lab 05: SQL injection attack, listing the database contents on non-Oracle databases

Cách 1: Không tools

B1: Tìm kiếm bảng chứa users

![](image-4.png)

=> Users table: <b>users_xzgekf</b>

B2: Tìm kiếm tên các cột trong bảng <b>users_xzgekf</b>

![](image-5.png)

Tìm được 2 cột: <b>username_tiahyp</b> và <b>password_pxnxwo</b>

B3: Tìm account admin trong table <b>users_xzgekf</b>

![](image-6.png)

>administrator: mbxe01j7vfka2mpc8705

Cách 2: Sử dụng Sqlmap

Payload:

```powershell
python .\sqlmap.py -u "https://0a1700dc041359d981a75ce500fb0000.web-security-academy.net/filter?category=" -p "category" --dbs --dump
```
Kết quả:

![](image-7.png)

## Lab 06: SQL injection attack, listing the database contents on Oracle

Cách 1: Không tools

Detect ra được csdl là Oracle 

![](image-8.png)

Sử dụng cú pháp sau để dump bảng và cột, cách làm tương tự như <a href="#lab-05-sql-injection-attack-listing-the-database-contents-on-non-oracle-databases">Lab 05</a>
```sql
SELECT table_name FROM all_tables
SELECT column_name FROM all_tab_columns
```
Cách 2: Sử dụng Sqlmap

Payload:
```powershell
python .\sqlmap.py -u "https://0aa2003104116239814557ce00ed001d.web-security-academy.net/filter?category=" -p "category" --dbms=oracle --dump
```
Kết quả:

![](image-9.png)

## Lab 07: SQL injection UNION attack, determining the number of columns returned by the query

Tìm được số cột là 3

![](image-10.png)

## Lab 08: SQL injection UNION attack, finding a column containing text

![](image-12.png)

## Lab 09: SQL injection UNION attack, retrieving data from other tables

![](image-13.png)

## Lab 10: SQL injection UNION attack, retrieving multiple values in a single column

Để retrieving nhiều giá trị từ 1 cột, sử dụng phép nối chuỗi

![](image-14.png)

Csdl sử dụng PostgreSQL => sử dụng cú pháp nối chuỗi của PostgreSQL

![](image-15.png)

## Lab 11: Blind SQL injection with conditional responses

Ứng dụng sử dụng TrackingId trong cookie để theo dõi người dùng khi họ truy cập. 

Nếu TrackingId có trong DB => Thông báo <b>Welcome Back!</b><br>
Ngược lại, không có thông báo nào!

### [DETECT]

![](image-16.png)

Bài cho 1 bảng <b>users</b> có cột <b>username</b> và <b>password</b>. Trong có username=<b>administrator</b>

### [TEST]

![](image-17.png)

Sử dụng <b>Intruder</b> để BruteForce password

![](image-18.png)

Xác định được <b>password</b> dài 20 ký tự

Payload:

![](image-19.png)

Kết quả:

![](image-20.png)

Sắp xếp theo thứ tự từ 1->20 ta được password:

> yjuxiq7m8wg9emo8o8tj

![](image-21.png)

![](image-22.png)

## Lab 12: Blind SQL injection with conditional errors

Lỗ hổng nằm ở <b>TrackingId</b>

![](image-23.png)

Nếu sai cú pháp, server trả về 500, ngược lại đúng trả về 200

Sử dụng kỹ thuật <b>conditional errors</b>

![](image-26.png)


