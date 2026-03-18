# 🎬 Global Video Reliability Platform — SRE Monitoring Project

## 📌 Project Overview

This project demonstrates how a distributed video processing system can be monitored and validated using modern Site Reliability Engineering (SRE) practices.

The goal was to simulate a real production-like workflow where video processing jobs are submitted, queued, processed by background workers, and continuously monitored for performance and reliability issues.

This project focuses not only on building services but also on **observing system behavior under load and detecting failure conditions early.**

---

## 🏗️ System Architecture

The platform consists of the following components:

- **Upload Service** — Receives incoming job requests
- **Worker Service** — Processes queued jobs asynchronously
- **Redis** — Acts as the job queue backend
- **Prometheus** — Collects and stores system metrics
- **Grafana** — Provides visualization dashboards and alerting
- **Load Generator** — Simulates traffic spikes and stress conditions

This architecture represents a simplified version of background processing pipelines used in large-scale video platforms.

---

## ⚙️ How to Run the Project

### Step 1 — Start All Services

From the project root directory:

```bash
docker compose up --build
```
📸 Screenshot:

![Docker Services Running](screenshots/01-docker-services-running.png)

---

### Step 2 — Verify Containers Are Running

Open a **new terminal window** and run:

```bash
docker compose ps
```
---

### Step 3 — Verify Prometheus Targets

Open Prometheus in your browser:

http://localhost:9090

From the top menu go to:

Status → Targets

Verify that both services are in **UP** state:

- upload-service
- worker-service

This confirms Prometheus is successfully scraping metrics.

📸 Screenshot:

![Prometheus Targets](screenshots/02-prometheus-targets-up.png)

---

### Step 4 — Verify Worker Metrics in Prometheus

In Prometheus UI go to:

Graph → Enter Query:

jobs_processed_total

Click **Execute**.

You should see metric values plotted.  
This confirms worker metrics are being collected.

📸 Screenshot:

![Prometheus Worker Metric](screenshots/03-prometheus-worker-metric.png)

---

### Step 5 — Configure Grafana Data Source

Open Grafana:

http://localhost:3000

Login:

- Username: admin  
- Password: admin  

Navigate to:

Connections → Data Sources → Add Data Source → Prometheus

Set URL:

http://prometheus:9090

Click **Save & Test**.  
You should see **Data source is working**.

📸 Screenshot:

![Grafana Datasource](screenshots/04-grafana-datasource.png)

---

### Step 6 — Create Monitoring Dashboard

Create a new dashboard and add two panels:

Panel 1 Query:

jobs_processed_total

Panel 2 Query:

worker_active_jobs

Set visualization to **Time Series**.

Arrange both panels in the same dashboard.

📸 Screenshot:

![Grafana Dashboard](screenshots/05-grafana-dashboard.png)

---

### Step 7 — Validate Alert Firing

Create alert rule on metric:

worker_active_jobs == 0

Evaluation time: 1 minute

When worker stops processing jobs → alert should move to **FIRING** state.

📸 Screenshot:

![Alert Firing](screenshots/06-alert-firing.png)

---
