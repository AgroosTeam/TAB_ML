# TAB ML FastAPI sever
***
[<img width="45%" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">](https://www.python.org/)
[<img width="45%" src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">](https://fastapi.tiangolo.com/)
## Quickstart
***
Clone this repository:
```
  https://github.com/AgroosTeam/TAB_ML.git
```
Continue in the cloned repository folder.

Install requirements:
```
  pip install -r requirements.txt
```

Run to start FastAPI server:
```
  uvicorn API.main:app --reload
```

## API endpoints
```
INFO:     Will watch for changes in these directories: [`YOUR_FILE_PATH`]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15092] using StatReload
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\Uzer\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
INFO:     Started server process [17876]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
### POST
- [/predict]() <br>
  **description:** adds one message to database <br>
  **body:**
  ```json
  {
    "text": "TextField"
  }
  ```