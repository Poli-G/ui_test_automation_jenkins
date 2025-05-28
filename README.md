### ui_test_automation_jenkins
UI test automation for the Jenkins web interface using Selenium and Pytest with Page Object Model (POM) structure.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/github/license/Poli-G/ui_test_automation_jenkins)


### Technologies Used

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**

### Project Goals

- Practice UI test automation on a real application (Jenkins)
- Apply clean and scalable test architecture
- Develop reusable page objects
- Use `pytest` fixtures and configuration

### Project Structure
<pre>ui_test_automation_jenkins/
├── .venv/            # Virtual environment
├── .env              # Environment variables 
├── pages/            # Page objects
└  └── login_page.py  # Page Object for the login page
├── tests/            # Test files
└  └── test_login.py  # Test for autorisation
├── conftest.py       # Fixtures for pytest
├── pytest.ini        # Pytest configuration
├── requirements.txt  # Dependencies
└── README.md         # Project description  
</pre>

### How to Run

### 1. Create and activate a virtual environment
 ##### Linux/macOS
  ```bash     
    python3 -m venv .venv
    source .venv/bin/activate
  ```
 ##### Windows
  ```bash
    python -m venv .venv
    .venv\Scripts\activate
  ```

### 2. Install dependencies
  ```bash
    pip install -r requirements.txt
  ```

### 3. Run tests
  ```bash
    pytest
  ```


