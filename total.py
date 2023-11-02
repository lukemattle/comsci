#Sales quantities of a certain item, calculated to the nearest thousand, 
#for Jan-March, April-June, July-Sep and Oct-Dec are held in separate arrays for each of 3 outlets. 
#The sales figures for each quarter are to be totalled and output in the format

#	Total for quarter 1 xxxx
#	Total for quarter 2 xxxx
#	Total for quarter 3 xxxx
#	Total for quarter 4 xxxx

#	Write a pseudocode algorithm for this program. 

Outlet1Sales = [10,12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]

pos = 0
quarter = []

for i in range(4):
    temp1 = Outlet1Sales[pos]
    temp2 = Outlet2Sales[pos]
    temp3 = Outlet3Sales[pos]
    pos += 1
    quarter.append((temp1+temp2+temp3))

print ('Total for quarter 1: ' + str(quarter[1]) + '\nTotal for quarter 2: ' + str(quarter[2]) + '\nTotal for quarter 3: ' + str(quarter[3]))