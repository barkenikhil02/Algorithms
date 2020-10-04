# prefered sol look at function call to know how to run
def balanceCheck(s):
    if len(s) % 2 != 0:
        return False
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if (len(stack) == 0):
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0


if (__name__) == "__main__":
    print(balanceCheck('()'))

# my sol but not prefered its wrong way to do this DS problem but it works
# para = "[](){{[][][]}}"

# co = 0
# cc = 0
# so = 0
# sc = 0
# cuo = 0
# cuc = 0


# for i in range(len(para)):
#     if len(para) == 0:
#         print(True)
#         break
#     elif len(para) % 2 != 0:
#         print(False)
#         break
#     if para[i] == "(":
#         co += 1
#     elif para[i] == ")":
#         cc += 1

#     if para[i] == "[":
#         so += 1
#     elif para[i] == "]":
#         sc += 1

#     if para[i] == "{":
#         cuo += 1
#     elif para[i] == "}":
#         cuc += 1

# if (co == cc and so == sc and cuo == cuc):
#     print("True")
# else:
#     print("False")
