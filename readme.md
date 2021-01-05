# Subscition and payment gateway integration

## Code review by CodeGrip

![Review](/Images/codegrip_review.png)


## Step 1: Installation, project cloning and python environment setup

#### Python download link : 
##### `https://www.python.org/downloads/`

#### mysql download link : 
##### Installaing file download : `https://dev.mysql.com/downloads/mysql/` \
##### Download MySql workbench( optional ) : `https://www.mysql.com/products/workbench/`

#### Clone the repo :
##### ```git clone https://github.com/tejas17kuthe/SubsciptionAndPayment_REST_DJANGO.git```

##### Folder Structure:
```
└── SubsciptionAndPayment_REST_DJANGO
    ├── mysql_details
    └── restAPI
        ├── images
        ├── mysql_details
        ├── restAPI
        │   └── __pycache__
        └── subscriptionAPI
            ├── __pycache__
            └── migrations
                └── __pycache__
```

#### Open command promp or terminal and cd into the downloaded folder
##### ` cd SubsciptionAndPayment_REST_DJANGO`

#### Install python virtaulenv package
##### ` pip install virtualenv `  or  ` pip3 install virtualenv ` 
 
#### Create Virtual environament and activate it

##### Create : ` virtualenv env_restAPI `

##### Activate : mac and linux ` source ./env_restAPI/bin/activate `  

## step 2: Resolve dependancies and run the project

#### Install requirement.txt
##### ` cd restAPI`

##### `pip install -r requirements.txt` 

#### Go to mysql_details and change the .cnf file details for database connection
##### ` cd mysql_details `

##### To Edit file mac and linux you can execute ` nano connection.cnf` and in windows you can use text editor to edit the file.

```
[client]
database = sampleSubscription
user = <Enter your mysql username>
password = <Enter your mysql password>
default-character-set = utf8
```
and save the file 

##### Now you have to create a blank schema in mysql by name `sampleSubscription`. You can do this by using MySql workbench or mysql shell.
mysql shell command
```
mysql -u <yout mysql username> -p

mysql > CREATE SCHEMA `sampleSubscription`;
Query OK, 1 row affected (0.00 sec)

mysql > exit;
Bye

```

#### Go to restAPI
##### `cd ..`
##### `python manage.py makemigrations`
#### `python manage.py migrate`
This will create tables in database
#### Now create an admin user to perform admin operations like adding new manager details.
```
python manage.py createsuperuser 
Username (leave blank to use 'tejaskuthe'): <User name of your choice>
Email address: <your email id>
Password: < password >
Password (again): < confirm password >
Superuser created successfully.

```
Installation and dependencies completed. Now start django server
#### `python manage.py runserver`
#### You should see
```
Performing system checks...

System check identified no issues (0 silenced).
January 05, 2021 - 12:38:32
Django version 2.0.2, using settings 'restAPI.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
##### congratulation application is running successfully

## Step 3: Using postman and API endpoints.

### Download and Install Postman.
####       link `https://www.postman.com/downloads/`

### API
#### User `Login API` POST request `http://127.0.0.1:8000/login/`
 
```
This api is used to log into the server.
Admin user and manager both can login to the server.
```
![Review](/Images/loginapi.png)

#### Create new manager account. `Signup API` POST request `http://127.0.0.1:8000/signup/`
```
This api does not require any login password to perform action. 
As the user which will be creating the account will be a first time user.
If we want we can also specifically allow admin user to create manager account and restrict all other users from creating an account, this operation will need update in the application. 
```
![Review](/Images/signupapi.png)



#### `Subscription API`
![Review](/Images/subscriptionapi.png)

### Get all manaer details
![Review](/Images/managerdetailapi.png)

### Payment Get Has API
![Review](/Images/paymentapi.png)

### Sending Received JSON with hash to payu money api
![Review](/Images/payupaymentapi.png)
