/* Write your PL/SQL query statement below */
select emp.name as Employee
from employee emp, employee MGR
where emp.managerId = MGR.id and emp.salary > MGR.salary
