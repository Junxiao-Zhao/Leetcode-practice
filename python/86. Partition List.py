class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


def partition(head: ListNode, x: int):
    top = ListNode(next=head)
    i, j = top, top

    while j and j.next:
        change = False
        cur = j.next
        if cur.val < x:
            if i != j:
                move = i.next
                i.next = cur
                j.next = cur.next
                cur.next = move
                change = True
            i = i.next

        j = j if change else j.next

        k = top.next
        while k:
            print(k, end="->")
            k = k.next
        print()

    return top.next


if __name__ == "__main__":
    nxt = None
    head = None
    for i in [1, 4, 3, 0, 2, 5, 2][::-1]:
        head = ListNode(i, nxt)
        nxt = head

    partition(head, 3)
