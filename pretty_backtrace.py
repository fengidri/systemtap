# -*- coding:utf-8 -*-
#    author    :   丁雪峰
#    time      :   2015-11-30 23:04:06
#    email     :   fengidri@yeah.net
#    version   :   1.0.1

import sys
import re
import os
process = sys.argv[2]
def handle(line):
    regex = "(0x[0-9a-z]+) : ([^\[]+)\+.+? \[(.+)\]"
    match = re.search(regex, line)
    if not match:
        print ""
        return

    fun = os.popen("c++filt %s" % match.group(2)).read()
    fun = fun.strip()
    pos = os.popen("addr2line -e %s %s"  % (process, match.group(1))).read()
    pos = pos.strip()

    fun = "\033[31m%s" % fun.replace('(', '\033[0m(')
    print fun, pos


for line in open(sys.argv[1]).readlines():
    handle(line)



if __name__ == "__main__":
    pass


