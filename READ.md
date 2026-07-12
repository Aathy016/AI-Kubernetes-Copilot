# 🤖 AI Kubernetes Copilot

An AI-powered Kubernetes AIOps Platform built using Kubernetes, Prometheus, Grafana, ChromaDB, Ollama, RAG, and Streamlit.

The platform continuously monitors Kubernetes clusters, detects incidents, performs AI-driven Root Cause Analysis (RCA), generates remediation recommendations, stores incident history, and provides an intelligent Kubernetes Copilot powered by a local Large Language Model.

---

## 🚀 Features

### ☸️ Kubernetes Monitoring
- Multi-cluster Kubernetes support
- Cluster health monitoring
- Pod monitoring
- Deployment monitoring
- Service monitoring
- Namespace monitoring
- Kubernetes event analysis
- Pod log collection

### 📊 Prometheus Monitoring
- CPU utilization monitoring
- Memory utilization monitoring
- Cluster health metrics
- Real-time metric collection

### 📈 Grafana Integration
- Grafana health verification
- Dashboard discovery
- Observability integration

### 🚨 AI Incident Detection
- Automatic incident detection
- Severity classification
- Cluster risk assessment
- Active incident dashboard

### 🧠 AI Root Cause Analysis
- AI-powered RCA generation
- Cluster issue investigation
- Automated root cause reporting

### 🔧 AI Remediation Engine
- Generates remediation plans
- Kubernetes troubleshooting recommendations
- Operational best practices

### 💬 AI Kubernetes Copilot
- Natural language Kubernetes assistant
- Cluster-aware troubleshooting
- Kubernetes knowledge retrieval
- AI-powered recommendations

### 📚 RAG Knowledge Base
- ChromaDB vector database
- Kubernetes knowledge retrieval
- Context-aware AI responses
- Incident knowledge storage

### 🤖 Local LLM Integration
- Ollama integration
- Qwen2.5 / Phi-3 support
- Fully local inference
- No external API dependency

### 🗂 Incident Management
- Incident storage
- Incident history tracking
- Timeline generation
- Historical RCA retrieval

### 📄 Reporting
- AI RCA PDF generation
- Downloadable RCA reports
- Incident documentation

### 🖥 Dashboard
- Streamlit web dashboard
- Cluster health overview
- Incident monitoring
- AI recommendations
- Incident timeline
- Grafana integration

---

## 🏗 Architecture

```text
                   +-------------------+
                   | Kubernetes Cluster |
                   +---------+---------+
                             |
                             v
                   +-------------------+
                   | Kubernetes Tool   |
                   +---------+---------+
                             |
          ---------------------------------------
          |                                     |
          v                                     v

+--------------------+              +--------------------+
| Prometheus Metrics |              | Kubernetes Events  |
+---------+----------+              +----------+---------+
          |                                    |
          v                                    v

+--------------------+              +--------------------+
| Cluster Analyzer   |              | Event Analyzer     |
+---------+----------+              +----------+---------+
          ------------------+------------------
                             |
                             v

                  +---------------------+
                  | Incident Detector   |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | RCA Engine          |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | Remediation Engine  |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | Incident Storage    |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | Timeline Manager    |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | ChromaDB RAG        |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | Ollama LLM          |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | AI Kubernetes       |
                  | Copilot             |
                  +----------+----------+
                             |
                             v

                  +---------------------+
                  | Streamlit Dashboard |
                  +---------------------+
```

---

## 🛠 Technology Stack

### Programming
- Python 3.11

### AI & GenAI
- Ollama
- Qwen2.5 / Phi-3
- ChromaDB
- RAG Architecture

### Kubernetes
- Kubernetes Python Client
- Minikube

### Monitoring
- Prometheus
- Grafana

### Dashboard
- Streamlit

### Reporting
- ReportLab

### Storage
- ChromaDB

---

## 📂 Project Structure

```text
AI-Kubernetes-Copilot
│
├── ai_agent
│   ├── cluster_analyzer.py
│   ├── copilot_chat.py
│   ├── event_analyzer.py
│   ├── incident_detector.py
│   ├── llm_agent.py
│   ├── llm_recommendation_engine.py
│   ├── rca_engine.py
│   └── remediation_engine.py
│
├── tools
│   ├── kubernetes_tool.py
│   ├── prometheus_tool.py
│   ├── grafana_tool.py
│   └── cluster_manager.py
│
├── storage
│   ├── incident_storage.py
│   └── timeline_manager.py
│
├── rag
│   ├── rag_engine.py
│   └── knowledge_loader.py
│
├── reports
│   └── rca_report_generator.py
│
├── tests
│   ├── test_kubernetes_tool.py
│   ├── test_prometheus.py
│   ├── test_cluster_analyzer.py
│   ├── test_grafana.py
│   └── test_copilot.py
│
├── chroma_db
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Kubernetes-Copilot.git

cd AI-Kubernetes-Copilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ☸️ Start Kubernetes

```bash
minikube start
```

Verify:

```bash
kubectl get nodes
```

---

## 📊 Install Prometheus

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install prometheus prometheus-community/prometheus \
-n monitoring \
--create-namespace
```

Port Forward:

```bash
kubectl port-forward svc/prometheus-server 9090:80 -n monitoring
```

---

## 📈 Install Grafana

```bash
helm repo add grafana https://grafana.github.io/helm-charts

helm repo update

helm install grafana grafana/grafana \
-n monitoring
```

Port Forward:

```bash
kubectl port-forward svc/grafana 3000:80 -n monitoring
```

---

## 🤖 Install Ollama

Download:

https://ollama.com/download

Pull Model:

```bash
ollama pull phi3:mini
```

Verify:

```bash
curl http://localhost:11434/api/tags
```

---

## 📚 Load RAG Knowledge Base

```bash
python rag/knowledge_loader.py
```

Verify:

```bash
python tests/test_collections.py
```

Expected:

```text
k8s_incidents
```

---

## 🧪 Run Tests

### Kubernetes

```bash
python tests/test_kubernetes_tool.py
```

### Prometheus

```bash
python tests/test_prometheus.py
```

### Cluster Analyzer

```bash
python tests/test_cluster_analyzer.py
```

### Grafana

```bash
python tests/test_grafana.py
```

### Copilot

```bash
python tests/test_copilot.py
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 💬 Example Copilot Questions

```text
Why is pod broken-app pending?

Explain ImagePullBackOff

Explain CrashLoopBackOff

How healthy is my cluster?

What are the current risks?

Give recommendations to improve health score.
```

---

## 📌 Completed Phases

✅ Phase 1 – Kubernetes Integration

✅ Phase 2 – Prometheus Integration

✅ Phase 3 – Grafana Integration

✅ Phase 4 – Cluster Health Analyzer

✅ Phase 5 – AI Recommendation Engine

✅ Phase 6 – ChromaDB Integration

✅ Phase 7 – RAG Knowledge Base

✅ Phase 8 – Ollama Integration

✅ Phase 9 – Kubernetes Copilot

✅ Phase 10 – RCA Engine

✅ Phase 11 – Incident Detection

✅ Phase 12 – Incident Storage

✅ Phase 13 – PDF RCA Reports

✅ Phase 14 – Event Analysis

✅ Phase 15 – Remediation Engine

✅ Phase 16 – Incident Timeline

✅ Phase 17 – Grafana Dashboard Integration

✅ Phase 18 – Enhanced Dashboard

✅ Phase 19 – Multi-Cluster Support

✅ Phase 20 – Full AIOps Dashboard

---

## 🎯 Resume Project Title

**AI-Powered Kubernetes AIOps Platform with RAG, RCA, Incident Detection, Remediation Recommendations, Multi-Cluster Monitoring, and Local LLM Integration**

---

## 👨‍💻 Author

**Aathyuktha Selvam**

B.Tech Artificial Intelligence & Data Science

Automation Developer | Kubernetes | DevOps | GenAI | RAG | AIOps | Cloud Automation