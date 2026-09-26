class Solution:
    def evaluate(self, s, knowledge):
        values = {key: value for key, value in knowledge}

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                start = i

                while s[i] != ')':
                    i += 1

                key = s[start:i]
                result.append(values.get(key, '?'))
                i += 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)