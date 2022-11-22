
# assignment 50
# see lab 11

# Store 'I use MIPS!' at the top of the stack, and then call the stack

# setup: add 12 to stack pointer (11 characters in string + final null)
ADDI $sp, $sp, -12

ADDI $t0, $zero, 73   # I
SB $t0, 0($sp)        # save byte in $t0 register to $sp 0

ADDI $t0, $zero, 32   # (space)
SB $t0, 1($sp)        # save byte in $t0 register to $sp 1

ADDI $t0, $zero, 117  # u
SB $t0, 2($sp)        # save byte in $t0 register to $sp 2

ADDI $t0, $zero, 115  # s
SB $t0, 3($sp)        # save byte in $t0 register to $sp 3

ADDI $t0, $zero, 101  # e
SB $t0, 4($sp)        # save byte in $t0 register to $sp 4

ADDI $t0, $zero, 32   # (space)
SB $t0, 5($sp)        # save byte in $t0 register to $sp 5

ADDI $t0, $zero, 77   # M
SB $t0, 6($sp)        # save byte in $t0 register to $sp 6

ADDI $t0, $zero, 73   # I
SB $t0, 7($sp)        # save byte in $t0 register to $sp 7

ADDI $t0, $zero, 80   # P
SB $t0, 8($sp)        # save byte in $t0 register to $sp 8

ADDI $t0, $zero, 83   # S
SB $t0, 9($sp)        # save byte in $t0 register to $sp 9

ADDI $t0, $zero, 33   # !
SB $t0, 10($sp)       # save byte in $t0 register to $sp 10

ADDI $t0, $zero, 0    # (null)
SB $t0, 11($sp)       # save byte in $t0 register to $sp 11

ADDI $v0, $zero, 4    # set 4 at $v0 register for printing string
ADDI $a0, $sp, 0      # set location for start of message at $sp 0
syscall 			  # print to the log
