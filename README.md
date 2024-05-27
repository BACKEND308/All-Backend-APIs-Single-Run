# All-Backend-APIs-Single-Run
For simplification purposes, this is a repo that merges all the backend apis into one. This means that only one server has to be run by users.
## Running the backend server:
### 1.Clone this rpository
```
    git clone github.com/BACKEND308/All-Backend-APIs-Single-Run
```
### 2.Install the required packages with npm
You need to have node.js installed for this step. Please download it from the node.js [website](https://nodejs.org/en/download/package-manager) if you don't have it already, and follow the installation instructions.
You will also need to have nodemon installed. For this step do the following
```
    npm install -g nodemon
```
Now you can install the required packages by running:
```
    npm install
```
### 3.Run the server
Run
```
    npm start
```
## Configuring environment variables
**PORT:** you can change the value of the port as needed
### Connection to MySQL:
You will need to set the following variables to connect to a MySQL database and create tables there equivalent to the MogoDB collections.
**MYSQL_HOST:** 

**MYSQL_USER**

**MYSQL_PASSWORD**

**MYSQL_DATABASE**
