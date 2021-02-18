"""
--- Day 8: Handheld Halting ---
Strategy:
- Execute each line of code (which looks like assembly)
"""


def execute_code(part_2=True):
    """
    Executes the code in assembly_program
    :return: The value in the accumulator at the end of the execution
    """
    # Dict to keep each done operation
    executed_lines = dict()
    # Accumulator register
    acc = 0
    # Index for lines of code
    index = 0

    while index < len(assembly_program):
        # Check for an infinite loop
        if index in executed_lines:
            if not part_2:
                # Difference between Part 1 and Part 2 of the problem
                return acc
            return 0

        # Mark the line
        executed_lines[index] = 1

        # Get the command and execute it
        command, argument = assembly_program[index].split(' ')

        # Execute commands
        if command == 'nop':
            index += 1
        elif command == 'acc':
            acc += int(argument)
            index += 1
        else:
            index += int(argument)

        # If the program is not an infinite loop, return the accumulator
    return acc


def switch_and_execute(index, old_word, new_word):
    """
    Switches between the commands at index and executes the new code
    :return: Accumulator value (if the code executed successfully) or None
    """
    # Switch old_word to new_word
    new_command = new_word + assembly_program[index][3:]
    assembly_program[index] = new_command
    acc_value = execute_code()

    # Return accumulator value if the program ended successfully
    if acc_value:
        return acc_value

    # Switch back
    old_command = old_word + assembly_program[index][3:]
    assembly_program[index] = old_command

    return None


def part1():
    """
    Part 1 of the problem
    """
    return execute_code(False)


def part2():
    """
    Part 2 of the problem
    """
    # Keep a list of all the nop/jmp lines
    nop_jump_lines = [index for index, line in enumerate(assembly_program) if 'nop' in line or 'jmp' in line]

    for index in nop_jump_lines:
        # Switch the value of the line and execute the program
        # Return if the program ended successfully
        if 'nop' in assembly_program[index]:
            value = switch_and_execute(index, 'nop', 'jmp')
            if value:
                return value
        else:
            value = switch_and_execute(index, 'jmp', 'nop')
            if value:
                return value


if __name__ == '__main__':
    f = open('input.txt', 'rt')
    assembly_program = f.readlines()

    print("Part 1: ", part1())
    print("Part 2: ", part2())

    f.close()
