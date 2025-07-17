# note_taking

This is a simple note-taking web app built using Python with the Flask web framework and backed by MariaDB for persistent data storage. The app allows users to write, save, and display notes along with timestamps.

## Features
 1. Write and save notes: Users can add notes and they are saved in the database with a timestamp.
 2. Display saved notes: Saved notes are displayed in descending order based on their creation time.
 3. Backup: Automated database backups to a dedicated EBS volume for data persistence.

## Technologies Used

    1. Frontend: HTML, CSS (responsive design)
    2. Backend: Flask (Python 3)
    3. Database: MariaDB
    4. Deployment: AWS EC2, EBS

# Installation and Setup
  Prerequisites

    1. AWS EC2 instance running with a RHEL or Ubuntu-based OS.
    2. Python 3.x installed.
    3. MariaDB installed and running.
    4. AWS CLI for managing resources (optional but recommended).

1. Clone this repository

    git clone https://github.com/yourusername/note_taking.git
    cd note_taking

3. Install Dependencies

Install Flask and other required Python packages:

    pip3 install flask
    pip3 install mysql-connector-python

3. Configure MariaDB

Make sure MariaDB is running and create a new database and user for the app:

    sudo mysql -u root -p

Then, run the following SQL commands:

    CREATE DATABASE notesdb;
    CREATE USER 'noteuser'@'localhost' IDENTIFIED BY 'notepass';
    GRANT ALL PRIVILEGES ON notesdb.* TO 'noteuser'@'localhost';
    FLUSH PRIVILEGES;

4. Setup the Database

The app uses a notes table to store notes. Connect to your MariaDB instance and create the table:

    sudo mysql -u noteuser -p

Run the following SQL:

    USE notesdb;
    CREATE TABLE notes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        content TEXT,
        timestamp DATETIME
    );

5. Update the Flask Application

In the app.py file, make sure you update the MariaDB connection details (if necessary):

    db = mysql.connector.connect(
        host="localhost",
        user="noteuser",
        password="notepass",
        database="notesdb"
    )

6. Run the Application

You can now start the Flask app by running:

    sudo python3 app.py

The app should be accessible at your EC2 instance's public IP.

Open your browser and go to:  http://<your-ec2-public-ip>

You should be able to write and save notes!
Automated Backup to EBS Volume

This project also includes an automated MariaDB backup script.
Create Backup Script

The script /backup/db-backup.sh is used to back up the MariaDB database:

    #!/bin/bash
    mysqldump -u noteuser -pnotepass notesdb > /backup/notesdb_$(date +%F_%T).sql

3. Monitor Backups

Backups are saved in the /backup directory, where the script creates a new backup file with a timestamp.
