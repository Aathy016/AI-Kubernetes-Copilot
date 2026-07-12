import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from tools.grafana_tool import GrafanaTool

grafana = GrafanaTool()

print("\n===== HEALTH =====")
print(grafana.health())

print("\n===== DASHBOARDS =====")
print(grafana.get_dashboards())