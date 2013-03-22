#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def dotFillTabs(theString=''):
    """ Function that changes tabs for spaces (4 spaces for each tab) and replace them with dots """
    theResult = theString.expandtabs(4).replace("  ", "..")
    return theResult

def dotFillToCol(theString='',lastCol=30):
    """ Function writes dots to the spacified column of characters counting from first character in the print clausule not from screen edge """
    wroteChars = len(theString)
    totalDots = lastCol - int(wroteChars)
    return theString + '.'*totalDots


# Sample 1
# Using dotFillTabs

testTabs1 = 'check1 screen\t\t'  # 2 tabs
testTabs2 = 'check2 ram\t\t\t'  # 3 tabs
testTabs3 = 'check3\t\t\t\t'  # 4 Tabs

checkOK = ': [OK]'
checkKO = ': [KO]'

print 'Function dotFillTabs'
print "_"*20

print dotFillTabs(testTabs1) + checkKO
print dotFillTabs(testTabs2) + checkOK
print dotFillTabs(testTabs3) + checkOK

# Sample 2
# Using dotFillCols

print 'Function dotFillToCol'
print "_"*20

testCols1 = 'check1 memo'
testCols2 = 'check2 ram'
testCols3 = 'check3'

print dotFillToCol(testCols1,20) + checkOK
print dotFillToCol(testCols2,20) + checkKO
print dotFillToCol(testCols3,20) + checkOK




