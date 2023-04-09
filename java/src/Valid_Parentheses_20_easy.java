import java.util.Stack;

public class Valid_Parentheses_20_easy {
    public static boolean isValid(String s) {
        Stack<Character> q = new Stack<>();
        Character cur, prev;

        for (int i = 0; i < s.length(); i++) {
            cur = s.charAt(i);
            if (cur == '(' || cur == '[' || cur == '{') {
                q.add(cur);
            } else {
                if (q.size() == 0)
                    return false;
                prev = q.pop();
                switch (prev) {
                    case '(':
                        if (cur != ')')
                            return false;
                        break;
                    case '[':
                        if (cur != ']')
                            return false;
                        break;
                    case '{':
                        if (cur != '}')
                            return false;
                        break;
                }
            }
        }

        return q.size() == 0;
    }

    public static void main(String[] args) {
        String s = "()[]{}";
        System.out.println(isValid(s));
    }

}
