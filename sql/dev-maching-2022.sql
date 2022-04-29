# 22.04.02 토요일
SELECT p.CART_ID, IF(p.PRICE < cp.MINIMUM_REQUIREMENT, 1, 0) AS ABUSED
FROM (
  SELECT p.CART_ID, SUM(p.PRICE) AS PRICE
  FROM CART_PRODUCTS AS p
  GROUP BY p.CART_ID) AS p
JOIN COUPONS AS cp
ON cp.CART_ID = p.CART_ID
ORDER BY p.CART_ID;