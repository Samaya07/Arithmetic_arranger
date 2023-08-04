def arithmetic_arranger(problems, answer=False):
  list_num1 = []
  list_num2 = []
  list_answer = []
  list_operator = []
  list_max = []
  list_operands = []
  arranged_problems = ""
  if (len(problems) > 5):
    error = "Error: Too many problems."
    return error
  for problem in problems:
    list_operands = problem.split(' ')
    num1 = list_operands[0]
    num2 = list_operands[2]

    for ele in num1:
      if ele.isdigit() != True:
        return "Error: Numbers must only contain digits."
    for ele in num2:
      if ele.isdigit() != True:
        return "Error: Numbers must only contain digits."
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    list_num1.append(num1)
    if (list_operands[1] == '*' or list_operands[1] == '/'):
      return "Error: Operator must be '+' or '-'."
    list_operator.append(list_operands[1])
    list_num2.append(num2)

  list_length = len(list_num1)
  for i in range(0, list_length):
    if (list_operator[i] == '-'):
      list_answer.append(int(list_num1[i]) - int(list_num2[i]))
    else:
      list_answer.append(int(list_num1[i]) + int(list_num2[i]))

  for i in range(0, list_length):
    if (int_len(int(list_num1[i])) < int_len(int(list_num2[i]))):
      diff = int_len(int(list_num2[i])) - int_len(int(list_num1[i]))
      space = ' ' * diff
      arranged_problems = arranged_problems + space + "  " + list_num1[i]
    elif (int_len(int(list_num1[i])) > int_len(int(list_num2[i]))):
      diff = int_len(int(list_num1[i])) - int_len(int(list_num2[i]))
      arranged_problems = arranged_problems + "  " + list_num1[i]
    else:
      arranged_problems = arranged_problems + "  " + list_num1[i]
    if (i < list_length - 1):
      arranged_problems = arranged_problems + " " * 4

  arranged_problems = arranged_problems + "\n"

  for i in range(0, list_length):
    if (int_len(int(list_num1[i])) < int_len(int(list_num2[i]))):
      arranged_problems = arranged_problems + list_operator[
        i] + " " + list_num2[i]
    elif (int_len(int(list_num1[i])) > int_len(int(list_num2[i]))):
      diff = int_len(int(list_num1[i])) - int_len(int(list_num2[i]))
      arranged_problems = arranged_problems + list_operator[
        i] + " " + " " * diff + list_num2[i]
    else:
      arranged_problems = arranged_problems + list_operator[
        i] + " " + list_num2[i]
    if i < list_length - 1:
      arranged_problems = arranged_problems + " " * 4

  arranged_problems = arranged_problems + "\n"

  for i in range(0, list_length):
    if (int_len(int(list_num1[i])) > int_len(int(list_num2[i]))):
      max = int_len(int(list_num1[i]))
    else:
      max = int_len(int(list_num2[i]))
    list_max.append(max + 2)
    arranged_problems = arranged_problems + "-" * (max + 2)
    if (i < list_length - 1):
      arranged_problems = arranged_problems + " " * 4
  if answer == True:
    arranged_problems = arranged_problems + "\n"
  if (answer == True):
    for i in range(0, list_length):
      dif = int(list_max[i]) - int_anslen(int(list_answer[i]))
      arranged_problems = arranged_problems + " " * dif + str(list_answer[i])
      if (i < list_length - 1):
        arranged_problems = arranged_problems + " " * 4

  return arranged_problems


def int_len(a):
  i = 10
  x = 0
  if a == 0:
    return 1
  while (a > 0):
    a = a // i
    x = x + 1
  return x


def int_anslen(a):
  if (a > 0):
    i = 10
    x = 0
    while (a > 0):
      a = a // i
      x = x + 1
    return x
  elif (a < 0):
    a = a - (2 * a)
    i = 10
    x = 0
    while (a > 0):
      a = a // i
      x = x + 1
    return x + 1
  else:
    return 1

print(arithmetic_arranger(["9780 + 3527", "1887 - 1888", "9989 - 1","9 + 7753","7452 + 38"],True))
