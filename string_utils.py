def split_before_each_uppercases(formula):
    start = 0
    split_formula = []

    if formula == "":
      return split_formula
      

    
    for end in range(1,len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
        
   

    split_formula.append(formula[start:])

    return split_formula


def split_at_first_digit(formula):
  start = 1
  endlist = []

  for digitornum in formula[1:]:
    if digitornum.isdigit():
      break
    start += 1

  if start == len(formula):
    return formula, 1

  letters = formula[:start]
  nums = int(formula[start:])

  return letters, nums
