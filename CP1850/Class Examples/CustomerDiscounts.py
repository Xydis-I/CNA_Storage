# -*- coding: utf-8 -*-
print("The Invoice Program\n")
customerType = input("Enter Customer Type (R/W): ")
invoiceTotal = float(input("Invoice Total: \t$"))
discountPercent = 0
grandTotal = 0

if (customerType.lower() == "r"):
    if (invoiceTotal < 250):
        discountPercent = 0
    elif invoiceTotal >= 250:
        discountPercent = 0.2
        grandTotal = invoiceTotal - invoiceTotal * discountPercent

elif (customerType.lower() == "w"):
    discountPercent = 0.4
    grandTotal = invoiceTotal - invoiceTotal * discountPercent
    
else:
    print("Customer Type Must Be 'R' or 'W'.")
    
    
print("\nInvoice Total: \t\t\t$%.1f\nDiscount Percent: \t\t$%.1f\nDiscount Amount: \t\t$%.1f\nNew Invoice Total: \t\t$%.1f" %
      (invoiceTotal, discountPercent, invoiceTotal * discountPercent, grandTotal))