class Solution:
    def braceExpansionII(self, expression):
        def union(set1, set2):
            return set1 | set2

        def product(set1, set2):
            return {a + b for a in set1 for b in set2}

        def parse():
            nonlocal index

            result = set()
            current = {""}

            while index < len(expression) and expression[index] != '}':
                ch = expression[index]

                if ch == '{':
                    index += 1
                    part = parse()
                    index += 1  # Skip '}'
                elif ch == ',':
                    result = union(result, current)
                    current = {""}
                    index += 1
                    continue
                else:
                    part = {ch}
                    index += 1

                current = product(current, part)

            result = union(result, current)
            return result

        index = 0
        result = parse()

        return sorted(result)