"""
Question 06: String comprehension
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
"""
import sys

def string_comprehension(input_string: str) -> str:
    output = ""
    cnt = 1
    for idx in range(1, len(input_string)):
        if input_string[idx] == input_string[idx - 1]:
            cnt += 1
        else:
            output = output + input_string[idx - 1] + str(cnt)
            cnt = 1

    # Last set of chars
    output = output + input_string[-1] + str(cnt)

    # Check length and return
    return output if len(output) < len(input_string) else input_string


def main(argv):
    string_1 = argv[0]
    print(string_comprehension(string_1))


if __name__ == '__main__':
    main(sys.argv[1:])
