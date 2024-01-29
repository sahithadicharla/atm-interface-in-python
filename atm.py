print("Welcome to SAHITH Bank")
pin = 2000
chances = 3
balance = 10000
while chances != 0: 
     user_pin = int(input("Please enter the four digit pin"))
     if user_pin != pin :
          chances -= 1
          print("Wrong pin entered")
          print(f"you have{chances} chances left")
     else:
          user_choice = input("B : balance, D : deposit, W : withdraw")
     if user_choice == "B":
          print(f"Your total balance is Rs.{balance}")

     if user_choice == "D":
          deposit_user = int(input("enter the amount to be deposited"))
          total_balance = deposit_user + balance
          print(f"you have deposited Rs.{deposit_user}")
          print(f"your total balance is Rs.{total_balance}")
     
     if user_choice == "W" :
          withdraw_user = int(input("enter the amount to be withdrawn"))
          total_balance = withdraw_user - balance
          print(f"you have withdrawn Rs.{withdraw_user}")
          print(f"your total balance is Rs.{total_balance}")

     user_exit = input("would you like to exit? Yes/No")
     if user_exit == "Yes" :
          print("Thank you for using SAHITH Bank")
          break
     else:
          continue