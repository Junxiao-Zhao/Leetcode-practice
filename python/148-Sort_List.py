# https://leetcode.com/problems/sort-list/


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


def sortList_0(head: ListNode):
    if head is None:
        return head
    cur = head
    store = []

    while cur is not None:
        store.append(cur)
        cur = cur.next

    store.sort(key=lambda x: x.val)

    head = store[0]
    for i in range(len(store)):
        store[i].next = store[i + 1] if i < len(store) - 1 else None

    return head


def sortList(head: ListNode):
    if head is None:
        return head

    def merge(left: ListNode, right: ListNode):
        if not left:
            return right
        if not right:
            return left
        temp_head = prev = None
        cur_l = left
        cur_r = right
        while cur_l and cur_r:
            if cur_l.val <= cur_r.val:
                small = cur_l
                large = cur_r
            else:
                small = cur_r
                large = cur_l

            if not temp_head:
                temp_head = small
            else:
                prev.next = small
            prev = small
            cur_l = small.next
            cur_r = large

        if not cur_l:
            prev.next = cur_r
        else:
            prev.next = cur_l

        return temp_head

    def merge_sort(head: ListNode, lens: int):
        if lens <= 1:
            return head

        left_len = lens // 2
        right_len = lens - left_len

        right_head = head
        for i in range(left_len - 1):
            right_head = right_head.next

        left_end = right_head
        right_head = right_head.next
        left_end.next = None

        right_end = right_head
        for i in range(right_len - 1):
            right_end = right_end.next
        right_end.next = None

        left_sort = merge_sort(head, left_len)
        right_sort = merge_sort(right_head, right_len)
        return merge(left_sort, right_sort)

    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next

    return merge_sort(head, count)


if __name__ == "__main__":
    head = [4, 2, 1, 3]
    for i in range(len(head)):
        head[i] = ListNode(head[i])

    for i in range(len(head)):
        head[i].next = head[i + 1] if i < len(head) - 1 else None

    new_head = sortList(head[0])
    while new_head:
        print(new_head)
        new_head = new_head.next
