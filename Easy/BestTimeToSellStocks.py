# 16/06/23

def maxProfit2(prices) -> int:
    if len(prices) == 1:
        return 0
    buy, sell = 0, 1
    max_prof = 0
    while sell < len(prices):
        temp_proof = prices[sell] - prices[buy]
        if temp_proof > 0:
            max_prof = max(temp_proof, max_prof)
        else:
            buy = sell

        sell += 1
    return max_prof
