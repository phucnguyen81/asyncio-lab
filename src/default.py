#!/usr/bin/env python
"""List modules of current package."""
import pkgutil
from pathlib import Path

print("Available modules:")
for module in pkgutil.iter_modules([Path(__file__).parent]):
    if not module.ispkg:
        print(module.name)
