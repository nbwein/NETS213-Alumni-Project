# NETS213-Alumni-Project

In order to have the appropriate data for this project, we will need to obtain a list of 
as many SEAS alumni as possible from the last 20 years (1995-2015). If feasible, this list 
should have each person’s name and major. Either Career Services or QuakerNet will be used 
to obtain this list (1 point). Next, we will import this data to CrowdFlower to create the tasks for 
our workers (4 points). The task will provide a worker with the name and major of an alumnus. It will 
first ask whether this person has a LinkedIn profile. Conditional on the answer to this 
question being “yes,” the worker will extract the following information from their profile, 
if available and/or applicable: 
  LinkedIn profile short URL
  Personal website URL
  Graduation Year
  Name of grad school
  For all jobs since graduation:
     Company
     Job Title
     Years employed
In order to ensure quality control throughout this project, we will design a thorough set 
of test questions (2 points). In order for people to be able to complete this task, they will have to 
answer a certain percentage of the test questions correctly. This will ensure that the 
workers completing this task know how to properly extract the information being requested. 
Additionally, we will have multiple workers fill in information for each alumnus and check 
whether responses match-up. In order to aggregate our responses, we will write a program 
to analyze the CSV file containing the results (4 points). The results can be sorted by various 
categories, such as major or graduating class. Aggregating the results by different 
categories will then allow us to analyze according to such categories (4 points). Some of the trends 
we will consider include: Do people from a particular major tend to go into the same field 
of work? How have trends changed over the past 20 years in terms what constitutes a 
“typical” job for a certain major? How have trends changed over the past 20 years in terms 
of how long people stay at their first job out of college? What is the average number of 
jobs for members of each graduating class?
