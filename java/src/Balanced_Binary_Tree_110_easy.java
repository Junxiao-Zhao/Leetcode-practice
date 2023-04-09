public class Balanced_Binary_Tree_110_easy {

    public static int postOrder(TreeNode node) {
        if (node == null)
            return 0;

        int l = postOrder(node.left);
        int r = postOrder(node.right);

        if (l == -1 || r == -1 || Math.abs(l - r) > 1)
            return -1;
        else
            return Math.max(l, r) + 1;

    }

    public static boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        else
            return postOrder(root) >= 0;

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        System.out.println(isBalanced(root));
    }
}
