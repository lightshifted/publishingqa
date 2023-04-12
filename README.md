# Set Up

Commands are executed from  `root` directory unless otherwise specified.
### 1. Create Virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Clone Motörhead Repository
```bash
git clone https://github.com/getmetal/motorhead
```

### 5. Initialize Motörhead Server
From `motorhead` directory, run the following command:
```bash
docker-compose build && docker-compose up
```

### 6. Start Flask Server
From `root` directory, run the following command:
```bash
python app.py
```

You should see the following ouput:
```bash
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.107:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 367-912-636
 ```

 ### 7. Update `.env` File With OpenAI API Key

## API Endpoints
At the moment, endpoints are available through Postman
- **POST** file `/upload`
- **POST** question `/api/answer`
- **GET** history `/sessions/publishingqa/memory`
- **DELETE** history `/sessions/publishingqa/memory`

## Postman

### Upload File
URL: _POST_ `http://localhost:5000/upload`
`Headers`: `Content-Type: multipart/form-data`
`Body`: `file: <file>` # click on 'Select Files' and select a file
Send! 🐇

### Submit Query
URL: _POST_ `http://localhost:5000/api/answer`
`Headers`: `Content-Type: application/json`
BODY: `raw` & `JSON` --> `{question: <your query>}`
Send! 🐇

### Get History (10 message max)
URL: _GET_ `http://localhost:5000/sessions/publishingqa/memory`
Send! 🐇

### Delete History
URL: _DELETE_ `http://localhost:5000/sessions/publishingqa/memory`
Send! 🐇
