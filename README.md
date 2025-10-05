# SARWatch

<p align="center">
  <img src="SARWatch frontend.jpg" width="600" alt="SAR Satellite Example">
</p>

**SARWatch** is an SaaS initiative and prototype platform, ^[oficial site](https://sarwatch.earth), that leverages **Synthetic Aperture Radar (SAR)** satellite imagery for **real-time monitoring and analysis of natural disasters**.  
The project aims to enable resilient, weather-independent Earth observation by integrating open and commercial SAR data through a modern, cloud-based architecture.

---

## Overview

Conventional optical satellites are powerful tools for observing Earth's surface but fail under adverse weather conditions such as clouds, smoke, or volcanic ash.  
SAR satellites, however, can operate **day and night**, **penetrate atmospheric layers**, and **detect ground changes at centimeter-level precision**.  

**SARWatch** uses this capability to provide an intelligent monitoring system for:
- Floods, fires, and volcanic eruptions  
- Ground deformation and subsidence  
- Infrastructure damage  
- Climate and environmental tracking  

---

## Contents
--------

| Section | Description |
| -------- | ------------ |
| [1. Problem Statement](#1-problem-statement) | Challenges with optical satellites during disasters |
| [2. Proposed Solution](#2-proposed-solution) | SAR-based approach for real-time monitoring |
| [3. Current Limitations](#3-current-limitations) | Data frequency and availability issues |
| [4. Technological Context](#4-technological-context) | Market and LEO ecosystem evolution |
| [5. Applications](#5-applications) | Real-world use cases |
| [6. Platform Architecture](#6-platform-architecture) | Cloud design and data flow |
| [7. Functional Modules](#7-functional-modules) | UI and user roles |
| [8. Data Sources](#8-data-sources) | Integration with open and commercial providers |
| [9. Non-Functional Requirements](#9-non-functional-requirements) | Scalability, security, reliability |
| [10. Future Enhancements](#10-future-enhancements) | Planned improvements |

---

## 1. Problem Statement

During extreme weather events (storms, hurricanes, fires, eruptions), optical satellites cannot capture usable imagery due to clouds, smoke, or dust.  
This makes **real-time monitoring** and **rapid emergency response** extremely difficult.

---

## 2. Proposed Solution

**SARWatch** proposes the creation of a web-based platform to collect, process, and visualize **SAR satellite data** for near real-time disaster monitoring.

### Key Advantages of SAR
- **Weather independence:** Operates day and night, unaffected by sunlight or clouds.  
- **Atmospheric penetration:** Microwaves pass through dust, rain, or volcanic ash.  
- **Ground displacement detection:** Measures deformations at centimeter scale.

---

## 3. Current Limitations

While SAR offers huge advantages, most commercial satellites still have **multi-day revisit times**.  
However, emerging constellations like **Capella Space**, **ICEYE**, and **Umbra** are reducing this to **less than one hour**, unlocking operational use cases.

---

## 4. Technological Context

The space industry is growing rapidly — **over 70,000 LEO satellites** are expected to launch within five years.  
These satellites will orbit between **160–1,900 km**, completing one revolution every 90 minutes.

According to **Goldman Sachs Research**, the satellite market could grow from **$15B to $108B by 2035**, with potential to reach **$457B** in optimistic scenarios.

### Cost & Ecosystem
- Launch cost: up to **$12,000/kg**, expected to fall to **$100–200/kg** with reusable rockets.  
- LEO systems will complement terrestrial networks, enabling hybrid global connectivity.

---

## 5. Applications

| Domain | Use Case |
| ------- | -------- |
| **Emergency Management** | Floods, fires, and volcanic eruption monitoring |
| **Infrastructure Monitoring** | Detect land movement near dams, roads, or buildings |
| **Agriculture & Water** | Soil moisture estimation, flood zone detection |
| **Environmental Studies** | Track deforestation, erosion, and glacial retreat |

<video width="600" controls>
  <source src="InfrastructuresDamage.mp4" type="video/mp4">
  Tu navegador no soporta el video.
</video>
---

## 6. Platform Architecture

### Cloud Infrastructure (AWS)

| Layer | Services |
|-------|-----------|
| Data Ingestion & Storage | AWS Lambda / Glue, S3, RDS / DynamoDB |
| Processing & AI Analysis | AWS SageMaker, EC2 / Fargate |
| APIs & Frontend | API Gateway + Lambda, CloudFront + S3 |
| Authentication | AWS Cognito |
| Payments | Stripe / AWS Marketplace |

### System Overview
- Interactive map viewer  
- Satellite imagery database  
- Role-based access control  
- AI-powered alerts  
- Premium report and download system  

---

## 7. Functional Modules

### 7.1. Home Interface
- Interactive world map with zoom and search  
- Login/Sign-up options  
- Alerts and notifications panel  

### 7.2. User Roles

| Role | Permissions |
|------|--------------|
| **Public Users** | Browse free old maps|
| **Subscription Users** | Monitoring tools and acces to reports|
| **Authorities / Governments** | Access premium SAR data, generate reports, receive AI alerts |

### 7.3. Map & Reports
- Sidebar shows available SAR maps by region  
- Options to download, purchase, or request data  
- Smart Reports combine SAR data with socioeconomic layers  

---

## 8. Data Sources

- **NASA Earthdata** (Sentinel, Landsat, RADARSAT)  
- **ESA Copernicus**  
- **OpenStreetMap** and national GIS databases  
- Government infrastructure and census data  

---

## 9. Non-Functional Requirements

| Requirement | Description |
|--------------|-------------|
| Scalability | Auto-scaling backend (ECS/Fargate) |
| Security | Cognito + IAM roles |
| Data Privacy | GDPR-compliant |
| Performance | Map load < 3s, API < 500ms (Expected) |
| Localization | Multi-language support (Phase 2) |

---

## 10. Future Enhancements

- Mobile app for citizen reporting and offline access  
- Crowdsourced validation of detected changes  
- Multi-level alert severity (Minor, Moderate, Critical)  
- Integration with official emergency systems  
- Full multilingual support  

---

## Acknowledgments

Claude --> used for web page creation
Ai.invideo.io --> Video generation
GoogleCloud Text to speach --> Audio generation
ChatGPT --> consulting tool



