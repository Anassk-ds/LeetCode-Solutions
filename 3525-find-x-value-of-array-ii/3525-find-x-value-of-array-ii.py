class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [[1, [0] * k] for _ in range(4 * n)]

        def create_node(value):
            remainder = value % k
            count = [0] * k
            count[remainder] = 1
            return [remainder, count]

        def merge(left, right):
            left_product, left_count = left
            right_product, right_count = right

            product = (left_product * right_product) % k
            count = left_count[:]

            for r in range(k):
                new_remainder = (left_product * r) % k
                count[new_remainder] += right_count[r]

            return [product, count]

        def build(node, left, right):
            if left == right:
                tree[node] = create_node(nums[left])
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, left, right, index, value):
            if left == right:
                tree[node] = create_node(value)
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, right, index, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return tree[node]

            mid = (left + right) // 2

            if qr <= mid:
                return query(node * 2, left, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql, qr)

            left_result = query(node * 2, left, mid, ql, qr)
            right_result = query(node * 2 + 1, mid + 1, right, ql, qr)

            return merge(left_result, right_result)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            _, count = query(1, 0, n - 1, start, n - 1)

            result.append(count[x])

        return result