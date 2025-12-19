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
<img width="2528" height="1242" alt="image" src="https://github.com/user-attachments/assets/f5b1a4e0-59c8-4405-9411-a058a6a10a52" />

---

## 🔍 Résultats CodeQL


<img width="2558" height="1113" alt="image" src="https://github.com/user-attachments/assets/77c42b4c-44aa-4cf6-a2f3-be1278d8604a" />

---

## ✅ Pipeline après correction

<img width="2548" height="1197" alt="image" src="https://github.com/user-attachments/assets/198ab727-1415-404f-ab94-be95597e7a34" />








