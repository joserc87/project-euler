
__author__ = 'joserc87'

import sys
import math

class Problem:
	""" A class to solve a generic problem """

	problemNumber = 0;
	problemTitle = "";
	problemDescription = "** Problem title not specified **";


	# Common parameters are -v (--verbose), -n (problem limit), -p (--print-definition), -h (--help)
	programName = "";
	verbose = False;
	problemTarget = -1;
	showProblemDescription = False;
	showHelp = False;


	def __init__(self, probNum, probTitle, probDescr, probDefaultTarget, args):
		""" Default constructor """
		self.verbose = self.showProblemDescription = self.showHelp = False;
		self.problemNumber = probNum;
		self.problemTitle = probTitle;
		self.problemDescription = probDescr;
		self.problemTarget = probDefaultTarget;
		self.parseArguments(args);

	def solve(self, n):
		""" Solves the euler problem for the number n and return the solution as an integer """
		return 0;

	def parseArguments(self, args):
		""" Parse the program argumets """
		i = 1;
		argc = len(args);
		correct = True;
		programName = str(args[0]);
		while (i < argc and correct):
			arg = str(args[i]);
			if (arg == '-v' or arg == '--verbose'):
				self.verbose = True;
			elif (arg == '-p' or arg == '--print-description'):
				self.showProblemDescription = True;
			elif (arg == '-h' or arg == '--help'):
				self.showHelp = True;
			elif (arg == '-n'):
				i+=1; # Increment twice because of the extra parameter
				self.problemTarget = int(args[i]);
			else:
				# Unrecognized parameters.
				self.problemTarget = -1;
				self.verbose = False;
				self.showProblemDescription = False;
				self.showHelp = True;
				correct = False;
			i+=1;

	def run(self):
		if (self.showHelp):
			self.printUsage();
		elif (self.showProblemDescription):
			self.printProblemDescription();
		else:
			solution = self.solve(self.problemTarget);
			print ("The solution for " + str(self.problemTarget) + " is " + str(solution));


	def printUsage(self):
		print(	"Usage: " + str(self.programName) + " -[vph] [-n NUMBER]\n" + \
				"Solves the euler problem number " + str(self.problemNumber) + "\n" + \
				"\t-v, --verbose            verbosely outputs the process\n" + \
				"\t-p, --print-definition   prints the definition of the euler problem\n" + \
				"\t-h, --help               prints this help\n" + \
				"\t-n NUMBER                Changes the input for the euler problem (integer bigger than 0)\n");

	def printProblemDescription(self):
		""" Prints the euler problem definition """
		print ('');
		lineLength = len(self.problemTitle) + 6;

		# DOTS
		for i in range(lineLength):
			print ('*', end='');
		print('\n*', end='');

		# PROBLEM NUMBER
		for i in range(math.floor((lineLength - 14)/2)):
			print (' ', end='');
		print ("PROBLEM " + "%03d" % self.problemNumber + ":", end='')
		for i in range(math.ceil((lineLength - 14)/2)):
			print (' ', end='');
		print('*\n*', end='');

		# EMPTY LINE
		for i in range(lineLength - 2):
			print (' ', end='');
		print('*');

		# TITLE
		print("* \"" + str(self.problemTitle) + "\" *");
		# DOTS
		for i in range(lineLength):
			print ('*', end='');
		# DESCRIPTION
		print ("\n\n" + str(self.problemDescription) + "\n");
