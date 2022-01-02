# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2
# to 10 are given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
# cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


largest = 0
final = 0
for dem in range(2, 1000):        # 1/2 to 1/999
        num = 10 ** len(str(dem)) #starting at 10 and adjusting as the numbers get larger
        if num % dem != 0:        #only continue if 10 / dem produces a remainder
            
            repeats = []           #stores the division results for given dem 
            length = 0             #number of operations/length of decimal
            remain = 0             #remainder of int div
            
            while num not in repeats:    #runs until same numerator appears
                
                remain = num % dem
                repeats.append(num)
                if num % dem != 0:    #checks to see if this operation has happened before, if it has not, the result is stored
                    
                    num = remain * 10        #dropping down a zero                    
                    length = len(repeats)    #i need to store the remainder *10, that gives me the next term and if they are the same, they are repeating
                    
            
            if length > largest:
                largest = length - 1
                final = dem


                

print(final, largest)
