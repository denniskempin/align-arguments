
def find_arguments_region(edit, view, location):
  """Returns the start, end index of the selected argument list."""
  end = location
  start = location - 1
  open_brackets = 0
  while start >= 0:
    if view.substr(start) == '(':
      open_brackets -= 1
      if open_brackets < 0:
        start += 1
        break
    if view.substr(start) == ')':
      open_brackets += 1
    start -= 1
  if start < 0:
    return 0, 0

  open_brackets = 0
  while end < view.size():
    if view.substr(end) == ')':
      open_brackets -= 1
      if open_brackets < 0:
        break
    if view.substr(end) == '(':
      open_brackets += 1
    end += 1
  if end >= view.size():
    return 0, 0
  return start, end


def smart_split(search, string):
  """Split string while maintaining blocks encapsulated by brackets."""
  result = []
  open_brackets = 0
  last_split = 0
  for i, char in enumerate(string):
    if char == '(':
      open_brackets += 1
    elif char == ')':
      open_brackets -= 1
    elif open_brackets <= 0 and char == search:
      result.append(string[last_split:i])
      last_split = i + 1
  result.append(string[last_split:])
  return result


def indent_arguments(data, indent):
  lines = smart_split("\n", data)
  result = [lines[0]] + [indent + l.strip() for l in lines[1:]]
  return "\n".join(result)

def format_arguments(data, indent, line_length_limit, one_per_line):
  print(line_length_limit - len(indent))
  arguments = smart_split(',', data)
  lines = []
  accumulator = []
  for i, argument in enumerate(arguments):
    new_line = ', '.join(accumulator + [argument.strip()])
    print(i, ':', argument.strip(), '-', new_line, '-', len(new_line))
    
    if len(new_line) >= line_length_limit - len(indent):
      if one_per_line:
        return format_one_per_line(arguments, indent, line_length_limit)
      if len(accumulator):
        if len(lines):
          lines.append(indent + ', '.join(accumulator) + ',')
        else:
          lines.append(', '.join(accumulator) + ',')
        accumulator = []
    accumulator.append(argument.strip())
  if len(accumulator):
    if len(lines):
      lines.append(indent + ', '.join(accumulator))
    else:
      lines.append(', '.join(accumulator))
  return "\n".join(lines)


def format_one_per_line(arguments, indent, line_length_limit):
  result = [arguments[0]] + [indent + a.strip() for a in arguments[1:]]
  return ",\n".join(result)

