# ###################################################
#					INFORMATION
# ###################################################

	PEOJECT...................: dotFill
	VERSION...................: 0.1 a
	
	DESCRIPCION:
	
	dotFill is a little function with the objective
	of print dots between 2 text pieces. The idea is
	to format the output of info putting the dots
	after the first column and X tabs after, in the
	next column. Like the spaces number can be different
	the dots filled the different distance.

	sample:
	
	The dots are filling diferent number of spaces. 
	That is dotFill function.
		
	Checking RAM.............: [OK]
	Checking disk space......: [OK]
    Users....................: [OK]

	By the moment, the script has 3 functions what are three differents
	ways to print the dots.

  - Write print with tabs (\t)
	- Tabs are expanded (4 spaces in each TAB)
	-  Replace two spaces to two dots (Space between words doesn´t replace)

  - Write dots next to col limit 
	- Doesn´t matter the long of words. While exist space to print dots
		next to a limit what you decide, the dots will be print

  - Progressively print 
	- Dots are printed at screen one by one like a progress bar next to the last
		column indicated. Always ends at this last column becasuse wrote characters
		are counted and extracted of the complete number.

	TODO:

	- Im planning to give the option of print whith colors but is important that
		will be sopported in every OS, not only linux or Mac



