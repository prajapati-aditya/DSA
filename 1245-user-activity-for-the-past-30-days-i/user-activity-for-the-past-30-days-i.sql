# Write your MySQL query statement below
select activity_date as day, count(distinct user_id)
as active_users 
from activity 
where activity_date in (
    select activity_date from activity 
    where activity_date BETWEEN '2019-06-28' and '2019-07-28'
)
group by activity_date