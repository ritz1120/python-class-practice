create database rithika;
use rithika;
create table pythoncourse(
name varchar(20),
age int)
insert into pythoncourse values("rithika",17,"python");
alter table pythoncourse add column course varchar(20);
select * from pythoncourse;
delete from pythoncourse where name="rithika";
set sql_safe_updates=0;
insert into pythoncourse values("sanjai",17,"python");
update pythoncourse set age=18 where name="rithika"
select name from pythoncourse;
select * from pythoncourse where name="rithika"
alter table pythoncourse drop column age;






