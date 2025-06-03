### US_01.001 – Login to Jenkins

**Test Case ID:** TC_01.001_01  
**Title:** Login with valid credentials  
**Preconditions:** User is on the Jenkins login page  
**Test Steps:**
1. Enter valid username  
2. Enter valid password  
3. Click the "Login" button  
**Expected Result:**
  User is redirected to the Jenkins dashboard 

**Automation:** `tests/test_login.py

### US_02.001 – Create a New Item

**Test Case ID:** TC_02.001_01  
**Title:** New Item page is accessible

**Steps:**

1. Open Jenkins Dashboard  
2. Click on “New Item”  

**Expected Result:** 
   New Item page is opened with input field and list of item types

**Automation:**  test_new_item_page.py
---

**Test Case ID:** TC_02.001_02  
**Title:** Enter valid item name and create

**Steps:**

1. Open New Item page  
2. Enter name: `test_item_01`  
3. Select "Freestyle project"  
4. Click OK  

**Expected Result:** 
   User is redirected to config page; item appears on dashboard


**Automation:**  test_new_item_action.py
---

**Test Case ID:** TC_02.001_03
**Title:** Verify accepted characters in item name

**Steps:**

1. Open New Item page 
2. Enter name: project_123 
3. Select any item type
4. Click OK

5. **Expected Result:**
   Item is created successfully; Configuration page is opened

**Automation:**  test_new_item_name.py
---
**Test Case ID:** TC_02.001_03

**Title:** Verify accepted characters in item name

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Enter name: `project_123`
2. Select any item type
3. Click OK
    
    **Expected Result:**
    
    Item is created successfully; configuration page is opened