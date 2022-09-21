candles = int(input("Enter Number of candles : "))
rate = int(input("Enter rate of Burned candles : "))

candles_Burned = candles//rate
if candles_Burned >= rate:
    candles_Burned+=candles_Burned//rate
total = candles_Burned+candles
print(total)
