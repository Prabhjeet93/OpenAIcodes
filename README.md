# OpenAIcodes


Write code to automate the automation testing.
1. you will write a test case, Code should read that test case and create a test script by calling corresponding methods.
2. there will be rules to writing the test cases.


test case -> Sample
1. open facebook url ->				 1. Open facebook url "www.facebook.com"
2. enter username in text filed  ->  2. Enter username "test@test.com" in "username_webelement"
3. enter password				 ->  3. Enter username "password" in "pass_webelement"
4. click on login button         ->  4. Click on "login" button
5. validate home page title.     ->  5. Validate the home page with text "welcome to facebook" in "val_homepage_webelement"


It should create a test script.


purposed Solution :- 

1. Create a utlity class with proper mrthod names. In the methods pass the action, webelement, text, flag
2. Now Write Test case in a format. ( it should contain few specific keywords, test data and webelements.
3. Write code to convert test case in to test script. -> in to a separate file. --> This will be the main code.


Advantage over BDD ->  BDD has similar functionality but we will have advantage
1. It will write test scripts by seeing test cases.
2. We dont have to write code everytime for the each test step.
3. It will call automatically.