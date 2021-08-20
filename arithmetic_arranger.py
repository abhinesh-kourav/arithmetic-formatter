import re
def arithmetic_arranger(problems,bool=False):
  topLine = ""
  bottomLine = ""
  dashLine = ""
  resLine= ""
  if len(problems)>5:
    return "Error: Too many problems."
  for problem in problems:
    if "*" in problem or "/" in problem:
      return "Error: Operator must be '+' or '-'."
    elif "+" in problem or "-" in problem:
      operands = problem.split(" ") 
      first = operands[0]
      operator = operands[1]
      second = operands[2]
    if re.search('/D',first):
      return "Error: Numbers must only contain digits."
    if re.search('[^\d\s]',second):
      return "Error: Numbers must only contain digits."
    if len(first)>4 or len(second)>4:
      return "Error: Numbers cannot be more than four digits." 
    result = str(eval(problem))
    maxlen = max(len(first),len(second))
    length = maxlen + 2
    top = first.rjust(length)
    bottom = operator + second.rjust(length-1)
    res = result.rjust(length)
    dash = ''
    for s in range(length):
      dash = dash + '-'
    if problem != problems[-1]:
      topLine += top + "    "
      bottomLine += bottom + "    "
      dashLine += dash + '    '
      resLine += res + '    '
    else: 
      topLine += top
      bottomLine += bottom
      dashLine += dash
      resLine += res
  
  if bool:
    return topLine + '\n' + bottomLine + '\n' + dashLine +  '\n' + resLine
  else:
    return topLine + '\n' + bottomLine + '\n' + dashLine

#print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],True))