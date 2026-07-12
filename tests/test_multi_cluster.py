import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tools.cluster_manager import ClusterManager


manager = ClusterManager()


contexts = manager.get_contexts()


print(
    "Available Clusters:"
)


print(
    contexts
)