# Bobjoying

Private website to put together my cooking recipe.

Base on [Django:제로부터 시작하는 인스타그램](https://youtu.be/M8UPyeF5DfM)


## Load Map

- [ ] Add Update & Delete function
- [ ] Deploy application with AWS
- [ ] Update login & reply function(run with Enter)
- [ ] Add weekly menu planner function


## How to Run

<p>1. make virtual env</p>

```
python -m venv venv
```

<p>2. Activate virtual env</p>

```
source ./venv/Scripts/activate
```

<p>3. Intall package</p>

```
pip install -r requirements.txt
```

<p>4. DB migration</p>

```
python manage.py makemigrations
```
```
python manage.py migrate
```

<p>5. Runserver</p>

```
python manage.py runserver
```

<p>6. Connect Localhost</p>

``` 
http://127.0.0.1:8000/main/
```

<p>7. Login with test account</p>

```
test_id
test_pw
```