import math


def print_sequence(seq_size):
    start = 2
    seq = ""
    upper_bound = int(start + seq_size)
    seq += str(start)
    for step in range(start + 1, upper_bound):
        if (step & 1):  # odd
            seq += ", " + str(step * - 1)
        else:
            seq += ", " + str(step)

    print(seq)


seq_size = 10
user_input_seq_size = math.fabs(int(input("Enter sequence size: ") or 0))
if user_input_seq_size > 0: seq_size = user_input_seq_size
print_sequence(seq_size)
