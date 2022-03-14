# 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
WHERE NAME REGEXP "^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)";
# REGEXP "Lucy|Ella"
# 이런식으로 짜도되는데, 예외 케이스 중에 Andry Lucy 이런 이름이 있나봄.
# 그래서 Lucy로 시작되고(^), Lucy로 끝나도록($) 해줘야 문제 통과함.
# 딱 Lucy만 걸리도록 해주는거임.

# SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
# FROM ANIMAL_INS
# WHERE NAME regexp "^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$"
# ORDER BY ANIMAL_ID;


# 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
# WHERE ANIMAL_TYPE = "Dog" AND NAME LIKE "%el%" 
WHERE ANIMAL_TYPE = "Dog" AND NAME REGEXP "el"
ORDER BY NAME ASC;
