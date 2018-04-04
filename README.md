# LSA-Tool
The script gets a list of words from an excel sheet and will upload them to the following website: http://lsa.colorado.edu/cgi-bin/LSA-matrix.html, "This interface allows you to compare the similarity of multiple texts or terms within a particular LSA space. Each text is compared to all other texts." The results for each subject will be saved in individual CSV  files.

This python programming is written using 2.7 version, and it will work on version 2 only, If this is the first time you are running this tool, make sure you have the necessary libraries installed If you already have the following libraries, you can skip to the parameters section.

The libraries you need to install before running the code are: 
'mechanize', 'bs4', 'pandas' , 'xlrd' 

In order to install these libraries, open windows command prompt and use 'pip' method, here is an example:
after you opened command prompt type in:

C:\Python27\Scripts\pip install mechanize	

This example would install 'mechanize' library, and this needs to be done for all the libraries if you don't have them installed.
And remember, in your computer Python could be installed in a different directory, so make sure you get the path correctly.

REALLY IMPORTANT: if you have TRUE and FALSE in your table as real world, before running the code, make sure you change their cell type to text format in the excel sheet and retype them.(if you didn’t type them after you changed the format to text it won't change anything and python will read them as 1 and 0).

This code will take words from each row and puts them in a list, and depending on how many responses each subject has, the code will gather all responses and adds to a list. for example, if there are three responses per subject the code will only upload the words to LSA website once all three rows have been added to the list. number of responses are also one of the parameters, make sure you update that as well.

Running the code

1-	Double click on the python code

2-	First the application will ask for a file and you should know where it is located using your browser, all you have, is, to feed the excel file to the program. 

3-	Second, it will ask for a parameter file which is the same as Read me file. I suggest having a separate parameter file for each individual experiment.

4-	Third it will ask for a directory to save the output files, you just need to select the folder you want your output to be saved.
The results should be saved in the folder you provided for the script, in individual tables.

If you had any problem running the script, you should contact Mehrdad Vaziri at mehrdadv@mail.usf.edu

