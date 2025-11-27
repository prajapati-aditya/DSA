# Write your MySQL query statement below
select p.project_id, ROUND(SUM(e.experience_years)/Count(*),2) as average_years 
 from
project as p
left join employee as e
on p.employee_id = e.employee_id
group by project_id