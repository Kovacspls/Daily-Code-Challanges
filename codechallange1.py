"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether 
any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Upgrade to premium and get in-depth solutions to every problem. 
Since you were referred by one of our affiliates, 
you'll get a 10% discount on checkout!

If you liked this problem, 
feel free to forward it along so they can subscribe here! 
As always, shoot us an email if there's anything we can help with!"""


k = 17
my_list = [10, 15, 3, 7] 


def add_up(value, list):

    for i in list:
        for j in list:
            if i+j == value or i == value:
                return True
                break


print(add_up(k, my_list))
