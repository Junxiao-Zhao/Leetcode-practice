public class best_time_to_buy_and_sell_stock_II_122_medium {
    public static int buy_sell(int[] prices) {
        int profit = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < prices[i - 1]) {
                profit += prices[i - 1];
                profit -= prices[i];
            }

        }

        profit += prices[prices.length - 1];

        return profit;
    }

    public static void main(String[] args) {
        int[] prices = { 7, 6, 4, 3, 1 };
        System.out.println(buy_sell(prices));
    }
}
