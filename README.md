# Udacity-Log-Project
A database log tool. It uses `psycopg2` to communicate with <a href="https://www.postgresql.org">PostgreSQL Database</a>, then it queries the database and wirte the results in a text file.

## How to run it
* clone the project using `https://github.com/mostafa-saeed/Udacity-Log-Project`.
* change the directory using `cd Udacity-Log-Project`.
* Run the application using `python3 app.py`.
* Then you will find `logFile.txt` which inclues all the results from the database.

## Files explanation
* app.py
  * This file contains the core logic of the application.
  * It also inculdes the log Function which writes a string in both terminal window and in the log file.
* db_functions.py
  * This file contains the database string.
  * It send queries to the database and return the result.

## Here's an example of the application's output
### Terminal window
<img src="https://image.ibb.co/hGSa2m/Screenshot_from_2017_11_23_13_10_48.png" alt="Terminal window output">

### Log file
<img src="https://preview.ibb.co/ckQTNm/Screenshot_from_2017_11_23_13_15_30.png" alt="Screenshot_from_2017_11_23_13_15_30" alt="logFile.txt output">
