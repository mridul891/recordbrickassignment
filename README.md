
```markdown
# Remote Bricks Assigments 

## Description
Assignment for the remotebrick org . Api endpoints for registration , login etc .

## Prerequisites
- Python 3.x
- `venv` module (comes pre-installed with Python 3.3+)

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/username/repository.git
cd repository
```

### 2. Create a Virtual Environment
Create a virtual environment in the project directory:
```bash
python3 -m venv venv
```
Replace `python3` with `python` if your default Python version is 3.x.

### 3. Activate the Virtual Environment

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **On macOS and Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
Install the required packages using `pip`:
```bash
pip install -r requirements.txt
```

### 5. Run the Python File
Run the Python file using:
```bash
python main.py
```

## Deactivating the Virtual Environment
Once you're done, deactivate the virtual environment using:
```bash
deactivate
```

## Additional Information

### Adding New Dependencies
If you need to install additional Python packages, use `pip` while the virtual environment is activated:
```bash
pip install package_name
```
Then, update the `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

### Deleting the Virtual Environment
To remove the virtual environment, simply delete the `venv` directory:
```bash
rm -rf venv
```
or on Windows:
```bash
rmdir /s /q venv
```
