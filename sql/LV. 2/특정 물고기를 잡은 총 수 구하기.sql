-- 코드를 작성해주세요
select count(*) FISH_COUNT
from FISH_INFO natural join FISH_NAME_INFO 
where FISH_NAME ='BASS' or FISH_NAME ='SNAPPER'