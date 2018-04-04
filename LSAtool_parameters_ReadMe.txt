#This python programming is writting using 2.7 version, and it will work on version 2 only,
#If this is the first time you are running this tool, make sure you have the necessary libraries installed
#If you already have the following libraries, you can skip to the parameters section.

#The libraries you need to install before running the code are: 
#'mechanize', 'bs4' , 'pandas' , 'xlrd' , lxml,
#You open windows command prompt and use 'pip' method, here is an example:
#after you opened command prompt type in:
#C:\Python27\Scripts\pip install mechanize		
#this example would install 'mechanize' library, and this needs to be done for all the libraries if you don't have them installed
#And remember, in your computer Python could be installed in a different directory, so make sure you get the path correctly.


#REALLY IMPORTANT: if you have TRUE and FALSE in your table as real world, before running the code, make sure you change
#their cell type to text format in the excel sheet and retype them.(if you don't type them after you changed the format to
#text it won't change anything and python will read them as 1 and 0).
#This particular code will take words from each row and puts them in a list, and depending on how many response each 
#subject has, the code will gather all responses and adds to a list. for example if there are three responses per subject
#the code will only upload the words to LSA once all three rows have been added to the list. 
#number of responses are also one of the paramateres, make sure you update that as well.

##PARAMETERS
#The following part is the parameters the code needs in order to run. DO NOT remove any hashtag signs or value titles,
#only change the numbers in front of them according to your excel sheet

#How many responses each subject has?-->nr 
nr = 3
#Which sheet do you want to work on? --> sh
sh = 2
#Which column index is the subject number? --> sid
sid = 1
#Which Column index is the first word? --> cfw
cfw = 7
#which Column index is the last word? --> clw
clw = 15
#Which row index is the first word? --> rfw
rfw = 259
#Which row index is the last word? --> rlw 
rlw=261

##Running the code

#Double click on the python code
#First the application will ask for a file and you should know where it is located using your browser, all you have to do
#is to feed the excel file to the program. 
#Second, it will ask for a parameter file which is the same as Read me file.(the one you are currently reading)
#I suggest having a seperate parameter file for each individual experiment.
#Third it will ask for a directory to save the output files, you just need to 
#select the folder you want your output to be saved.
#The results should be saved in the folder you provided for the script, in individual tables.


#If you had any problem running the script, you should contact Mehrdad Vaziri at mehrdadv@mail.usf.edu
