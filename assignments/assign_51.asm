
# assignment 51
# see lab 11

# Count from 0 to 100 in increments of 10

####################################################################
# not using $sp stack pointer here (b/c not outputing anything)
# so no need to set up $sp stack pointer
#
# n.b., $sp stack pointer (used in assignment 50) is NOT
# the same as $s0, $s1, and $s2 registers (used here)
#
# ADDI - adds an 'immediate' constant to a specified value
#	   	 (the 'immediate' constant used here is $zero)
# ADD  - adds value in one register to the value in another register
####################################################################


ADDI $s0, $zero, 0			# set $s0 register to 0
ADDI $s1, $zero, 10			# set $s1 register to 10
ADDI $s2, $zero, 100		# set $s2 register to 100

AGAIN: ADD $s0, $s0, $s1	# $s0 = $s0 + $s1

BEQ $s0, $s2, DONE			# if $s0 == $s2, branch down to 'DONE:' line
J AGAIN						# else, jump back up to 'AGAIN:' line

DONE:						# exit here at this 'DONE:' line
