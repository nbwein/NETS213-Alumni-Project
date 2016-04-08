import csv

# the file will have two outputs. the first being the data, and the second being either yes or no 
# This program will output the result as to whether or not the overall labeling of the information 
# we have gathered is right. We will then sort this file and keep all the yes results, and take the information
#from the no results and put them back into crowdflower to see if other workers can give us better answers

with open('sample_aggregation_data.csv') as f:

    info_dictionary = {};
    for line in csv.reader(f, '\t'):
        information = line[0]
        correct = line[1]
        if information not in info_dictionary
            info_dictionary[information] = [0, 0]

        if correct == 'yes' :
            info_dictionary[information][0] += 1
        else 
            info_dictionary[information][1] += 1

    labels = {}
    for info in info_dictionary :
        if info_dictionary[info][0] > info_dictionary[info][1] :
        labels[info] = 'yes'
    else :
        labels[info] = 'no'

for url in labels :
    print url, '\t', labels[url]
end 
