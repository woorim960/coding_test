from itertools import combinations as comb
def solution(orders, course):
  course_ls = []
  for i in course :
    for order in orders :
      a = list(map(''.join, comb(order, i)))
      course_ls.append(a)

  result = []
  course_ls = sum(course_ls, [])
  for sc in set(course_ls) :
    if course_ls.count(sc) >= 2 :
      result.append(sc)

  # result = []
  # for c in course_2 :
  #   if course.count(c) >= 2:
  #     result.append(cs)

  return result
  
  

def is_contain(cs, od) :
  cnt = 0
  for c in list(cs) :
    if c in od :
      cnt += 1
  if len(cs) == cnt :
    return True
  return False


print( solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]) )
print( solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) )
print( solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) )
