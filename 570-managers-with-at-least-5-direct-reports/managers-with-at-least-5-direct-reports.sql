# Write your MySQL query statement below
select a1.name 
from employee as a1
join employee a2
on a1.id = a2.managerId
group by a2.managerId
having count(*) >= 5 