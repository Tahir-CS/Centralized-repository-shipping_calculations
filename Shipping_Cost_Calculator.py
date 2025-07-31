# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
price = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * price

## Display the result 
print(f"Shipping Cost: {shipping_cost} USD")

