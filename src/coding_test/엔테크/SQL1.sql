-- 코드를 입력하세요
SELECT c.NAME, count(p.id) as CNT
from CHARACTERS c
LEFT JOIN PURCHASES p ON
c.NAME = p.ITEM GROUP BY c.NAME;