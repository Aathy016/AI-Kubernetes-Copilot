import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.prometheus_tool import PrometheusTool


prom = PrometheusTool()

print("\n===== UP TARGETS =====\n")

print(prom.get_up_targets())

print("\n===== CPU USAGE =====\n")

print(prom.get_node_cpu())

print("\n===== MEMORY USAGE =====\n")

print(prom.get_node_memory())