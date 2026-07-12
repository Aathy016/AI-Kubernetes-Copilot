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

from ai_agent.cluster_analyzer import ClusterAnalyzer
from ai_agent.recommendation_engine import RecommendationEngine
from reports.rca_report_generator import PDFReportGenerator


analyzer = ClusterAnalyzer()

report = analyzer.analyze()

engine = RecommendationEngine()

recommendations = engine.generate(report)

pdf = PDFReportGenerator()

pdf.generate(
    report,
    recommendations
)