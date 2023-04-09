import java.util.*;

public class Longest_Substring_Without_Repeating_Characters_3_medium {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> dict = new HashMap<>();

        int l = 0, r = 0, num, len = 0;
        char cur;

        while (r < s.length()) {
            cur = s.charAt(r);
            num = dict.getOrDefault(cur, 0);
            dict.put(cur, num + 1);

            if (dict.keySet().size() == r - l + 1) {
                len = Math.max(len, r - l + 1);
            } else {
                while (r - l + 1 > len) {
                    cur = s.charAt(l);
                    num = dict.get(cur) - 1;
                    if (num == 0) {
                        dict.remove(cur);
                    } else {
                        dict.replace(cur, num);
                    }
                    l++;
                }
            }

            r++;
        }

        return len;
    }
}
