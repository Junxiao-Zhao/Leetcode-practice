public class Merge_Two_Sorted_Lists_21_easy {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if (list1 == null)
            return list2;
        else if (list2 == null)
            return list1;

        ListNode start = null, prev = null, a = list1, b = list2;

        while (a != null && b != null) {
            if (a.val <= b.val) {
                if (start == null) {
                    start = a;
                } else {
                    prev.next = a;
                }
                prev = a;
                a = a.next;
            } else {
                if (start == null) {
                    start = b;
                } else {
                    prev.next = b;
                }
                prev = b;
                b = b.next;
            }
        }

        if (a == null) {
            prev.next = b;
        } else {
            prev.next = a;
        }

        return start;
    }
}