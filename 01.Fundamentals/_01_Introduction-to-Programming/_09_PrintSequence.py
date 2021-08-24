import math

def build_sequence(seq_size):
    start = 2
    seq = ""
    upper_bound = int(start + seq_size)
    seq += str(start)
    # method zero size check (vs input check)
    if (seq_size == 0): return "";
    for step in range(start + 1, upper_bound):
        if (step & 1):  # odd
            seq += ", " + str(step * - 1)
        else:
            seq += ", " + str(step)

    return seq


if __name__ == '__main__':
    seq_size = 10
    user_input_seq_size = int(math.fabs(int(input("Enter sequence size(defaults for sequence size of 10): ") or 0)))
    # input zero-size check
    if user_input_seq_size > 0: seq_size = user_input_seq_size
    print(build_sequence(seq_size))