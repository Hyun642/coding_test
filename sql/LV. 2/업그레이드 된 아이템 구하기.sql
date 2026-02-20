-- 코드를 작성해주세요
select it.ITEM_ID,	ITEM_NAME,	RARITY
from ITEM_TREE as it join ITEM_INFO inf on it.ITEM_ID = inf.ITEM_ID
where it.PARENT_ITEM_ID in (select item_id
        from ITEM_INFO 
        where RARITY = "RARE")
order by inf.item_id desc