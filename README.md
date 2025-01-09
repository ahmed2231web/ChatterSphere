# 🌐 ChatterSphere

<div align="center">

![ChatterSphere Logo](https://img.shields.io/badge/ChatterSphere-Connect%20Instantly-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMzIgNTZDNDUuMjU0OCA1NiA1NiA0NS4yNTQ4IDU2IDMyQzU2IDE4Ljc0NTIgNDUuMjU0OCA4IDMyIDhDMTguNzQ1MiA4IDggMTguNzQ1MiA4IDMyQzggMzcuNzA3MiAxMC4wMjk2IDQyLjk3NDQgMTMuNDM0NCA0N0w4LjUxOTkyIDU1LjQ4QzEwLjY2NzIgNTUuODIwOCAxMi44OTYgNTYgMzIgNTZaIiBmaWxsPSIjZmZmIi8+PC9zdmc+)

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-brightgreen.svg)](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

*A modern, real-time chat application built with Django and WebSockets* 🚀

[Live Demo](#) · [Report Bug](#) · [Request Feature](#)

</div>

---

## ✨ Features

- 🔐 **Secure Authentication**
  - User registration and login
  - Password protection
  - Session management

- 💬 **Real-Time Chat**
  - Instant message delivery
  - Multiple chat rooms
  - Recent rooms history
  - Room creation and joining

- 🎨 **Modern UI/UX**
  - Responsive design
  - Clean interface
  - Intuitive navigation
  - Beautiful animations

- 🛠️ **Technical Features**
  - WebSocket implementation
  - Asynchronous message handling
  - Efficient data management
  - Scalable architecture

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ChatterSphere.git
cd ChatterSphere
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser! 🎉

## 🌟 Usage

1. **Register/Login**
   - Create a new account or login
   - Secure authentication process
   - Password protection

2. **Create or Join Rooms**
   - Create new chat rooms
   - Join existing rooms
   - Access recent room history

3. **Start Chatting**
   - Real-time message delivery
   - Emoji support
   - File sharing capabilities

## 🛠️ Technology Stack

- **Backend**
  - Django 4.2
  - Channels (WebSocket)
  - SQLite/PostgreSQL
  - Redis (for WebSocket backend)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5

- **Real-Time Communication**
  - WebSocket Protocol
  - Asynchronous Gateway Interface (ASGI)
  - Channel Layers

### Login Page
[Login Screenshot]

### Chat Room
[Chat Room Screenshot]

### Create/Join Room
[Room Creation Screenshot]

</details>
</div>

## 🔧 Configuration

Key configuration options in `settings.py`:

```python
# WebSocket Configuration
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📬 Contact

Your Name - Ahmed

Project Link: [https://github.com/ahmed2231web/ChatterSphere](https://github.com/ahmed2231web/ChatterSphere)

---

<div align="center">

### ⭐ Star this repo if you like it!

Made with ❤️ by Ahmed

</div>
