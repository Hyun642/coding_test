-- 코드를 입력하세요
SELECT year(SALES_DATE) year,month(SALES_DATE) month,GENDER ,count(distinct USER_ID) USERS
from USER_INFO join ONLINE_SALE using (USER_ID)
where GENDER is not null
group by year(SALES_DATE),month(SALES_DATE),GENDER

order by YEAR,	MONTH,	GENDER