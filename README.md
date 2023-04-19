### [Two Pointers](https://turingplanet.org/2020/05/20/array-two-pointers%e5%a5%97%e8%b7%af%e3%80%90leetcode%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e6%95%99%e7%a8%8b2%e3%80%91/)
![two pointers](./notes%20pic/two%20pointers.png)
- Move at least one pointer each step to avoid dead loops

### [Binary Search](https://turingplanet.org/2020/06/20/%e4%ba%8c%e5%88%86%e6%9f%a5%e6%89%bebinary-search%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e3%80%90leetcode%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e6%95%99%e7%a8%8b3%e3%80%91/)
![binary search](./notes%20pic/binary%20search%20template.png)
- Reduce search region but keep potential results each time
- Use `l + (r - l) / 2` instead of `(l + r) / 2`
- For blur search, `l < r`, return `l`
    - First occurance, `l = mid + 1` and `r = mid`
    - Last occurance, `l = mid` and `r = mid - 1`; `l + (r - l + 1) / 2`
- For closet to (万用型), `l < r - 1`, `l = mid`, `r = mid`
    - If `arr[l] > target`, return `l`
    - If `arr[r] < target`, return `r`
    - Else return the closest one's index

### [LinkedList](https://turingplanet.org/2020/06/20/%e9%93%be%e8%a1%a8linked-list%e9%a2%98%e5%9e%8b%e5%a5%97%e8%b7%af%e3%80%90leetcode%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e6%95%99%e7%a8%8b4%e3%80%91/)
![LinkedList](./notes%20pic/LinkedList%20vs%20Array.png)
- Two pointers
    - move in the same direction
    - define speed and distance in between
- Bottom up recursion
    - Ask for subproblem result
    - Do something in current level recursion
    - Return result
    - Add start before head in avoid of edge case

### [Stack](https://turingplanet.org/2020/06/21/stack%e5%a0%86%e6%a0%88%e8%a7%a3%e9%a2%98%e5%a5%97%e8%b7%af%e3%80%90leetcode%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e6%95%99%e7%a8%8b5%e3%80%91/)
- Keep elements in the Stack monotonic in/decreasing

### [Heap](https://turingplanet.org/2020/07/04/leetcode6heap/)
![Heap](./notes%20pic/Heap.png)
![Heap vs Sort](./notes%20pic/Heap%20vs%20Sort.png)