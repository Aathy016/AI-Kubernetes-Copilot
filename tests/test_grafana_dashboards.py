import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tools.grafana_tool import GrafanaTool

try:

    grafana = GrafanaTool()

    dashboards = grafana.get_dashboards()

    print("\n===== GRAFANA DASHBOARDS =====")
    print(dashboards)

except Exception as e:

    print("\n===== ERROR =====")
    print(str(e))