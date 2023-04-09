import java.util.*;

public class assign_cookies_455_easy {
    public static int assginCookies(int[] children, int[] cookies) {
        Arrays.sort(children);
        Arrays.sort(cookies);
        int i = 0;
        int j = 0;
        while (i < children.length && j < cookies.length) {
            if (children[i] <= cookies[j])
                i++;
            j++;
        }
        return i;
    }

    public static void main(String[] args) throws Exception {
        int[] child = {1,5};
        int[] cookies = {1, 2, 3};
        int num = assginCookies(child, cookies);
        System.out.println(num);
    }
}
