select round( (sum( if(min_ord=min_del,1,0)
            )/count(*)*100),2

)
    as immediate_percentage

from 
( 
    select delivery_id,
        customer_id, 
        min(order_date) as min_ord,
        min(customer_pref_delivery_date) as min_del
    from delivery 
    group by customer_id
) as new_table
