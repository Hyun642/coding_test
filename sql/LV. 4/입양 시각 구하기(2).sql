with recursive time as (select 0 as hour
                  union all
                  select hour + 1 from time where hour < 23)
-- 코드를 입력하세요
SELECT t.hour, count(a.ANIMAL_ID)	COUNT
from time t left join ANIMAL_OUTS a on t.hour = hour(a.datetime)  
group by  t.hour
order by t.hour