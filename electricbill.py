print("****************************************************************************************************************")
print("                                         UTTAR PRADESH POWER CORPORATE LIMITED                                  ")
print("                                            Bill of Supply for Electricity                                      ")
print("Circle : Upwest                                   Circle Code :105                      TollFreeNo. :18001800440")                                       

print("----------------------------------------------------------------------------------------")

customerName = str(input("Customer Name             : "))
customerNo = int(input("Customer Number           : "))
old_reading =int(input("Old Meter Reading         : ")) 
Current_reading =int(input("Current Meter Reading     : "))
Total_unit = Current_reading - old_reading
print("Total Units Consumed      : ",Total_unit)

print("----------------------------------------------------------------------------------------")

Fixed_Charge = int(input("Fixed Rental Line Maintenance Charges : "))
unit_Charge = Total_unit*3.25
Extra_unit = Total_unit-100
if Total_unit <= 100:
                   total_charge = unit_Charge     
                   print("Total Unit Charge                     : ",total_charge)
else:
     beyond_100 = Extra_unit*4.75
     total_charge = beyond_100 + 325 
     print("Total Unit Charge                     : ",total_charge)

total_tax = total_charge * 0.115

print("Total Tax (11.5%)                     : ",total_tax)


print("----------------------------------------------------------------------------------------")


Total_Bill = Fixed_Charge + total_charge + total_tax
print("Total Bill Amount Payable             : ",Total_Bill)
     
print("****************************************************************************************************************")


     
     
                   
                   
                   
                   
