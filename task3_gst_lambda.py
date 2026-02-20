# Task 3 - Lambda Function: GST Calculator

gst = lambda price: price + (0.18 * price)

print(gst(100))  # Expected: 118

# Optional: GST + Discount together
gst_discount = lambda price, discount: (price - (price * discount / 100)) * 1.18

print(gst_discount(1000, 10))