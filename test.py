s1 = "()"
# output = True
s2 = "()[]{}"
# output = True
s3 = "{]"
# output = False
s4 = "([)]"
# output = False

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4)) 