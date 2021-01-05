# Subscition and payment gateway integration

## Code review by CodeGrip

![Review](/Images/codegrip_review.png)


## Step 1: Installation, project cloning and python environment setup

#### Python download link : 
`https://www.python.org/downloads/`

#### mysql download link : 
Installaing file download : `https://dev.mysql.com/downloads/mysql/` \
Download MySql workbench( optional ) : `https://www.mysql.com/products/workbench/`

#### Clone the repo :
```git clone https://github.com/tejas17kuthe/SubsciptionAndPayment_REST_DJANGO.git```

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
` cd SubsciptionAndPayment_REST_DJANGO`

#### Install python virtaulenv package
 ` pip install virtualenv `  or  ` pip3 install virtualenv ` 
 
#### Create Virtual environament and activate it

##### Create : ` virtualenv env_restAPI `

##### Activate : mac and linux ` source ./env_restAPI/bin/activate `  

## step 2: Install requrement.txt and run the project

#### Install requirement.txt
` cd restAPI`

##### `pip install -r requirements.txt` 

#### Go to mysql_details and change the .cnf file details for database connection
` cd mysql_details `

##### To Edit file mac and linux you can execute ` nano connection.cnf` and in windows you can use text editor to edit the file.

```
[client]
database = sampleSubscription
user = <Enter your mysql username>
password = <Enter your mysql password>
default-character-set = utf8
```
and save the file 

##### Now you have to create a blank schema in mysql. You can do this by using MySql workbench or mysql shell.
mysql shell command
```
mysql -u <yout mysql username> -p

mysql > CREATE SCHEMA `sampleSubscription`;
Query OK, 1 row affected (0.00 sec)

```
