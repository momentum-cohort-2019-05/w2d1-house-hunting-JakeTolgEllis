annual_salary= int(input( "What is your annual salary?"))
portion_saved= float(input("How much do you save each month?"))
total_cost= int(input ("What is the cost of your dream home?"))
r= 0.04
current_savings= 0.00
portion_down_payment= 0.25
num_months= 0

while current_savings < portion_down_payment:
    current_savings = (current_savings +(current_savings * (r/12))) + ((annual_salary/12)*portion_saved)
    num_months= num_months+1
    if current_savings >= portion_down_payment:
        print("it will take you" + str(num_months) + )"months to save up for your house")





