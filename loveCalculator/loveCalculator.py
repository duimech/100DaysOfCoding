# This calculates a love match based on the amount of times that letters appear in two names
# Author: Ray Bolin
# Date: 1/2/2022
# 100DaysOfCoding

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Count the number of occurrances of each letter of the name in the word true
#Name 1
name1_lower = name1.lower()

countt_t_n1 = name1_lower.count("t")
countt_r_n1 = name1_lower.count("r")
countt_u_n1 = name1_lower.count("u")
countt_e_n1 = name1_lower.count("e")

countt_total_n1 = countt_t_n1 + countt_r_n1 + countt_u_n1 + countt_e_n1

# Count the number of occurrances of each letter of the name in the word love
countl_l_n1 = name1_lower.count("l")
countl_o_n1 = name1_lower.count("o")
countl_v_n1 = name1_lower.count("v")
countl_e_n1 = name1_lower.count("e")

countl_total_n1 = countl_l_n1 + countl_o_n1 + countl_v_n1 + countl_e_n1


# Name 2
name2_lower = name2.lower()

countt_t_n2 = name2_lower.count("t")
countt_r_n2 = name2_lower.count("r")
countt_u_n2 = name2_lower.count("u")
countt_e_n2 = name2_lower.count("e")

countt_total_n2 = countt_t_n2 + countt_r_n2 + countt_u_n2 + countt_e_n2


countl_l_n2 = name2_lower.count("l")
countl_o_n2 = name2_lower.count("o")
countl_v_n2 = name2_lower.count("v")
countl_e_n2 = name2_lower.count("e")

countl_total_n2 = countl_l_n2 + countl_o_n2 + countl_v_n2 + countl_e_n2

# Get the totals

countt_total = countt_total_n1 + countt_total_n2
countl_total = countl_total_n1 + countl_total_n2

string_countt = str(countt_total)
string_countl = str(countl_total)
string_total = string_countt + string_countl
integer_total = int(string_total)

if integer_total < 10 or integer_total > 90:
    print(f"Your score is {integer_total}, you go together like coke and mentos.")
elif integer_total >= 40 and integer_total <= 50:
    print(f"Your score is {integer_total}, you are alright together.")
else:
    print(f"Your score is {integer_total}.")
