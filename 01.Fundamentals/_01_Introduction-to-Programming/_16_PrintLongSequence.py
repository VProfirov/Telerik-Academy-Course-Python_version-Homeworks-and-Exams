from _09_PrintSequence import build_sequence
import math

seq_size = 1000
user_input_seq_size = math.fabs(int(input("Enter a large size for the sequence build: ")))
if user_input_seq_size > 0: seq_size = user_input_seq_size
sequence = build_sequence(seq_size)
print(sequence)

# TODO: Solve for the improting of file without running the function calls in it!!!