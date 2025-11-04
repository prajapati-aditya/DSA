# Write your MySQL query statement below

select prd.product_name , sls.year , sls.price 
from Sales as sls
left join 
Product as prd
on sls.product_id = prd.product_id 
