select a.history_id,# a.total_price, a.rental_period, dp.discount_rate,
if(a.plan_id=0, a.total_price, round((total_price*(1-(0.01*dp.discount_rate))))) as FEE
from(
    select rh.history_id, c.car_type, 
    datediff(rh.end_date, rh.start_date) + 1 as rental_period,
    c.daily_fee,
    (datediff(rh.end_date, rh.start_date) + 1) * c.daily_fee as total_price,
    case
    when datediff(rh.end_date, rh.start_date) + 1 >= 90 then 12
    when datediff(rh.end_date, rh.start_date) + 1 >= 30 then 11
    when datediff(rh.end_date, rh.start_date) + 1 >= 7 then 10
    else 0
    end as plan_id
    from car_rental_company_rental_history as rh
    inner join car_rental_company_car as c
    on rh.car_id=c.car_id
    where c.car_type='트럭'
) as a
left join car_rental_company_discount_plan as dp
on a.plan_id=dp.plan_id
order by FEE desc, history_id desc;
