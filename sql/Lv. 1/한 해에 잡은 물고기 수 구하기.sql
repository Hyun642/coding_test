한 해에 잡은 물고기 수 구하기

문제 설명
낚시앱에서 사용하는 FISH_INFO 테이블은 잡은 물고기들의 정보를 담고 있습니다.
 FISH_INFO 테이블의 구조는 다음과 같으며 
 ID, FISH_TYPE, LENGTH, TIME은 각각 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 
 물고기를 잡은 날짜를 나타냅니다.


문제
FISH_INFO 테이블에서 2021년도에 잡은 물고기 수를 출력하는 SQL 문을 작성해주세요.

이 때 컬럼명은 'FISH_COUNT' 로 지정해주세요.

-- 코드를 작성해주세요
select count(*) as 'FISH_COUNT' from FISH_INFO where year(time) = '2021'
