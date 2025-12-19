# 🔐 DevSecOps Lab — CI/CD Security Pipeline

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Security](https://img.shields.io/badge/Security-DevSecOps-red)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)

## 📌 Description
Ce projet est un **laboratoire DevSecOps** qui démontre l’intégration automatique de la sécurité dans un pipeline **CI/CD GitHub Actions** pour une API **Python Flask** conteneurisée avec Docker.

La sécurité est testée **à chaque push** grâce à des outils automatisés.

---

## 🧱 Architecture du projet
```bash
devsecops-lab/
├── api/
│   └── app.py
├── Dockerfile
└── .github/
    └── workflows/
        └── devsecops.yml

<img width="1963" height="1127" alt="image" src="https://github.com/user-attachments/assets/933f0105-abbc-407b-a0bf-65445d19fbe8" />


---


🛠️ Technologies utilisées

- GitHub Actions (CI/CD)

- Python + Flask

- Docker

- CodeQL (SAST)

- Bandit (Sécurité Python)

- Trivy (Scan image Docker)

---

## ▶️ Pipeline GitHub Actions





