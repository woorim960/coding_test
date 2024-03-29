# 없어진 기록 찾기
SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS AS O
LEFT JOIN ANIMAL_INS AS I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL;

# 있었는데요 없었습니다
SELECT o.ANIMAL_ID, o.NAME FROM ANIMAL_OUTS AS o
LEFT JOIN ANIMAL_INS AS i
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE o.DATETIME < i.DATETIME
ORDER BY i.DATETIME;

# 오랜 기간 보호한 동물(1)
SELECT i.NAME, i.DATETIME FROM ANIMAL_INS AS i
LEFT JOIN ANIMAL_OUTS AS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE o.ANIMAL_ID IS NULL
ORDER BY DATETIME ASC
LIMIT 3;

# 보호소에서 중성화한 동물
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME FROM ANIMAL_INS AS i
LEFT JOIN ANIMAL_OUTS AS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE LIKE "I%" AND o.SEX_UPON_OUTCOME NOT LIKE "I%";
# WHERE i.SEX_UPON_INTAKE != o.SEX_UPON_OUTCOME;
# WHERE i.SEX_UPON_INTAKE regexp "^Intact" AND o.SEX_UPON_OUTCOME not regexp "^Intact"
