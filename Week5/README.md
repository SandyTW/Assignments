Week 5 Assignment 
======
要求三:基本的 SQL 指令
------

* 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和 password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。  
  ```
  INSERT INTO user VALUES(1, 'ply', 'ply', 'ply', default);
  ```
* 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。  
  ```
  SELECT * FROM user;
  ```
  ![image width = '300%'](https://user-images.githubusercontent.com/77286388/112092774-27619900-8bd3-11eb-9f28-0f0529a2a5df.png)
  
* 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。
  ```
  SELECT COUNT(id) FROM user;
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112415326-9e776880-8d5e-11eb-87d5-0a028aa4e69d.png)

* 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。
  ```
  SELECT * FROM user ORDER BY time DESC;
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112278422-c6fb5600-8cbd-11eb-861c-ef6c7aaa064a.png)

* 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。(Note. 按照時間排序之後的第 2 ~ 4 筆資料，所以不一定和 id 的數字排序一樣，)
  ```
  SELECT * FROM user ORDER BY time DESC LIMIT 1,3;
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112564282-f45b1780-8e15-11eb-9f19-d7150874a550.png)


* 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。
  ```
  SELECT * FROM user WHERE username = 'ply';
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112094603-955b8f80-8bd6-11eb-9f83-be1f600cc71e.png)
  
* 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。
  ```
  SELECT * FROM user WHERE username = 'ply' AND password = 'ply';
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112094982-bcb25c80-8bd6-11eb-8630-e3948f5a291b.png)

* 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。
  ```
  UPDATE user SET name = '丁滿' WHERE username = 'ply';
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112095544-a789fd80-8bd7-11eb-89cd-caaff0b915de.png)
  
* 使用 DELETE 指令刪除所有在 user 資料表中的資料。
  ``` 
  DELETE FROM user;
  ``` 
  ![image](https://user-images.githubusercontent.com/77286388/112115365-107f6e80-8bf4-11eb-8714-5ee55ebfe66f.png)
    
要求四:結合資料表 SQL JOIN 的操作 
------
* 使用 SELECT 搭配 JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名。
  ```
  SELECT message.id, message.user_id, user.name, message.content, message.time
  FROM message 
  INNER JOIN user on message.user_id = user.id;
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112252344-ea130f00-8c97-11eb-8b38-259f0e930240.png)

  
* 使用 SELECT 搭配 JOIN 的語法，取得 user 資料表中欄位 username 是 ply 的所有留言，資料中須包含留言會員的姓名。
  ```
  SELECT message.id, message.user_id, user.name, message.content, message.time 
  FROM message INNER JOIN user on message.user_id = user.id
  WHERE user.username = 'ply';
  ```
  ![image](https://user-images.githubusercontent.com/77286388/112252376-f72ffe00-8c97-11eb-9320-7959c04e4856.png)





  
  

