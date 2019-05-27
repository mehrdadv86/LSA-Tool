#-------------------------------------------------------------------------------
# Name:        LSA Tool V1.1
# Purpose:     The script gets a list of words from an excel sheet and will
#              upload them to the following website: http://lsa.colorado.edu/cgi-bin/LSA-matrix.html,
#              "This interface allows you to compare the similarity of multiple
#              texts or terms within a particular LSA space. Each text is compared to all other texts."
#              The results for each subject will be saved in individual CSV
#              files.
#
# Author:      Mehrdad Vaziri
# email:       mehrdadv@mail.usf.edu
#
# Created:     04/04/2018
# Updated:     05/27/2019
# Copyright:   (c) Mehrdad 2019
# 
#-------------------------------------------------------------------------------

import sys
from mechanize import Browser
import pandas as pd
import time
import xlrd
from Tkinter import Tk
from tkFileDialog import askopenfilename,askdirectory


Tk().withdraw()
xlspath=askopenfilename(title = "Select Excel sheet of the words") #Loading the file
filename = askopenfilename(title = "Select Parameter file", filetype = (("TXT files","*.txt"),("all files","*.*")))
outputFolder=askdirectory(title = "Select a folder to save the tables") #Where do you want to save it
print "Reading "+ xlspath


try:
	parameters = open(filename,'r')
	#this reads the file as text
	whole_file = parameters.read()
	#this executes the whole thing as code
	exec(whole_file)
	parameters.close()

except:
	print ("Your parameter file could not be found.  Or, there is an error in the file.")
	sys.exit(0)


def processXLS(xlspath,outputFolder):
    rows=[]            
    wb1 = xlrd.open_workbook(xlspath)
    sh1 = wb1.sheet_by_index(sh-1)
    for rownum in range(rfw-1,rlw):
        rows += [sh1.row_values(rownum,start_colx=sid-1, end_colx=clw)]
    
    wlist = []
    for item in rows:

        id = item[sid-1]
        tid = type(item[sid-1])
        del item [sid:cfw-1]
        for x in item:
            if x !="":
                wlist.append(str(x))
        if tid==float:
            outputname = int(id)
        if tid==unicode or tid==str:
            outputname = wlist[sid-1]
        outName = "subject_%s.csv"%outputname

        if len(wlist)>=2:
            result = getMatrixPage(wlist[-(len(wlist)-1):])
            try:
                result.to_csv(outputFolder+"\\"+outName,index=False)

            except:
                print (result)
            wlist = []
            time.sleep(2)

def getMatrixPage(listKeyWords,url="http://lsa.colorado.edu/cgi-bin/LSA-matrix.html",numFactors="150"):
    """Submit the form and get the soup
    listKeyWords - list each element is a new line of text.
    url - path to the lsa matrix website
    numFactors - string of the number of factors"""
    print(listKeyWords)
    if listKeyWords ==".":
        pass
    submitText = "\r\n\r\n".join(listKeyWords)

    br = Browser()

    print ("\ntry browser\n")
    br.open(url)
    br.select_form(nr=0)
    br["LSAFactors"] = numFactors
    br["txt1"]=submitText

    br.submit()


    df =  pd.read_html(br.response().read(),header =0)

    br.response().close()
    del br
    return df[0]

processXLS(xlspath,outputFolder)
