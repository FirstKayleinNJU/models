# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import functools

import absl.app
from absl import flags

help_wrap = functools.partial(flags.text_wrap, length=80, indent="  ",
                              firstline_indent="\n")

class HelpOneLetter(absl.app.HelpFlag):
  """-h is an alias for --help."""
  NAME = 'h'
  SHORT_NAME = None

flags.DEFINE_flag(HelpOneLetter())

def to_choices_str(choices):
  return "(choices: {})".format(", ".join([str(i) for i in choices]))
