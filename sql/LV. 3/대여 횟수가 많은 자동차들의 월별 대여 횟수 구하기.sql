-- 코드를 입력하세요
select  month(start_date) MONTH, CAR_ID, count(START_DATE) RECORDS
from
CAR_RENTAL_COMPANY_RENTAL_HISTORY as CAR_RENTAL join
   ( SELECT CAR_ID 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
    group by CAR_ID
    having count(*) >= 5
   ) as g using(car_id)
where  date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
group by car_id, month(start_date)
order by MONTH, CAR_ID desc