-- 코드를 입력하세요
SELECT USER_ID,	NICKNAME, sum(price)	TOTAL_SALES
from USED_GOODS_BOARD a join USED_GOODS_USER b on a.writer_id = b.USER_ID  
where status = 'DONE' 
group by USER_ID
having sum(price)>=700000
order by TOTAL_SALES