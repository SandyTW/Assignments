Week 5 Assignment 要求三:基本的 SQL 指令
-----

* 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和 password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。<br>
  INSERT INTO user VALUES(1, 'ply', 'ply', 'ply', default);

* 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。<br>
  SELECT * FROM user;

  ![image](https://user-images.githubusercontent.com/77286388/112092774-27619900-8bd3-11eb-9f28-0f0529a2a5df.png)

* 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。<br>
  SELECT COUNT(username) FROM user;
  
  ![image](https://user-images.githubusercontent.com/77286388/112093355-3ac13400-8bd4-11eb-8486-d48a0be1939b.png)

* 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。<br>
  SELECT * FROM user ORDER BY time;
  
  ![image](https://user-images.githubusercontent.com/77286388/112093866-26ca0200-8bd5-11eb-94cf-c705f464e005.png)

* 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。<br>
  SELECT * FROM user WHERE id BETWEEN 2 AND 4;
  
  ![image](https://user-images.githubusercontent.com/77286388/112094477-4c0b4000-8bd6-11eb-84fd-6f35f244e00c.png)
  
* 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。<br>
  SELECT * FROM user WHERE username = 'ply';
  
  ![image](https://user-images.githubusercontent.com/77286388/112094603-955b8f80-8bd6-11eb-9f83-be1f600cc71e.png)
  
* 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。<br>
  SELECT * FROM user WHERE username = 'ply' AND password = 'ply';
  
  ![image](https://user-images.githubusercontent.com/77286388/112094982-bcb25c80-8bd6-11eb-8630-e3948f5a291b.png)

* 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。<br>
  UPDATE user SET name = '丁滿' WHERE username = 'ply';

  ![image](https://user-images.githubusercontent.com/77286388/112095544-a789fd80-8bd7-11eb-89cd-caaff0b915de.png)
  
* 使用 DELETE 指令刪除所有在 user 資料表中的資料。<br>
   DELETE FROM user;
   
   ![image](https://user-images.githubusercontent.com/77286388/112115365-107f6e80-8bf4-11eb-8714-5ee55ebfe66f.png)

  
  

