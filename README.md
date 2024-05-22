PhotoFrame - Django and React Project

PhotoFrame is a web application for managing and selling photo frames. It includes a Django backend for managing the data and a React frontend for the user interface.

Features
Admin Panel: Manage photo frames, including adding new frames, updating prices, and enabling top sales.
User Interface: View a list of available photo frames, explore details, and make purchases.
Responsive Design: The frontend is responsive, supporting various devices and screen sizes.
REST API: Backend API built with Django Rest Framework for data management.
Tech Stack
Frontend: React, Axios
Backend: Django, Django Rest Framework
Database: SQLite (for local development)
Styling: CSS, Bootstrap (React-Bootstrap for frontend)
Other Tools: Axios for HTTP requests, React Router for navigation
Installation
Backend (Django)
•	Clone the repository:
git clone <repo-url>
cd photoframe-backend
•	Install Python dependencies:
pip install -r requirements.txt
•	Apply database migrations:
python manage.py migrate
•	Create a superuser account:
python manage.py createsuperuser
•	Run the development server:
python manage.py runserver
•	Access the Django admin panel at http://localhost:8000/admin/ to add and manage frames.

Frontend (React)
Open a new terminal and navigate to the frontend directory:
cd photoframe-frontend
Install npm dependencies:
npm install
Start the development server:
npm start
Access the frontend application at http://localhost:3000/.

API Endpoints
GET /api/frames/: Fetch all frames.
POST /api/frames/: Add a new frame.
PATCH /api/frames/{id}/: Update a frame (toggle top sales).
DELETE /api/frames/{id}/: Delete a frame.
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements
Hat tip to anyone whose code was used
Inspiration
Etc 	

