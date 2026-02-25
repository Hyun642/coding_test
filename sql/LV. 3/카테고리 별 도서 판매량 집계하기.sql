-- 코드를 입력하세요
SELECT CATEGORY,sum(SALES) as	TOTAL_SALES
from BOOK_SALES join BOOK using (BOOK_ID)
where month(SALES_DATE) = 1
group by CATEGORY
order by CATEGORY