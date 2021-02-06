from _09_PrintSequence import build_sequence
import math

# NOTE: The functionality of building the sequence is in the _09_PrintSequence.build_sequence() function
seq_size = 1000
user_input_seq_size = int(math.fabs(int(input("Enter a large size for the sequence build (defualts to 1000): ") or 0)))
if user_input_seq_size > 0: seq_size = user_input_seq_size
sequence = build_sequence(seq_size)
print(sequence)