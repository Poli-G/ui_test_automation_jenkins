## Test Case: Login with valid credentials

**User Story:** As a user, I want to log in to Jenkins so I can access the dashboard.

- **ID:** TC_UI_001
- **Preconditions:** User is on the Jenkins login page.
- **Test Steps:**
    1. Enter valid username.
    2. Enter valid password.
    3. Click the "Login" button.
- **Expected Result:** User is redirected to the Jenkins dashboard.
- **Automation:**  `tests/test_login.py`