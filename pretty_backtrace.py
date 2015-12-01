# -*- coding:utf-8 -*-
#    author    :   丁雪峰
#    time      :   2015-11-30 23:04:06
#    email     :   fengidri@yeah.net
#    version   :   1.0.1

import sys
import re
import os
def handle(line, process):
    regex = "(0x[0-9a-z]+) : ([^\[]+)\+.+? \[(.+)\]"
    match = re.search(regex, line)
    if not match:
        print ""
        return

    fun = os.popen("c++filt %s" % match.group(2)).read()
    fun = fun.strip()
    if process:
        pos = os.popen("addr2line -e %s %s"  % (process, match.group(1))).read()
        pos = pos.strip()
    else:
        pos = ''

    fun = "\033[31m%s" % fun.replace('(', '\033[0m(')
    print fun, pos


for line in open(sys.argv[1]).readlines():
    process = None
    if line.startswith("@process:"):
        process = line.split(':')[-1].strip()
        continue

    handle(line, process)



if __name__ == "__main__":
    pass


