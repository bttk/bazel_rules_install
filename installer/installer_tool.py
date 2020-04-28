# Copyright 2020 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import shutil
import sys
from typing import List

from rules_python.python.runfiles import runfiles

# shutil.copy2(src, dst)
# https://docs.python.org/3/library/shutil.html#shutil.copy2

def main():
    r: runfiles.Runfiles = runfiles.Create()
    rpaths: List[str] = sys.argv[1:]
    if len(rpaths) == 0:
        print("Specify runfiles in arguments", file=sys.stderr)
        sys.exit(-1)

    for rpath in rpaths:
        rloc: str = r.Rlocation(rpath)
        print("{!r} => {!r}".format(rpath, rloc))


if __name__ == '__main__':
    main()
