#Importing all the dependencies.
import os
import csv
csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:

    # Specifying the delimiter and file.
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Reading the header row.
    csv_header = next(csv_reader)
    
    #Naming the variables that will store data.
    tot_mon=0
    netP_L=0
    avg_chng1 =[]
    pl = []
    dt=[] 
    y = 1
    avg=0
    z=0
    a=0
    pl_sum=0

    for x in csv_reader:
        #total number of months included in the dataset
        tot_mon +=1
        #total amount of "Profit/Losses" over the entire period
        netP_L +=int(x[1])
        dt.append(x[0])
        pl.append(int(x[1]))
        if tot_mon>=2 :
            avg_chng1.append(int(pl[y])-int(pl[y-1]))
            y=y+1
            avg += float(avg_chng1[z])
            z=z+1 
              
    #Calculating the average change and rounding to 2 decimal points.

    av_change=round(float(avg/len(avg_chng1)),2)

    #The greatest increase in profits (date and amount) over the entire period

    max_chng=max(avg_chng1)
    min_chng=min(avg_chng1)
    for a in range(len(avg_chng1)):
        if avg_chng1[a] == min_chng:
            min_dt=dt[a+1]
        if avg_chng1[a] == max_chng:
            max_dt=dt[a+1]
           
    #text file to write the result
    with open(os.path.join("analysis", "output.txt"), "w") as f:

        print ("Financial Analysis\n")
        print ("Financial Analysis\n",file=f)

        print("----------------------------\n")
        print("----------------------------\n",file=f)  

        #Printing the total months.
        print ("Total Months : "+str(len(pl))+"\n")
        print ("Total Months : "+str(len(pl))+"\n",file=f)

        #total of P/L value of the given period
        print ("Total : $"+str(netP_L)+"\n")
        print ("Total : $"+str(netP_L)+"\n",file=f)

        #Average Change in p\l
        print ("Average Change : $"+str(av_change)+"\n")
        print ("Average Change : $"+str(av_change)+"\n",file=f)

        #The greatest increase in profits
        print ("Greatest Increase in Profits: "+max_dt+" ($"+str(max_chng)+")\n")
        print ("Greatest Increase in Profits: "+max_dt+" ($"+str(max_chng)+")\n",file=f)

        #The greatest decrease in profits 
        print ("Greatest Decrease in Profits: "+min_dt+" ($"+str(min_chng)+")\n")
        print ("Greatest Decrease in Profits: "+min_dt+" ($"+str(min_chng)+")\n",file=f)

        #Closing the text file
        f.close()