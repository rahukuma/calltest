# calltest
Language : Python
Framework : Robotframework

Tested on version : 
python - 3.5
robotframework - 3.0
requests - latest version

Steps to run : 
1. CLone the project.
2. Go to root directory.
By default my mobile nos are used.
Please change the mobile no appropriately in the robot file.
Also, make changes for auth_id/auth_token/application_id accordingly in Resources/rahul_account.py
3. Run the test with robot command, as(file separtor should be used as per os):
  robot -d ../Result */PlivoTest.robot
4. After run, log as results would be stored in <ROOT_DIR>/Result
5. After run all tests should be passed.

Description of the test and its structure :
  Only test file is PlivoTest.robot
  It has some documentation to describe what a test does
  Main Library(Api firing call) is plivo_call.py
  plivo_call.py has all the functions to fire all apis
