def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
            
        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'
            
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
        length = max(len(operand1), len(operand2)) + 2
        
        first_line.append(operand1.rjust(length))
        second_line.append(operator + operand2.rjust(length - 1))
        dashes.append('-' * length)
        
        if show_answers:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            answers.append(str(result).rjust(length))
            
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes)
    )
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)
        
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')