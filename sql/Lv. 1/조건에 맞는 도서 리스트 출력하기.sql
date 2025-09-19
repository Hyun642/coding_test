-- 조건에 맞는 도서 리스트 출력하기
-- 문제 설명
-- 다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(BOOK) 테이블입니다.

-- BOOK 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.

-- 문제
-- BOOK 테이블에서 2021년에 출판된 '인문' 카테고리에 속하는 도서 리스트를 찾아서 도서 ID(BOOK_ID), 출판일 (PUBLISHED_DATE)을 출력하는 SQL문을 작성해주세요.
-- 결과는 출판일을 기준으로 오름차순 정렬해주세요.

-- ex) BOOK_ID	PUBLISHED_DATE
-- 4	2021-03-15
-- 3	2021-04-11

-- 코드를 입력하세요
SELECT book_id, date_format(published_date,'%Y-%m-%d') from book where year(published_date) = '2021'  and CATEGORY = '인문' order by published_date
