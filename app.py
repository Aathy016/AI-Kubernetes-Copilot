import streamlit as st
from ai_agent.event_analyzer import EventAnalyzer
from ai_agent.remediation_engine import RemediationEngine
from storage.timeline_manager import TimelineManager
from tools.grafana_tool import GrafanaTool
from ai_agent.cluster_analyzer import ClusterAnalyzer
from ai_agent.llm_recommendation_engine import (
    LLMRecommendationEngine
)
from ai_agent.copilot_chat import CopilotChat
from ai_agent.rca_engine import RCAEngine
from ai_agent.incident_detector import IncidentDetector

from reports.rca_report_generator import (
    PDFReportGenerator
)

from tools.cluster_manager import ClusterManager

from storage.incident_storage import (
    IncidentStorage
)

st.set_page_config(
    page_title="AI Kubernetes Copilot",
    layout="wide"
)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:

    st.title("AI Kubernetes Copilot")

    st.markdown("""
    - Dashboard
    - Incidents
    - Event Analysis
    - RCA
    - Remediation
    - Timeline
    - Grafana
    - Copilot
    """)

st.title("🤖 AI Kubernetes Copilot")

try:

    manager = ClusterManager()

    contexts = manager.get_contexts()

    # ---------------------------------------------------------
    # Multi-Cluster Support (Phase 19)
    # ---------------------------------------------------------
    selected_clusters = st.multiselect(
        "Select Clusters",
        contexts["contexts"],
        default=[contexts["active"]]
    )

    if not selected_clusters:

        st.warning(
            "Please select at least one cluster."
        )

        st.stop()

    # Primary cluster drives the main dashboard below
    selected_cluster = selected_clusters[0]

    manager.switch_context(
        selected_cluster
    )

    st.success(
        f"Connected to: {selected_cluster}"
    )

except Exception as e:

    st.error(
        f"Cluster Connection Failed:\n{e}"
    )

    st.stop()

if st.button(
    "🔄 Refresh Cluster Data"
):
    st.rerun()

try:

    analyzer = ClusterAnalyzer()

    report = analyzer.analyze()
    detector = IncidentDetector()

    active_incidents = detector.detect(
    report
)

except Exception as e:

    st.error(
        f"Cluster Analysis Failed:\n{e}"
    )

    st.stop()

try:

    engine = LLMRecommendationEngine()

    llm_report = {

        "cpu": report["cpu"],

        "memory": report["memory"],

        "health_score": report["health_score"],

        "running": report["running"],

        "pending": report["pending"],

        "failed": report["failed"]

    }


    ai_response = engine.generate(
        llm_report
    )


    if isinstance(ai_response, dict):

        analysis = ai_response.get(
            "response",
            "No AI response generated."
        )

    else:

        analysis = ai_response


except Exception as e:

    analysis = (
        f"AI Analysis Failed:\n{e}"
    )

# ---------------------------------------------------------
# Cluster Risk Level
# ---------------------------------------------------------
risk_level = "LOW"

if report["health_score"] < 60:
    risk_level = "HIGH"

elif report["health_score"] < 80:
    risk_level = "MEDIUM"

st.subheader(
    "📊 Cluster Health Dashboard"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "CPU Usage",
        f"{report['cpu']:.2f}%"
    )

with col2:

    st.metric(
        "Memory Usage",
        f"{report['memory']:.2f}%"
    )

with col3:

    st.metric(
        "Health Score",
        f"{report['health_score']}/100"
    )

with col4:

    st.metric(
        "Incidents",
        len(active_incidents)
    )

st.metric(
    "Risk Level",
    risk_level
)

st.subheader(
    "☸️ Cluster Status"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.success(
        f"Running Pods: {report['running']}"
    )

with col2:

    st.warning(
        f"Pending Pods: {report['pending']}"
    )

with col3:

    st.error(
        f"Failed Pods: {report['failed']}"
    )

# ---------------------------------------------------------
# Multi-Cluster Overview (Phase 19)
# ---------------------------------------------------------
if len(selected_clusters) > 1:

    st.subheader(
        "🌐 Multi-Cluster Overview"
    )

    for cluster in selected_clusters:

        try:

            manager.switch_context(cluster)

            cluster_analyzer = ClusterAnalyzer()

            cluster_report = cluster_analyzer.analyze()

            st.subheader(
                f"Cluster: {cluster}"
            )

            st.json(cluster_report)

        except Exception as e:

            st.error(
                f"Failed to analyze cluster {cluster}:\n{e}"
            )

    # Restore primary cluster context for the rest of the app
    manager.switch_context(selected_cluster)

st.subheader(
    "🚨 Active Incidents"
)

if active_incidents:

    for incident in active_incidents:

        severity = incident.get(
            "severity",
            "INFO"
        )

        issue = incident.get(
            "issue",
            "Unknown Issue"
        )

        if severity == "CRITICAL":

            st.error(
                f"[{severity}] {issue}"
            )

        elif severity == "HIGH":

            st.error(
                f"[{severity}] {issue}"
            )

        elif severity == "MEDIUM":

            st.warning(
                f"[{severity}] {issue}"
            )

        else:

            st.info(
                f"[{severity}] {issue}"
            )

else:

    st.success(
        "No Active Incidents Detected"
    )
st.subheader(
    "📋 Kubernetes Event Analysis"
)

try:

    analyzer = EventAnalyzer()

    event_results = analyzer.analyze()

    if event_results:

        for event in event_results:

            severity = event.get(
                "severity",
                "INFO"
            )

            message = (
                f"{event.get('issue', 'Unknown Issue')} "
                f"| Resource: {event.get('resource', 'Unknown Resource')}"
            )

            if severity in ["CRITICAL", "HIGH"]:

                st.error(
                    f"[{severity}] {message}"
                )

            elif severity == "MEDIUM":

                st.warning(
                    f"[{severity}] {message}"
                )

            else:

                st.info(
                    f"[{severity}] {message}"
                )

    else:

        st.success(
            "No critical Kubernetes events detected."
        )

except Exception as e:

    st.error(
        f"Event Analyzer Failed:\n{e}"
    )
st.subheader(
    "🧠 AI Cluster Analysis"
)

st.info(
    analysis
)

# ---------------------------------------------------------
# AI Recommendations
# ---------------------------------------------------------
st.subheader(
    "💡 AI Recommendations"
)

if report["pending"] > 0:

    st.warning(
        "Investigate pending pods."
    )

if report["failed"] > 0:

    st.error(
        "Investigate failed workloads."
    )

if report["cpu"] > 80:

    st.warning(
        "High CPU utilization detected."
    )

if report["memory"] > 80:

    st.warning(
        "High memory utilization detected."
    )

st.subheader(
    "🚨 AI Root Cause Analysis"
)

rca_result = None

if st.button(
    "Generate AI RCA"
):

    try:

        with st.spinner(
            "Analyzing cluster issues..."
        ):

            rca_engine = RCAEngine()

            rca_result = rca_engine.analyze(
                report
            )

            storage = IncidentStorage()

            incident_id = storage.save_incident(
                report,
                rca_result
            )
            timeline = TimelineManager()

            timeline.create_event(
    "AI RCA",
    "Root Cause Analysis Generated"
)
            st.markdown(
                "### 🔍 RCA Result"
            )

            st.write(
                rca_result
            )

            st.download_button(
                "Download RCA",
                rca_result,
                file_name="rca_report.txt"
            )

            st.success(
                f"Incident Saved Successfully | ID: {incident_id}"
            )

    except Exception as e:

        st.error(
            f"RCA Failed:\n{e}"
        )
st.subheader(
    "🛠️ AI Remediation Engine"
)

if st.button(
    "Generate Remediation Plan"
):

    try:

        remediation = RemediationEngine()

        fixes = remediation.generate(
            report
        )

        st.markdown(
            "### Suggested Fixes"
        )

        st.write(
            fixes
        )

    except Exception as e:

        st.error(
            f"Remediation Failed:\n{e}"
        )
st.subheader(
    "📄 RCA Report Generator"
)

if st.button(
    "Generate PDF Report"
):

    try:

        pdf = PDFReportGenerator()

        output_file = (
            "reports/AI_RCA_Report.pdf"
        )

        pdf.generate(
            report,
            analysis,
            output_file
        )

        st.success(
            "PDF Report Generated Successfully"
        )

        st.code(
            output_file
        )

    except Exception as e:

        st.error(
            f"PDF Generation Failed:\n{e}"
        )

st.subheader(
    "📚 Incident History"
)

try:

    storage = IncidentStorage()

    incidents = storage.get_all_incidents()

    if (
        "documents" in incidents
        and incidents["documents"]
    ):

        docs = list(
            reversed(
                incidents["documents"]
            )
        )

        for i, doc in enumerate(
            docs,
            start=1
        ):

            with st.expander(
                f"Incident #{i}"
            ):

                st.code(
                    doc
                )

    else:

        st.info(
            "No incidents found."
        )

except Exception as e:

    st.error(
        f"Unable to load incident history:\n{e}"
    )

st.markdown("---")
st.subheader(
    "📅 Incident Timeline"
)

try:

    timeline = TimelineManager()

    events = timeline.get_events()

    if events:

        for event in reversed(events):

            st.info(
                f"{event['timestamp']} | "
                f"{event['title']} | "
                f"{event['description']}"
            )

    else:

        st.info(
            "No timeline events found."
        )

except Exception as e:

    st.error(
        f"Timeline Error:\n{e}"
    )

# ---------------------------------------------------------
# Grafana Monitoring
# ---------------------------------------------------------
st.subheader(
    "📈 Grafana Monitoring"
)

try:

    grafana = GrafanaTool()

    health = grafana.health()

    st.success(
        f"Grafana Connected | Version: {health['version']}"
    )

    dashboards = grafana.get_dashboards()

    if dashboards:

        for dashboard in dashboards:

            st.info(
                dashboard.get(
                    "title",
                    "Unknown Dashboard"
                )
            )

    else:

        st.warning(
            "No Grafana Dashboards Found"
        )

except Exception as e:

    st.error(
        f"Grafana Error:\n{e}"
    )

st.subheader(
    "💬 Kubernetes AI Copilot"
)

st.markdown(
    """
### Example Questions

- Why is pod broken-app pending?
- Explain ImagePullBackOff
- Explain ErrImagePull
- What are the current cluster risks?
- How healthy is my cluster?
- Give recommendations to improve health score.
"""
)

question = st.text_input(
    "Ask Kubernetes Copilot",
    placeholder="Why is pod broken-app pending?"
)

if st.button(
    "Ask Copilot"
):

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner(
                "Analyzing Cluster..."
            ):

                copilot = CopilotChat()

                answer = copilot.ask(
                    question=question,
                    report=report
                )

                st.markdown(
                    "### 🤖 Copilot Response"
                )

                st.write(
                    answer
                )

        except Exception as e:

            st.error(
                f"Copilot Error:\n{e}"
            )

with st.expander(
    "🔍 View Raw Cluster Report"
):

    st.json(
        report
    )

# ---------------------------------------------------------
# Project Statistics
# ---------------------------------------------------------
st.subheader(
    "📈 Project Statistics"
)

st.json({
    "Cluster Health": report["health_score"],
    "Running Pods": report["running"],
    "Pending Pods": report["pending"],
    "Failed Pods": report["failed"],
    "Incidents": len(active_incidents)
})

st.markdown("---")

st.caption(
    "AI Kubernetes Copilot | Kubernetes + Prometheus + ChromaDB + Ollama (Qwen2.5-1.5B)"
)