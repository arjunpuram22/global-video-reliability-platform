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
