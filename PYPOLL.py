# Importing the operating system and csv.
import os
import csv

election_csv_path = os.path.join('Resources', 'election_data.csv')
#importing the csv with path.
with open(election_csv_path) as elec_csvfile:

    # specifying the deliminter.
    elect_csv_reader = csv.reader(elec_csvfile, delimiter=',')
     # Reading the header of the csv.
    elect_csv_header = next(elect_csv_reader)
    
    # Initialise variables
    cnt0=0
    cnt1=0
    cnt2=0
    total_votes=0
    Candidates=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]

    #Using for loop with increament of 1 to store the total votes.
    #adding the number of votes in the variable total_votes.

    for row in elect_csv_reader:
        total_votes+=1
        if row[2]==Candidates[0]:
            cnt0=cnt0+1  
        elif row[2]==Candidates[1]:  
            cnt1=cnt1+1
        elif row[2]==Candidates[2]:  
            cnt2=cnt2+1  

    # creating a text file for output.
    with open(os.path.join("analysis", "output.txt"), "w") as f:       

        print("Election Results\n")
        print("Election Results\n",file=f)

        print("---------------------\n")
        print("---------------------\n",file=f)

        

        print("Total Votes: "+str(total_votes)+"\n")
        print("Total Votes: "+str(total_votes)+"\n",file=f)

        print("---------------------\n")
        print("---------------------\n",file=f)

        #Total no of votes each candidate won,percentage of votes each candidate won
        #and total number of votes each candidate won

        print(Candidates[0]+": "+str(round(float((cnt0/total_votes)*100),3))+"% ("+str(cnt0)+")\n")
        print(Candidates[0]+": "+str(round(float((cnt0/total_votes)*100),3))+"% ("+str(cnt0)+")\n",file=f)

        print(Candidates[1]+": "+str(round(float((cnt1/total_votes)*100),3))+"% ("+str(cnt1)+")\n")
        print(Candidates[1]+": "+str(round(float((cnt1/total_votes)*100),3))+"% ("+str(cnt1)+")\n",file=f)

        print(Candidates[2]+": "+str(round(float((cnt2/total_votes)*100),3))+"% ("+str(cnt2)+")\n")
        print(Candidates[2]+": "+str(round(float((cnt2/total_votes)*100),3))+"% ("+str(cnt2)+")\n",file=f)

        print("---------------------\n")
        print("---------------------\n",file=f)

        # Printing the name of the winner.
    
        if max(cnt0,cnt1,cnt2) == cnt0:
            winner=Candidates[0]
        elif max(cnt0,cnt1,cnt2) == cnt1:
             winner=Candidates[1]
        else:
             winner=Candidates[2]

        print("Winner: "+winner)
        print("Winner: "+winner+"\n",file=f)

        print("\n---------------------\n")
        print("\n---------------------\n",file=f)
        #Closing txt file.
        f.close()
    