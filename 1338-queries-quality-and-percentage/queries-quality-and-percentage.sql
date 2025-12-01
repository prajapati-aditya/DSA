# Write your MySQL query statement below
select query_name, ROUND(sum(q.rating/q.position)/count(*),2) as quality,
ROUND(sum(if(rating<3,1,0))/count(*)*100,2) as poor_query_percentage
from queries as q
group by q.query_name

