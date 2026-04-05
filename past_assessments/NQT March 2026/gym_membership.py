months = int(input("Enter the number of months for the gym membership: "))
plans = [(1, 2000), (3, 5000), (6, 8000), (12, 12000)]

dp = [float('inf')] * (months + 1)
dp[0] = 0

for i in range(1, months + 1):
    for month, price in plans:
        if i >= month:
            dp[i] = min(dp[i], dp[i - month] + price)

print(f"The minimum cost for a {months}-month gym membership is: {dp[months]}")