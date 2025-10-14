# Full-Stack Contact Management System


[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18.x-61DAFB.svg?logo=react)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-05998b.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)](https://www.docker.com/)

A robust and efficient full-stack application for managing personal and professional contacts. This project features a modern, responsive frontend built with **React** and a high-performance RESTful API backend powered by **Python's FastAPI**.

The entire application is containerized with **Docker**, ensuring a seamless and consistent development and deployment experience across any environment.

---

## ✨ Key Features

-   **Full CRUD Functionality**: Create, read, update, and delete contacts with ease through an intuitive user interface.
-   **Responsive Frontend**: A clean and modern UI built with React that provides a seamless experience on desktop and mobile devices.
-   **High-Performance Backend**: A lightning-fast and scalable API built with FastAPI, featuring asynchronous request handling.
-   **Robust Database**: Utilizes a powerful database (e.g., SQLite/PostgreSQL) with data models managed by SQLAlchemy ORM for reliability and consistency.
-   **Containerized with Docker**: The entire stack (frontend, backend) is containerized using Docker and managed with Docker Compose for easy setup and deployment.
-   **Interactive API Docs**: Automatically generated, interactive API documentation (via Swagger UI & ReDoc) for easy testing and exploration of endpoints.

---

## 🛠️ Tech Stack & Architecture

| Category        | Technology                                                                |
| :-------------- | :------------------------------------------------------------------------ |
| **Frontend** | `React.js`, `CSS3`                                                        |
| **Backend** | `Python`, `FastAPI`, `Uvicorn`                                            |
| **Database** | `SQLite 3` / `PostgreSQL`, `SQLAlchemy (ORM)`                             |
| **DevOps/Tools**| `Docker`, `Docker Compose`, `Git`                                         |

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

-   [Git](https://git-scm.com/)
-   [Docker](https://www.docker.com/products/docker-desktop) & [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Setup

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/Ayush-Shrivas/Contact-Management-System.git](https://github.com/Ayush-Shrivas/Contact-Management-System.git)
    cd Contact-Management-System
    ```

2.  **Build and Run with Docker Compose**
    From the root directory of the project, run the following command. This will build the images and start the containers.
    ```sh
    docker-compose up --build
    ```

3.  **Access the Application**
    Once the containers are running, the application will be available at:
    -   🌐 **Frontend (React App)**: [http://localhost:3000](http://localhost:3000)
    -   📚 **Backend API Docs (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📝 API Endpoints

The backend provides a RESTful API to manage contacts. You can test these endpoints directly from the [auto-generated documentation](http://localhost:8000/docs).

| HTTP Method | Endpoint                 | Description                         |
| :---------- | :----------------------- | :---------------------------------- |
| `GET`       | `/api/contacts`          | Fetches a list of all contacts.     |
| `POST`      | `/api/contacts`          | Creates a new contact.              |
| `GET`       | `/api/contacts/{contact_id}` | Retrieves a single contact by its ID. |
| `PUT`       | `/api/contacts/{contact_id}` | Updates an existing contact's details. |
| `DELETE`    | `/api/contacts/{contact_id}` | Deletes a specified contact.        |

---
contact-management-system/
├── backend/                # FastAPI application
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/               # React application
│   ├── public/
│   ├── src/
│   └── Dockerfile
├── .gitignore
├── docker-compose.yml      # Docker orchestration file
└── README.md
---

## 👤 Author

**Ayush Shrivas**

-   **GitHub**: [@Ayush-Shrivas](https://github.com/Ayush-Shrivas)
-   **LinkedIn**: [Ayush Shrivas](https://www.linkedin.com/in/ayush-shrivas-190475299/)

---


---

## 📂 Project Structure
