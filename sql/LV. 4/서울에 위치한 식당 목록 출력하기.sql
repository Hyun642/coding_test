-- 코드를 입력하세요
SELECT  REST_ID , REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS, round(avg(REVIEW_SCORE),2) as SCORE    from REST_INFO natural join REST_REVIEW  
where address like '서울%'     group by REST_ID 
order by SCORE desc, favorites desc