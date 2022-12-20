# Write a function that receives a single string parameter and determines whether the parentheses in the string are balanced. Balanced parentheses mean that that for every left parenthesis “(“there is a matching right parenthesis “)” and they are properly nested.
# The string may consist of only parentheses or a mathematical expression. The function should return True if the parentheses are balanced and False otherwise.
# For Example:
# ()				True
# ()()				True
# (1+2)				True
# (())				True
# (one)				True
# )(				False
# ())				False

def isBalanced(s):
  b = []
  for c in s:
    if c in ["("]:
      b.append(c)
    elif c == ')':
      if not b:
        return False
      cc = b.pop()
  #     if cc == '(':
  #       if c != ")":
  #         return False
  # if b:
  #   return False
  return True
print(isBalanced("()"))
print(isBalanced("()()"))
print(isBalanced("(1+2)"))
print(isBalanced("(())"))
print(isBalanced("(one)"))
print(isBalanced(")("))
print(isBalanced("())"))