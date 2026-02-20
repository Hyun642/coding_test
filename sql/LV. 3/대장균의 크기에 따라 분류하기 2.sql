-- 코드를 작성해주세요
select e.id as ID, 
case
    when ti.rank = 1 then 'CRITICAL'
    when ti.rank = 2 then 'HIGH'
    when ti.rank = 3 then 'MEDIUM'
    else 'LOW'
    end as "COLONY_NAME"
from (select id, ntile(4) over (order by SIZE_OF_COLONY desc) 'rank'
    from ECOLI_DATA) ti join ECOLI_DATA e on ti.id = e.id
order by e.id