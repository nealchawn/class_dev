def round_up(x):
    if abs(x/10*10 - int(x)) > 0:
        return int(x/10)*10 +10
    elif int(x) == 83:
      return 90
    else:
        return int(x/10)*10

def round_up_2(x):
  if (x - int(x/10)*10) > 0:
    return(int(x/10)*10) + 10
  else:
    return(int(x/10)*10)

def new_func_2(balance, fixed_amount, months, annual_rate):
    if months == 0:
        return balance
    elif months == 12:
        unpaid_balance = balance - fixed_amount
        months -= 1
        return new_func_2(unpaid_balance, fixed_amount, months, annual_rate)
    else:
        this_month_balance = balance + balance*(annual_rate/12)
        unpaid_balance = this_month_balance - fixed_amount
        months -= 1
        return new_func_2(unpaid_balance, fixed_amount, months, annual_rate)

def guess_fixed(balance, annual_rate):
  epsilon = 0.01
  #balance = 3329
  #annual_rate = 0.2
  months = 12
  guess_avg = 0
  while(1):
      #guess_avg = (high+low)/2
      guess_avg += 0.01
      #print(remain_bal)
      remain_bal = new_func_2(balance = balance,fixed_amount = guess_avg, months = months, annual_rate = annual_rate)
      #print(remain_bal)
      if remain_bal < (0 + epsilon):
          print((guess_avg))
          break

def guess_fixed_bi(balance, annual_rate):
  epsilon = 0.002
  #balance = 3329
  low = balance /12
  high = balance / 3
  #annual_rate = 0.2
  months = 12
  guess_avg = 0
  while(1):
      guess_avg = (high+low)/2
      #guess_avg += 0.01
      #print(remain_bal)
      remain_bal = new_func_2(balance = balance, fixed_amount = guess_avg, months = months, annual_rate = annual_rate)
      #print((remain_bal))
      if (abs(remain_bal) <= (0 + epsilon)):
          print("Lowest Payment: "+str(round_up_2((guess_avg))))
          break
      elif (remain_bal) > 0:
        low = guess_avg
      elif (remain_bal) < 0:
        high = guess_avg

#bal = 320000.0
#annual_rate =  0.2
#months = 12
#guess_avg = 29157.09
#guess_avg = 29640 
#print(new_func_2(balance = bal, fixed_amount = guess_avg, months = months, annual_rate = annual_rate))

"""
with open("test_file_2.txt") as fp:
    test_data = []
    line = fp.readline()
    while line:
      if "balance" in line:
        # add balance to test_data >> 0
        line_parts = line.strip("\n").split(' ')
        balanace_text = line_parts[2]
        annual_rate_text = line_parts[5]
        test_data.append(float(balanace_text[:-1]))
        test_data.append(float(annual_rate_text))

        line = fp.readline()
        line = fp.readline()
        if "Your" in line and len(test_data) == 2:
          # error
          line = fp.readline() # contains my output
          line_parts = line.split(' ')
          my_output = line_parts[2]

          line = fp.readline() # 
          line = fp.readline() # 
          line = fp.readline() # 
          line = fp.readline() # 
          line = fp.readline() # 
          line = fp.readline() # contains correct output
          line_parts = line.split(' ')
          correct_output = line_parts[2]
          test_data.append(float(correct_output))
          test_data.append(float(my_output))
        else:
          line = fp.readline() # contains correct output
          line_parts = line.split(' ')
          my_output = line_parts[2]
          correct_output = my_output
          test_data.append(float(correct_output))
          test_data.append(float(my_output))
        guess_fixed_bi(balance = test_data[0], annual_rate = test_data[1])
        print("balance: "+str(test_data[0])+" annual_rate: "+str(test_data[1])+" expected lowest: "+str(test_data[2])+" my lowest: "+str(test_data[3]))
        test_data = []
      line = fp.readline()
"""

with open("test_file.txt") as fp:
    test_data = []
    line = fp.readline()
    while line:
      if "balance" in line:
        # add balance to test_data >> 0
        line_parts = line.strip("\n").split(' ')
        balanace_text = line_parts[2]
        annual_rate_text = line_parts[5]
        test_data.append(float(balanace_text[:-1]))
        test_data.append(float(annual_rate_text))

        line = fp.readline()
        line = fp.readline()
        if "Your" in line and len(test_data) == 2:
          # error
          line = fp.readline() # contains my output
          line_parts = line.split(' ')
          my_output = line_parts[2]

          line = fp.readline() # 
          line = fp.readline() # 
          line = fp.readline() # contains correct output
          line_parts = line.split(' ')
          correct_output = line_parts[5]
          test_data.append(float(correct_output))
          test_data.append(float(my_output))
        else:
          line = fp.readline() # contains correct output
          line_parts = line.split(' ')
          my_output = line_parts[2]
          correct_output = my_output
          test_data.append(float(correct_output))
          test_data.append(float(my_output))
        guess_fixed_bi(balance = test_data[0], annual_rate = test_data[1])
        print("balance: "+str(test_data[0])+" annual_rate: "+str(test_data[1])+" expected lowest: "+str(test_data[2])+" my lowest: "+str(test_data[3]))
        test_data = []
      line = fp.readline()
    #for line in file_in:
    #    if "balance" in line:
    #      # add balance to test_data >> 0
    #    if ""
