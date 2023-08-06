from forex_python.bitcoin import BtcConverter
import datetime
from math import floor

# Initialize API settings
BTC_converter = BtcConverter()

# Input
print("โปรแกรมเทียบราคาบิทคอยน์ปัจจุบันกับค่าเฉลี่ยต่อปีตั้งแต่ 2011-2021)")
print("----------------------------------")
year = int(input(" - ระบุปีที่ต้องการ: "))
price_now = int(input(" - ราคาปัจจุบัน: "))
print("----------------------------------")
print("กำลังประมวลผล รอสักครู่...")

# Get historical data for the entire year
price_data = [BTC_converter.get_previous_price('USD'
             ,datetime.datetime(year, 1, 1)
             + datetime.timedelta(days=i)) for i in range(365)]

# Calculate average price
avg_price = sum(price_data) / len(price_data)

# Compare with current price
if price_now > avg_price:
    print("ราคาปัจจุบัน สูงกว่า ราคาเฉลี่ยในปี",year)
    print("ราคาเฉลี่ยปีนี้:", floor(avg_price))
elif price_now < avg_price:
    print("ราคาปัจจุบัน ต่ำกว่า ราคาเฉลี่ยในปี",year)
    print("ราคาเฉลี่ยปีนี้:", floor(avg_price))
else:
    print("ราคาปัจจุบันอยู่ในช่วงราคาเฉลี่ยของปี",year)
    print("ราคาเฉลี่ยปีนี้:", floor(avg_price))
