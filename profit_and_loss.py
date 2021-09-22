#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("A program to analyse profit and loss")
name = input("Enter the name of the enterprise: ")
selling_price = float(input("Enter the selling price: "))
cost_price = float(input("Enter the cost price: "))

if (selling_price > cost_price):
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    txt = "You had a profit of {:.2f} at a profit percent of {:.2f}"
    print(txt.format(profit, profit_percent))
else:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    text = "You had a loss of {:.2f} at a loss percent of {:.2f}"
    print(text.format(loss, loss_percent))


# In[ ]:




