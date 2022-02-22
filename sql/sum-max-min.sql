# 최댓값 구하기
SELECT DATETIME AS 시간 FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;

# 최댓값 구하기
SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS;

# 최솟값 구하기
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS;

# 동물 수 구하기
SELECT SUM(ANIMAL_ID) AS count FROM ANIMAL_INS;
