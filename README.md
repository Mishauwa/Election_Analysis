# Election_Analysis

Link to the Analysis and written code: https://github.com/Mishauwa/Election_Analysis/blob/main/PyPoll_Challenge.py

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit 
of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doana received 3.1% of the vote and 11.606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Challenge Overview
In addition to the first election analysis the Colorade Board would like to see more data with the focus on each county.

1. The voter tournout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout 

## Challenge Election-Audit Results

The analysis of the election shows that:

- In total there have been 369.711 votes
- Below you can find a breakdown of the number of votes and percentage of total votes for each county

    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)

- The county with the largest turnout is Denver
- Below you can find a breakdown of the number of votes and the percentage of the total votes each candidate received

  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

- Diana DeGette won the election with a total of 272,892 votes and 73.8% of the votes

[election_analysis.txt](https://github.com/Mishauwa/Election_Analysis/files/9539032/election_analysis.txt)



## Challenge Summary

Next to the analysis the underlying script is also for purchase. The script can be used with slight modifications for any elections and is easily written. 
It's possible to load different csv files and use the script. 

One example is to use the script for the next years election with new candidates. For that you only use the next years csv file. 
The file has to be formatted in the same way or the index of the candidates name and counties name in the for loop has to be adjusted. Also the path where the file is stored has to be adjusted to the new location and file name. A new text file should be created. For that the save path has to be changed. 

A second example is to use the election results from different counties. For that example you have to load also a new csv file. Format the csv in the right way and follow the steps above. 




