"""
Day 8 using Python
although the code looks like assembly
"""

f = open('input.txt', 'rt')


def execute_code():
    # executes the code in assembly_program

    # dict to keep each done operation
    executed_lines = dict()
    # accumulator register
    acc = 0
    # index for lines of code
    index = 0
    while index < len(assembly_program):
        if index in executed_lines:
            # for part 1
            # return acc
            return 0
        executed_lines[index] = 1
        command, argument = assembly_program[index].split(' ')
        # execute commands
        if command == 'nop':
            index += 1
        elif command == 'acc':
            acc += int(argument)
            index += 1
        else:
            index += int(argument)
    # if the program is not an infinite loop, return the accumulator
    return acc


if __name__ == '__main__':
    assembly_program = f.readlines()

    # for part 1
    # print (execute_code())

    # keep a list of all the lines
    nop_jump_lines = [index for index, line in enumerate(assembly_program) if 'nop' in line or 'jmp' in line]
    for index in nop_jump_lines:
        # switch the value of the line and execute the program
        if 'nop' in assembly_program[index]:
            new_command = 'jmp' + assembly_program[index][3:]
            assembly_program[index] = new_command
            acc_value = execute_code()
            if acc_value:
                print(acc_value)
                break
            old_command = 'nop' + assembly_program[index][3:]
            assembly_program[index] = old_command
        else:
            new_command = 'nop' + assembly_program[index][3:]
            assembly_program[index] = new_command
            acc_value = execute_code()
            if acc_value:
                print(acc_value)
                break
            old_command = 'jmp' + assembly_program[index][3:]
            assembly_program[index] = old_command
