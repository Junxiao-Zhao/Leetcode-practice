import java.util.HashMap;

public class Valid_Anagram_242_easy {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        HashMap<Character, Integer> dict = new HashMap<>();
        int len = s.length();
        int num;
        char c;

        for (int i = 0; i < len; i++) {
            c = s.charAt(i);
            num = dict.getOrDefault(c, 0);
            dict.put(c, num + 1);
        }

        for (int i = 0; i < len; i++) {
            c = t.charAt(i);
            if (dict.containsKey(c)) {
                num = dict.get(c) - 1;
                if (num == 0) {
                    dict.remove(c);
                } else {
                    dict.replace(c, num);
                }
            } else
                return false;
        }

        return dict.size() == 0;
    }
}
