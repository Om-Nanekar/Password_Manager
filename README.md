# Password Manager (Python CLI App)

This is a simple command-line based Password Manager built using Python. It helps you create strong passwords, store login information, and view your saved password history. All data is saved permanently in a JSON file.

---

# Features:

* Password protected access to the manager
* Generate strong and random passwords
* Add new entries with:
  Mail
  Website URL
  Username
  Password
  Date and Time (auto recorded)
* View saved passwords in table format
* Passwords saved permanently in `password_history.json`

---

# How to Run:

1. Make sure Python is installed

2. Install required library
   Run this command:
   pip install tabulate

3. Open terminal in the folder and run:
   python main.py

4. Enter master password to access the manager
   (Default master password is: abcd1234)

---

# File Structure:

main.py – Main script for the password manager
password\_history.json – Stores your saved passwords
README.md – Project details

---

# Example Flow:

* Run the program
* Enter master password
* Choose:

  1. Create a random password
  2. Add new password
  3. Show saved passwords
  4. Exit

# Output (for option 3):
+----------------+-------------+-------------+----------------------+------------+----------+
| Mail           | URL's       | User Name   | Password             | Date       | Time     |
+----------------+-------------+-------------+----------------------+------------+----------+
| [example@mail.com](mailto:example@mail.com) | gmail.com | myusername  | mysecurepassword123! | 25-06-25   | 21:25:12 |
+----------------+-------------+-------------+----------------------+------------+----------+

---

# Built Using:

Python 3
tabulate module
json module
datetime module
random module

---

# Made by: [Om-Nanekar]

---
