### [Binary Search](https://turingplanet.org/2020/06/20/%e4%ba%8c%e5%88%86%e6%9f%a5%e6%89%bebinary-search%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e3%80%90leetcode%e5%88%b7%e9%a2%98%e5%a5%97%e8%b7%af%e6%95%99%e7%a8%8b3%e3%80%91/)
![template](./notes%20pic/binary%20search%20template.png)
- Reduce search region but keep potential results each time
- Use `l + (r - l) / 2` instead of `(l + r) / 2`
- For blur search, `l < r`, return `l`
    - First occurance, `l = mid + 1` and `r = mid`
    - Last occurance, `l = mid` and `r = mid - 1`; `l + (r - l + 1) / 2`
- For closet to (万用型), `l < r - 1`, `l = mid`, `r = mid`
    - If `arr[l] > target`, return `l`
    - If `arr[r] < target`, return `r`
    - Else return the closest one's index
