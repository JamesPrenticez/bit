# Bit Bot
## Getting Started

### Backend Setup (Windows)
0. cd backend
1. python -m venv venv
2. . venv/Scripts/activate
3. pip install -r requirements.txt
4. python main.py

### Frontend Setup
0. cd frontend
1. npm i / npm audit fix
2. npm run dev
3. http://localhost:3000/

### Requirements File
- To create a requirement file using pipreqs run the following command:
  - ``` pip install pipreqs ```
  - ``` pipreqs /path/to/project ``` (or . for root directory)
  - ``` pipreqs . --force ``` (rewrite exisiting)

### Enviroment Variables
(How to set up dotenv)[https://www.youtube.com/watch?v=YdgIWTYQ69A]
"Sometimes when your programming you have code or little bits and pieces that you dont want to share with the entire world - and I'm not just talking about you being embarrassed about your programming"
- ``` pip install python-dotenv ```
- Create a .env file and include the required information as shown in the .env.example 

### Usefull links
(HMR with flask)[https://python-webpack-boilerplate.readthedocs.io/en/latest/live_reload/]