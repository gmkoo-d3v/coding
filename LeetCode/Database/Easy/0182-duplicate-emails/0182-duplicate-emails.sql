/* Write your PL/SQL query statement below */
select p.email as Email
from Person p
group by email
having count(Email) > 1;