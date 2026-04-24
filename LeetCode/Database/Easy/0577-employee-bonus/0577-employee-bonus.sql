/* Write your PL/SQL query statement below */
select e.name, b.bonus
from Employee e
left join bonus b
on e.empID = b.empID
where b.bonus IS NULL or b.bonus < 1000;
