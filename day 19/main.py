"""
--- Day 19: Monster Messages ---
-Strategy:
You can implement some context-free grammar algorithms (which are hard to understand) or try to do a recursive
search and check.
"""


def check_string(rules, st, rules_list):
    """
    Check if a given string can be produced using the given list of rules
    :param rules: Dict of rules
    :param st: String which is checked against the rules
    :param rules_list: List of rules
    :return: True/False
    """
    # Base case, if the string or list of rules is empty
    if st == '' or rules_list == []:
        # True only if both are empty, False otherwise
        return st == '' and rules_list == []

    # Check against the first rule in the list
    first_rule = rules[rules_list[0]]
    if '"' in first_rule:
        # The rule is only a letter
        if st[0] in first_rule:
            # Check the string without the first letter
            return check_string(rules, st[1:], rules_list[1:])
        else:
            # Wrong letter
            return False
    else:
        # Else, expand the rule
        return any(check_string(rules, st, sub_entry + rules_list[1:]) for sub_entry in first_rule)


def parse_rule(rule):
    """
    Transform the given string to a list of rules
    :param rule: String
    :return: Tuple of the name/number of the rule and it's entry
    """
    name, entry = rule.split(": ")
    # If the rule is not a single letter, create a list with the sub-entries
    if '"' not in entry:
        entry = [[int(rule_name) for rule_name in sub_entry.split()] for sub_entry in entry.split("|")]
    return int(name), entry


def part1(list_of_rules, messages_to_be_checked):
    """
    First part of the problem
    """
    # Create a dictionary for the given rules and count how many messages are valid according to them
    rules_dict = dict(parse_rule(rule) for rule in list_of_rules)
    return sum(check_string(rules_dict, message, [0]) for message in messages_to_be_checked)


def part2(list_of_rules, messages_to_be_checked):
    """
    Second part of the problem
    """
    # Rules for the second part (add the special rules)
    rules_dict = dict(parse_rule(rule) for rule in list_of_rules + ["8: 42 | 42 8", "11: 42 31 | 42 11 31"])
    return sum(check_string(rules_dict, message, [0]) for message in messages_to_be_checked)


if __name__ == '__main__':
    f = open('input.txt', 'rt')
    rule_text, messages = [x.splitlines() for x in f.read().split("\n\n")]
    print("Part 1: ", part1(rule_text, messages))
    print("Part 2: ", part2(rule_text, messages))
    f.close()
