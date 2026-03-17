# Digital-Hunter-2

Final Exam Day 2 
Yehuda Freiman 205368319 Arava

## תיאור
שירות api כותב שאילתות אנליטיות מול MySQL כדי להפיק תובנות מודיעיניות על סמך הנתונים שעובדו

## ארכיטקטורה
````
 dump.sql נטען למסד הנתונים >
 dal.py מבצע שאילתות >
 main.py מקים שרת api לצורך גישה לשאילתות
````

## דרישות מקדימות
- Docker + Docker Compose
- Python 3.10+
- Git

## הרצה מקומית

```bash
# שכפל את הריפו
git clone https://github.com/yehudafreiman/Digital-Hunter-2.git
# הרץ את כל השירותים
docker-compose up --build
```

## משתני סביבה
הגדר קובץ `.env` בתיקייה הראשית:
```env
DB_HOST=mysql
DB_PORT=3306
DB_NAME=digital_hunter
DB_USER=root
DB_PASSWORD=root
```

## מבנה הפרויקט
````
├── FastAPI - Swagger UI.pdf
├── Figure_1.png
├── README.md
├── __pycache__
├── api
│   ├── Dockerfile
│   ├── __pycache__
│   │   ├── dal.cpython-313.pyc
│   │   ├── digital_hunter_map.cpython-313.pyc
│   │   └── main.cpython-313.pyc
│   ├── dal.py
│   ├── digital_hunter_map.py
│   ├── main.py
│   ├── ne_50m_admin_0_countries.dbf
│   ├── ne_50m_admin_0_countries.shp
│   ├── ne_50m_admin_0_countries.shx
│   └── requirements.txt
├── docker-compose.yml
└── dump.sql
````