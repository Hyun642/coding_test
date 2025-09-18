-- 인기있는 아이스크림
-- 문제 설명
-- FIRST_HALF 테이블은 아이스크림 가게의 상반기 주문 정보를 담은 테이블입니다.FIRST_HALF 테이블 구조는 다음과 같으며, SHIPMENT_ID, FLAVOR, TOTAL_ORDER는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다.


-- 코드를 입력하세요
SELECT flavor from first_half order by total_order desc, shipment_id



