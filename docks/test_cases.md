_### US_01.001 – Login to Jenkins

**Test Case ID:** TC_01.001_01
---
**Title:** Login with valid credentials  
**Preconditions:** User is on the Jenkins login page  
**Test Steps:**
1. Enter valid username  
2. Enter valid password  
3. Click the "Login" button  
**Expected Result:**
  User is redirected to the Jenkins dashboard 

****Automation:**** tests/test_login.py 

### US_02.001 – Create a New Item
---
**Test Case ID:** TC_02.001_01
---
**Title:** New Item page is accessible

**Steps:**

1. Open Jenkins Dashboard  
2. Click on “New Item”  

**Expected Result:** 
   New Item page is opened with input field and list of item types

**Automation:**  test_new_item_page.py
 

**Test Case ID:** TC_02.001_02 
---
**Title:** Enter valid item name and create

**Steps:**

1. Open New Item page  
2. Enter name: `test_item_01`  
3. Select "Freestyle project"  
4. Click OK  

**Expected Result:** 
   User is redirected to config page; item appears on dashboard

**Automation:**  test_new_item_action.py
 

**Test Case ID:** TC_02.001_03
---
**Title:** Verify accepted characters in item name

**Steps:**

1. Open New Item page 
2. Enter name: project_123 
3. Select any item type
4. Click OK

5. **Expected Result:**
   Item is created successfully; Configuration page is opened

**Automation:**  test_new_item_name.py

**Test Case ID:** TC_02.001_03
---

**Title:** Verify accepted characters in item name

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Enter name: `project_123`
2. Select any item type
3. Click OK
    
    **Expected Result:**
    
    Item is created successfully; configuration page is opened

**Automation:**  test_new_item_name.py 
 
**Test Case ID:** TC_02.001_04
---

**Title:** Special characters are not allowed in item name

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Enter name: `test@job!`
    
    **Expected Result:**
    
    Error message is shown; OK button is disabled

**Automation:** test_create_item_negative.py


**Test Case ID:** TC_02.001_05
---
**Title:** OK button disabled when item name is empty

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Leave name field empty
    
    **Expected Result:**
    
    OK button is disabled

**Automation:** test_disable_ok_button_on_empty_name.py


**Test Case ID:** TC_02.001_06
---
**Title:** Duplicate item name validation

**Preconditions:** Item `duplicate_item` already exists; user is on the New Item page

**Test Steps:**

1. Enter name: `duplicate_item`
    
    **Expected Result:**
    
    Red error message: "An item with this name already exists"; OK button is disabled

**Automation:** test_duplicate_item_name.py


**Test Case ID:** TC_02.001_07
---
**Title:** Attempt to create item without selecting item type

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Enter valid name
2. Do not select any item type
3. Click OK
    
    **Expected Result:**
    
    OK button is disabled; item is not created

**Automation:** test_create_without_type.py

**Test Case ID:** TC_02.001_08
---
**Title:** New item appears on dashboard

**Preconditions:** New item is created successfully

**Test Steps:**

1. Navigate back to Dashboard
    
    **Expected Result:**
    
    Item is listed on Dashboard

**Automation:** test_item_appears_on_dashboard.py

**Test Case ID:** TC_02.001_09
---
**Title:** Copy from non-existent item

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Enter valid name
2. Enter non-existent item in "Copy from" field
    
    **Expected Result:**
    
    After clicking OK, you are redirected to a page http://localhost:8080/view/all/createItem;  Error message: "No such job";  New item is NOT created.

**Automation:** test_copy_from_non_existent_item.py

**Test Case ID:** TC_02.001_10
---
**Title:** OK button remains disabled until all validation errors are resolved

**Preconditions:** User is on the New Item page

**Test Steps:**

1. Enter invalid name (e.g. `name!`)
2. Correct the name to a valid one (e.g. `valid_name`)
3. Select an item type
    
    **Expected Result:**
    
    OK button becomes enabled only after valid input is entered and item type is selected

**Automation:** test_invalid_item_name.py
