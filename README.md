# Group-Order-Calculator
Console app that takes in a few order details to calculate individual order totals for group orders. 

Subtotal:
The subtotal of an individual's order before any tip, taxes, or fees are applied.

Tip amount:
Split evenly among individuals.

Taxes:
Calculated by finding the tax rate of the order based on the order total and the amount of taxes being charged. Tax rate is applied to individual subtotals to get each persons tax amount.

Fees:
Split evenly among individuals. Derived by taking the sum of each individuals subtotal, tax, and tip amount and subtracting it from the overall order total. Anything left over after subtotal, taxes, and tip is considered "Fees".

Total:
subtotal + tip + tax + fees = total
