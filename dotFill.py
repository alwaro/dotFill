#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

def dotFillTabs(theString=''):
    """ Function that changes tabs for spaces (4 spaces for each tab) and replace them with dots """
    theResult = theString.expandtabs(4).replace("  ", "..")
    return theResult

def dotFillToCol(theString='',lastCol=30):
    """ Function writes dots to the spacified column of characters counting from first character in the print clausule not from screen edge """
    wroteChars = len(theString)
    totalDots = lastCol - int(wroteChars)
    return theString + '.'*totalDots

def dotFillToColProgress(theString='',lastCol=30,showSpeed=0.1):
    """ Function similar to dotFillToCol but each dot is apearing in screen progressively """
    wroteChars = len(theString)
    totalDots = lastCol - int(wroteChars)
    for num in xrange(1, totalDots):
        print '\r'+theString+'.'*num,
        time.sleep(0.2)




# Sample 1
# Using dotFillTabs

testTabs1 = 'check1 screen\t\t'  # 2 tabs
testTabs2 = 'check2 ram\t\t\t'  # 3 tabs
testTabs3 = 'check3\t\t\t\t'  # 4 Tabs

checkOK = ': [OK]'
checkKO = ': [KO]'

print '\n\nFunction dotFillTabs'
print "_"*20

print dotFillTabs(testTabs1) + checkKO
print dotFillTabs(testTabs2) + checkOK
print dotFillTabs(testTabs3) + checkOK

# Sample 2
# Using dotFillCols

print '\n\nFunction dotFillToCol'
print "_"*20

testCols1 = 'check1 memo'
testCols2 = 'check2 ram'
testCols3 = 'check3'

print dotFillToCol(testCols1,20) + checkOK
print dotFillToCol(testCols2,20) + checkKO
print dotFillToCol(testCols3,20) + checkOK


print '\n\nFunction dotFillToColProgress'
print "_"*20

dotFillToColProgress(testCols1,20) #+ checkOK
dotFillToColProgress(testCols2,20) #+ checkKO
dotFillToColProgress(testCols3,20) #+ checkOK




