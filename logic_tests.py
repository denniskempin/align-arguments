import unittest
from logic import smart_split, indent_arguments, format_arguments


indent_cases = [
  ('Simple example', '    ',
"""\
int param_a,
int param_b,
         int param_c\
""", """\
int param_a,
    int param_b,
    int param_c\
"""),

    ('Inner brackets', '    ',
"""\
param_a,
function_call(param_b, param_c)\
""", """\
param_a,
    function_call(param_b, param_c)\
"""),
]


format_cases = [
  ('Simple example', '    ', 30, False,
"""\
int param_a, int param_b, int param_c\
""", """\
int param_a, int param_b,
    int param_c\
"""),

  ('One-per-line example', '    ', 30, True,
"""\
int param_a, int param_b, int param_c\
""", """\
int param_a,
    int param_b,
    int param_c\
"""),
]


class TestArgumentsFormatting(unittest.TestCase):
  def test_bracket_aware_split(self):
    def test(string, expected):
      self.assertEqual(smart_split(',', string), expected)
    test('abcd', ['abcd'])
    test('a,b,c,d', ['a', 'b', 'c', 'd'])
    test(',a,b,c,d,', ['', 'a', 'b', 'c', 'd', ''])
    test('a,(b,c),d', ['a', '(b,c)', 'd'])
    test('(a,b,c,d)', ['(a,b,c,d)'])
    test('(a,(b,c),d)', ['(a,(b,c),d)'])
    test('(a,b,c,d', ['(a,b,c,d'])

  def test_indent_arguments(self):
    for title, indent, arguments, expected in indent_cases:
      print('Indent arguments case: %s' % title)
      self.assertEqual(indent_arguments(arguments, indent), expected)

  def test_format_arguments(self):
    for title, indent, ll, opl, arguments, expected in format_cases:
      print('Format arguments case: %s' % title)
      self.assertEqual(format_arguments(arguments, indent, ll, opl), expected)


if __name__ == '__main__':
  unittest.main()