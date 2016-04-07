# NETS213-Alumni-Project

In order to have the appropriate data for this project, we will need to obtain a list of 
as many SEAS alumni as possible from the last 20 years (1995-2015). If feasible, this list 
should have each person’s name and major. Either Career Services or QuakerNet will be used 
to obtain this list (1 point). Next, we will import this data to CrowdFlower to create the tasks for 
our workers (4 points). The task will provide a worker with the name and major of an alumnus. It will 
first ask whether this person has a LinkedIn profile. Conditional on the answer to this 
question being “yes,” the worker will extract the following information from their profile, 
if available and/or applicable: <br />
  LinkedIn profile short URL<br />
  Personal website URL<br />
  Graduation Year<br />
  Name of grad school<br />
  For all jobs since graduation:<br />
     --Company<br />
     --Job Title<br />
     --Years employed<br />
In order to ensure quality control throughout this project, we will design a thorough set 
of test questions (2 points). There will be two rounds to the test questions. 
An example of these questions is attached in the directory. Essentially, 
because our initial questions to the workers are open ended, we are going to make multiple choice question
to ensure the workers are knowledgeable enough to complete these tasks, but these test questions wont
eliminate workers simply for phrasing the job slightly differently than in the test question (ie by 
forgetting a space or a "."). In the first round, workers will be asked to sort through information and choose the 
right choice. In the second round of test questions, workers will verify that the data taken from the first crowdsourcing 
job posted is correct. In order for people to be able to complete each crowdsourcing task, they will have to 
answer a certain percentage of the test questions correctly. This will ensure that the 
workers completing this task know how to properly extract the information being requested. 
Additionally, we will have multiple workers fill in information for each alumnus and check 
whether responses match-up (for the first section). In order to aggregate our responses, we will write a program 
to analyze the CSV file containing the results (4 points). The results can be sorted by various 
categories, such as major or graduating class. Aggregating the results by different 
categories will then allow us to analyze according to such categories (4 points). Some of the trends 
we will consider include: Do people from a particular major tend to go into the same field 
of work? How have trends changed over the past 20 years in terms what constitutes a 
“typical” job for a certain major? How have trends changed over the past 20 years in terms 
of how long people stay at their first job out of college? What is the average number of 
jobs for members of each graduating class?


Data:<br />
Our raw input data will be in the format of a .txt file containing alumni names, graduation year, and some other information. Information regarding each alumnus will be separated by line-breaks in the text file.


