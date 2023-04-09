public class Invert_Binary_Tree_226_easy {

    static TreeNode temp;

    public static void postOrder(TreeNode node) {
        if (node == null) {
            return;
        }

        postOrder(node.left);
        postOrder(node.right);
        temp = node.left;
        node.left = node.right;
        node.right = temp;
    }

    public TreeNode invertTree(TreeNode root) {
        postOrder(root);
        return root;
    }
}
