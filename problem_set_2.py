

# this function can return the remaining balance in 12 months
# to minimize the fixed cose we just need to send this input into a newton raphson!
monthly_rate = 0.04
#annual_rate = 0.2
months = 12
balance = 42
def new_func(balance, months):
    if months == 0:
        return balance
    else:
        this_month_balance = balance + balance*(annual_rate/12)
        unpaid_balance = this_month_balance - this_month_balance*(monthly_rate)
        months -= 1
        return new_func(unpaid_balance, months)
        #prev_month_balance = balance - balance(monthly_rate)
        #this_month_balance = prev_month_balance + prev_month_balance(annual_rate/12)

#print("Remaining balance: "+str(round(new_func(balance, months),2)))

# this function can return the remaining balance in 12 months
# to minimize the fixed cose we just need to send this input into a newton raphson!
#monthly_rate = 0.04


#annual_rate = 0.25
months = 12
# balance = 4773
# balance = 3926
# balance = 3329
#fixed_amount = 110
balance = 882


def round_up(x):
    if abs(int(x/10)*10 - int(x)) >= 5:
        return int(x/10)*10 +10
    else:
        return int(x/10)*10

def new_func_2(balance, fixed_amount, months):
    if months == 0:
        return balance
    else:
        this_month_balance = balance + balance*(annual_rate/12)
        unpaid_balance = this_month_balance - fixed_amount
        months -= 1
        return new_func_2(unpaid_balance, fixed_amount, months)

high = balance
low = 0
epsilon = 10
balance = 3329
annual_rate = 0.2
guess_avg = 0

while(1):
    #guess_avg = (high+low)/2
    guess_avg += 2
    #print(remain_bal)
    remain_bal = new_func_2(balance, guess_avg, months)
    print(remain_bal)
    if remain_bal < (0 + epsilon):
        print((guess_avg))
        break

while(False):
    guess_avg = (high+low)/2
    remain_bal = new_func_2(balance, guess_avg, months)
    if abs(remain_bal) <= (0 + epsilon):
        print((guess_avg))
        break
    elif remain_bal > 0:
        low = guess_avg
    elif remain_bal < 0:
        high = guess_avg
