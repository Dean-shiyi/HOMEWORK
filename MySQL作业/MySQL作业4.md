设教学数据库Education有三个关系：
 
 ```
 CREATE DATABASE `Education` DEFAULT CHARACTER set utf8mb4 COLLATE utf8mb4_general_ci;
 ```
学生关系S（SNO，SNAME，AGE，SEX，SDEPT）；
 
 ```
 CREATE TABLE s(
id int(10) primary key auto_increment,
sno int(10),
sname VARCHAR(20) not null,
age int(10),
sex VARCHAR(20),
sdept VARCHAR(20)
);
 ```
学习关系SC（SNO，CNO，GRADE）；
 
 ```
 CREATE TABLE sc(
id int(10) PRIMARY key auto_increment,
sno int(10),
cno int(10),
grade int(10)
-- CONSTRAINT s_noid FOREIGN KEY(sno) REFERENCES s(sno),
-- CONSTRAINT c_noid FOREIGN KEY(cno) REFERENCES c(cno)
);
 ```
课程关系C（CNO，CNAME，CDEPT，TNAME）
 
 ```
 CREATE TABLE c(
id int(10) PRIMARY key auto_increment,
cno int(10),
cname VARCHAR(20),
cdept VARCHAR(10),
tname VARCHAR(10)
);
 ```
查询问题：

1：查所有年龄在20岁以下的学生姓名及年龄。
 
 ```
 SELECT sname,age FROM	s WHERE age < 20;
 ```
2：查考试成绩有不及格的学生的学号
 
 ```
 SELECT DISTINCT sno FROM sc WHERE grade < 60;
 ```
3：查所年龄在20至23岁之间的学生姓名、系别及年龄。
 
 ```
 SELECT sname,sdept,age FROM s WHERE age >20 and age <23;
 ```
4：查计算机系、数学系、信息系的学生姓名、性别。
 
 ```
 SELECT sname,sex FROM s WHERE sdept = '计算机系' or '数学系' or '信息系';
 ```
5：查既不是计算机系、数学系、又不是信息系的学生姓名、性别

 ```
 SELECT sname,sex FROM s WHERE sdept not in ('计算机系','数学系','信息系');
 ```
6：查所有姓“刘”的学生的姓名、学号和性别。

 ```
 SELECT sname,sno,sex FROM s WHERE sname LIKE '刘%';
 ```
 

7：查姓“上官”且全名为3个汉字的学生姓名。
 
 ```
 SELECT sname FROM s WHERE sname LIKE '上官_';
 ```
8：查所有不姓“张”的学生的姓名。
 
 ```
 SELECT sname FROM s WHERE sname not LIKE '张%';
 ```
9：查DB_Design课程的课程号。
 
 ```
 SELECT cno FROM c WHERE cname = 'DB_Design';
 ```
10：查缺考的学生的学号和课程号。
 
 ```
 SELECT sno,cno FROM sc WHERE grade is  null;
 ```
11：查年龄为空值的学生的学号和姓名。
 
 ```
 SELECT sno,sname FROM s WHERE age = null;
 ```
12：查计算机系20岁以下的学生的学号和姓名。
 
 ```
 SELECT sno,sname FROM s WHERE age < 20 and sdept = '计算机系';
 ```
13：查计算机系、数学系、信息系的学生姓名、性别。
 
 ```
 SELECT sname,sex FROM s WHERE sdept = '计算机系' or '数学系' or '信息系';
 ```
14：查询选修了C3课程的学生的学号和成绩，其结果按分数的降序排列。
 
 ```
 SELECT sc.sno,sc.grade FROM sc join c on sc.cno=c.cno WHERE c.cname='C3' ORDER BY sc.grade desc;
 ```
15：查询全体学生的情况，查询结果按所在系升序排列，对同一系中的学生按年龄降序排列。
 
 ```
 SELECT * FROM s ORDER BY sdept,age desc;
 ```
16：查询学生总人数。
 
 ```
 SELECT COUNT(*) as total_num FROM s;
 ```

17：查询选修了课程的学生人数。
 
 ```
 SELECT DISTINCT COUNT(s.sno) FROM s join sc on s.sno=sc.sno JOIN c on sc.cno= c.cno WHERE c.cname in ('茶艺','电影');
 SELECT COUNT(DISTINCT sc.sno) FROM sc JOIN c on sc.cno=c.cno WHERE c.cname in ('茶艺','电影');
 ```
18：计算选修了C1课程的学生平均成绩。
 
 ```
 SELECT AVG(sc.grade) FROM sc JOIN c on sc.cno=c.cno WHERE c.cname='C3'; 
 ```
19：查询学习C3课程的学生最高分数。
 
 ```
 SELECT max(sc.grade) FROM sc JOIN c on sc.cno=c.cno WHERE c.cname='C3'; 
 ```
20：查询各个课程号与相应的选课人数。
 
 ```
 SELECT cno,COUNT(*) FROM sc GROUP BY cno;
 ```
21：查询计算机系选修了3门以上课程的学生的学号。
 
 ```
 SELECT sc.sno FROM s JOIN sc on s.sno = sc.sno WHERE sdept = '计算机系' GROUP BY sc.sno HAVING COUNT(*) >3; 
 ```
22：求基本表S中男同学的每一年龄组（超过50人）有多少人？要求查询结果按人数升序排列，人数相同按年龄降序排列。
 
 ```
 
 ```
23：查询每个学生及其选修课程的情况。
 
 ```
SELECT sc.sno,c.* FROM sc JOIN c on sc.cno=c.cno WHERE c.cname in ('茶艺','电影');
 ```
24：查询选修了C2课程且成绩在90分以上的所有学生。
 
 ```
 SELECT s.sname FROM s join sc on s.sno=sc.sno JOIN c on sc.cno= c.cno WHERE c.cname = 'C2' and sc.grade >90;
 ```
25：查询每个学生选修的课程名及其成绩。
 
 ```
 SELECT s.sname,c.cname,sc.grade FROM s join sc on s.sno=sc.sno JOIN c on sc.cno= c.cno WHERE c.cname in ('茶艺','电影');
 ```
26：统计每一年龄选修课程的学生人数。
 
 ```
 
 ```
27：查询选修了C2课程的学生姓名。
 
 ```
 SELECT s.sname FROM s join sc on s.sno=sc.sno JOIN c on sc.cno= c.cno WHERE c.cname = 'C2';
 ```
28：查询与“张三”在同一个系学习的学生学号、姓名和系别。
 
 ```
 名字相同？
 SELECT sno,sname,sdept FROM s WHERE sdept = (SELECT sdept FROM s WHERE sname = '张三');
 ```
29：查询选修课程名为“数据库”的学生学号和姓名。
 
 ```
 SELECT s.sno,s.sname FROM s JOIN sc on s.sno = sc.sno JOIN c on sc.cno = c.cno WHERE c.cname = '数据库';
 ```
30：查询与“张三”在同一个系学习的学生学号、姓名和系别。
 
 
 ```
 同28 题
 ```
31：查询选修课程名为“数据库”的学生学号和姓名。
 
 ```
 同29 题
 ```
32：查询选修了C2课程的学生姓名。
 
 ```
 同27 题
 ```
33：查询所有未选修C2课程的学生姓名。
 
 ```
 SELECT s.sname FROM s join sc on s.sno=sc.sno JOIN c on sc.cno= c.cno WHERE c.cname not in ('c2');
 ```
34：查询与“张三”在同一个系学习的学生学号、姓名和系别。
 
 ```
 同28 题
 ```
35：查询选修了全部课程的学生姓名。
 
 ```
 
 ```
36：查询所学课程包含学生S3所学课程的学生学号
 
 ```
 
 ```
     
  
     
   