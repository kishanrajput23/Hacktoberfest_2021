class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_set = {'(','{','['}
        right_set = {')','}',']'}
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for each in s:
            if each in left_set:
                stack.append(each)
            elif each in right_set:
                try:
                    pop_out = stack.pop()
                except:
                    return 0
                if mapping[each] ==  pop_out:
                    continue
                else:
                    return 0
        if len(stack) > 0:
            return 0
        return 1
