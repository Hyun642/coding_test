-- 코드를 입력하세요
SELECT AUTHOR_ID, AUTHOR_NAME,CATEGORY,sum(price* sales) TOTAL_SALES 
from book join AUTHOR using (AUTHOR_ID) join BOOK_SALES using (BOOK_ID)
where sales_date like '2022-01%'
group by AUTHOR_NAME,CATEGORY
order by AUTHOR_ID,CATEGORY desc