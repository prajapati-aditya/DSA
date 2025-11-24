# Write your MySQL query statement below
select s.user_id,
        ROUND((sum(CASE when c.action ="confirmed" THEN 1 ELSE 0 END)/count(*)),2)
        as confirmation_rate
from signups as s
left join confirmations c
on s.user_id = c.user_id
group by s.user_id
order by confirmation_rate