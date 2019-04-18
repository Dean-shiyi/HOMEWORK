
a.建立一个公司数据库(gongsi)  

```
CREATE DATABASE `gongsi` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```
 b.建立一张部门表

b_id 部门编号 主键 自增长

b_name 部门名称  非空   
 
 ```
 CREATE TABLE department(
 b_id int(10) PRIMARY key auto_increment,
 b_name VARCHAR(20) not null);
 ```
 c.建立一张员工表

y_id 员工编号  主键，自增长

y_name 姓名

 y_sex 性别
 
 y_age 年龄
 
 y_address 住址  默认值：不详
 
 b_id 部门编号   外键列
 
 ```
 CREATE TABLE worker(
 y_id int(10) PRIMARY key auto_increment,
 y_name VARCHAR(20),
 y_sex VARCHAR(4),
 y_age int(10),
 y_address VARCHAR(20) DEFAULT '不详',
 b_id int(10),
 CONSTRAINT `dep_id` FOREIGN key(`b_id`) REFERENCES department(`b_id`)
 );
 ```
 
1、查询年龄在25至30岁之间的男员工的姓名和住址。 
 
 ```
 SELECT y_name,y_Address from worker WHERE y_sex='男' and y_age > 25 and y_age < 30;
 ```

2、查询财务部所有40岁以下男员工的所有信息 
 
 ```
 SELECT a.* FROM worker as a JOIN department as b on a.b_id = b.b_id WHERE y_sex = '男' and y_age < 40 AND b_name = '财务部'; 
 ```
3、查询人事部年龄最大的女员工姓名 
 
 ```
 SELECT a.y_name as name FROM Worker as a join department as b on a.b_id = b.b_id WHERE y_sex = '女' ORDER BY y_age desc LIMIT 0,1 ;
 ```
4、2号新到一名员工，已知姓名，性别，年龄，将此员工加入到员工表  
 
 ```
 当信息不全时需写具体插入信息
 INSERT into worker (y_name,y_sex,y_age) VALUES ('bob','男',25);
 ```

5、在员工表中，将人事部年龄大于30岁的女同事，调到后勤部
 
 ```
 UPDATE worker set b_id = 2 WHERE b_id =1 and y_sex = '女' and y_age >30;
 ```
6：查询每个部门年龄最大的员工，显示部门名字和年龄。
 
 ```
 SELECT b.b_name,MAX(a.y_age) FROM worker as a join department as b on a.b_id = b.b_id GROUP BY b.b_name;
 ```
7：查询每个部门各有多少人，显示部门名字和人数，按人数倒序，如果人数相同，按部门编号正序。
 
 ```
 注意，，，，，，，
 SELECT b.b_name,COUNT(*) as num FROM worker as a join department as b on a.b_id = b.b_id GROUP BY b.b_name,b.b_id ORDER BY num desc,b.b_id;
 ```
8：将张三的的名字改为李四，并调到财务部。
 
 ```
 UPDATE worker set y_name = '李四' and b_id = 3 WHERE y_name = '张三';
 ```
9：将后勤部年龄大于60岁的员工删除。
 
 ```
 DELETE FROM worker WHERE y_age > 60 and b_id = 2;
 ```
10：查询财务部年龄不在20-30之间的男生信息。
 
 ```
 SELECT * FROM worker WHERE b_id = 4 and (y_age <20 or y_age >30) and y_sex = '男';
 ```