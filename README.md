# align-arguments
Sublime Text 3 Plugin to automatically format and align argument lists on the opening bracket

Many [style guides][1] require that argument lists are formatted in the following way:

    ReturnType ClassName::ReallyLongFunctionName(Type par_name1, Type par_name2,
                                                 Type par_name3) {
      DoSomething();
      ...
    }

With the argument list lining up with the opening parenthesis. This can be tedious to format when renaming functions with a long list of arguments, which is why this plugin exists. It provides two commands. Place the cursor inside an argument list like this one

    ReturnType ClassName::ReallyLongFunctionName(Type par_name1, Type par_name2, Type par_name3) {

"Format Argument" will reformat the list of arguments and wrap the line if it exceeds the maximum line length (80 by default). The output will be matching the requirement above.

Alternatively you can run wrap lines yourself and let it just do the indentation with the "Align Arguments" command on a snippet like this:

    ReturnType ClassName::ReallyLongFunctionName(Type par_name1,
        Type par_name2,
        Type par_name3) {

Which will turn into:

    ReturnType ClassName::ReallyLongFunctionName(Type par_name1,
                                                 Type par_name2,
                                                 Type par_name3) {

Configuration:

    "align_arguments": {
      "line_length": 120,
      "one_per_line": true,
    }

  line_length: Maximum line length. Defaults to the first ruler on the current file, but can be overwritten with this parameter. 
  one_per_line: When the argument list becomes too long for a single line, put each argument on a separate line. Default: false.

[1]: https://google.github.io/styleguide/cppguide.html#Function_Declarations_and_Definitions
