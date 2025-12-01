# Write your MySQL query statement below
select date_format(trans_date,"%Y-%m") as month, 
        country, 
        count(*) as trans_count, 
        SUM(if(state='approved', 1, 0)) as approved_count,
        SUM(amount) as trans_total_amount,
        SUM(if(state='approved',amount,0)) as approved_total_amount    
from transactions 
group by date_format(trans_date,"%Y-%m"), country