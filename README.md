# Group-Order-Calculator
Console app that takes in a few order details to calculate individual order totals for group orders. 

Subtotal:
The subtotal of the individual's order before any tip, taxes, or fees are applied.

Tip amount:
Split evenly among individuals.

Taxes:
Calculated off of the tax rate of the order and applied to individual subtotals.

Fees:
Split evenly among individuals. Derived by taking the sum of each individuals subtotal, tax, and tip amount and subtracting it from the overall order total. Anything left over after subtotal, taxes, and tip is considered "Fees".

Total:
subtotal + tip + tax + fees = total