# Live Poll Voting System

## 📌 Description
A real-time client–server based voting system developed as part of a Computer Networks project. The system allows multiple clients to connect and vote simultaneously, with efficient handling of concurrent requests using UDP socket communication.

---

## 🚀 Features
- Supports multiple clients voting at the same time  
- Real-time vote collection and result processing  
- Client–server communication using UDP sockets  
- Detection of duplicate votes  
- Basic login authentication system  
- Network statistics tracking (packets, duplicates, loss %)  

---

## 🛠 Tech Stack
- Python (UDP Socket Programming)  
- Node.js (Express.js API)  
- HTML, CSS, JavaScript (Frontend)  
- Computer Networks Concepts  

---

## ⚙️ System Architecture
Client (Browser) → Node.js Server → Python UDP Server

- Frontend sends requests to Node server  
- Node server communicates with Python server via UDP  
- Python server processes votes and sends response  

---

## ▶️ How to Run

### 1. Start Python Server
```bash
python server.py
