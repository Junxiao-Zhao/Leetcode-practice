public class Valid_Palindrome_125_easy {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        char l, r;

        while (i < j) {
            if (Character.isLetterOrDigit(s.charAt(i)) && Character.isLetterOrDigit(s.charAt(j))) {
                l = Character.toLowerCase(s.charAt(i));
                r = Character.toLowerCase(s.charAt(j));

                if (l != r)
                    return false;
                i++;
                j--;
            } else {
                if (!Character.isLetterOrDigit(s.charAt(i))) {
                    i++;
                }
                if (!Character.isLetterOrDigit(s.charAt(j))) {
                    j--;
                }
            }

        }

        return true;
    }
}
