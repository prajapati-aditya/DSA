# Write your MySQL query statement below
select eu.unique_id , emp.name
from 
Employees as emp
left join 
EmployeeUNI as eu
on emp.id = eu.id