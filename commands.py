import sublime, sublime_plugin
from .logic import indent_arguments, find_arguments_region, format_arguments


class _AbstractBaseCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      start, end = find_arguments_region(edit, self.view, region.b)
      region = sublime.Region(start, end)
      data = self.view.substr(region)
      indent = " " * self.view.rowcol(start)[1]
      updated = self.process(data, indent)
      self.view.replace(edit, region, updated)

class IndentArgumentsCommand(_AbstractBaseCommand):
  def process(self, data, indent):
    return indent_arguments(data, indent)

class FormatArgumentsCommand(_AbstractBaseCommand):
  def process(self, data, indent):
    settings = self.view.settings()
    rulers = settings.get("rulers")

    aa_settings = settings.get("align_arguments", {})
    line_length = aa_settings.get("line_length",
                                  rulers[0] if rulers else 80)
    opl = aa_settings.get("one_per_line", False)
    return format_arguments(data, indent, line_length, opl)