-- 흉부외과 또는 일반외과 의사 목록 출력하기
-- 문제 설명
-- 다음은 종합병원에 속한 의사 정보를 담은DOCTOR 테이블입니다. 
-- DOCTOR 테이블은 다음과 같으며 DR_NAME, DR_ID, LCNS_NO, HIRE_YMD, MCDP_CD, TLNO는 

-- 각각 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 전화번호를 나타냅니다.

-- 문제
-- DOCTOR 테이블에서 진료과가 흉부외과(CS)이거나 일반외과(GS)인 
-- 의사의 이름, 의사ID, 진료과, 고용일자를 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 고용일자를 기준으로 내림차순 정렬하고, 고용일자가 같다면 이름을 기준으로 오름차순 정렬해주세요.

-- SQL을 실행하면 다음과 같이 출력되어야 합니다.

-- DR_NAME	DR_ID	MCDP_CD	HIRE_YMD
-- 니모	DR20200012	CS	2020-03-01

-- 주의사항
-- 날짜 포맷은 예시와 동일하게 나와야합니다.

-- -- 코드를 입력하세요
SELECT DR_NAME,	DR_ID,	MCDP_CD, date_format(HIRE_YMD,'%Y-%m-%d') from doctor where mcdp_cd = "cs" or mcdp_cd = "gs" order by hire_ymd desc, DR_NAME