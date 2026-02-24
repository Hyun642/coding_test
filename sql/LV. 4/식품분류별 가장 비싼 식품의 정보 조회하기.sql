-- 코드를 입력하세요
select CATEGORY,	MAX_PRICE,	PRODUCT_NAME
from (SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME, rank() over        (partition by CATEGORY order by price desc )  as rnk
    from FOOD_PRODUCT 
    where CATEGORY in ('과자', '국', '김치', '식용유')) as a
    WHERE rnk = 1
order by MAX_PRICE desc