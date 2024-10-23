# User Guide for dbtool

## Introduction

`dbtool` is a command-line tool that allows you to perform basic CRUD operations on a SQLite database.

## Installation

### **Prerequisites**

- Python 3.7 or higher
- `pip` package manager

### **Steps**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dbtool.git
   cd dbtool
   ```

2. **Install the Package**

    ```bash
    pip install .
    ```

### **Usage**

After installation, you can use the `dbtool` command.

### **Commands**

1. **Add a Record**

   ```bash
   dbtool add
   ```

   You will be prompted to enter the name and value.

2. **View Records**

    ```bash
    dbtool view
    ```

    Displays all records in the database.

3. **Update a Record**

   ```bash
   dbtool update
   ```

   You will be prompted to enter the record ID, new name, and new value.

4. **Delete a Record**

    ```bash
    dbtool delete
    ```
    
    You will be prompted to enter the record ID.

### Uninstallation

To uninstall `dbtool`, run:

    ```bash
    pip uninstall dbtool
    ```

