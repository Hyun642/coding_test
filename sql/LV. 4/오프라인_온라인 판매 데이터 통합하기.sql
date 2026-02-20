-- 코드를 입력하세요
(SELECT SALES_DATE,	PRODUCT_ID,	USER_ID,	SALES_AMOUNT
from ONLINE_SALE 
where SALES_DATE like "2022-03%"

union all
SELECT date_format(SALES_DATE,"%Y-%m-%d"),	PRODUCT_ID,	null as USER_ID,	SALES_AMOUNT
from OFFLINE_SALE 
where SALES_DATE like "2022-03%" )

order by SALES_DATE , product_id, user_id