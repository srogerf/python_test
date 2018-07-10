#!/usr/bin/env python
import sys

import test_module

print(dir(test_module))
print(sys.platform)
print("---")
print("value is %s " % test_module.test_val)
