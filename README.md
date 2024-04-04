# FetchChallenge
Algorithm Explanation:

The algorithm identifies the fake gold bar among nine bars within only two weighings. Here's a breakdown of the algorithm:

1. Divide the nine gold bars into three groups of three bars each:
   - Group A: Bars 0, 1, and 2
   - Group B: Bars 3, 4, and 5
   - Group C: Bars 6, 7, and 8

2. Compare the weights of Group A (0, 1, 2) and Group B (3, 4, 5):
   - If the weights are equal, the fake gold bar is in Group C.
   - Proceed to compare any two bars within Group C:
     - If the two bars have equal weight, the third bar is the fake gold bar.
     - Otherwise, the lighter bar is the fake gold bar.

3. If the weight of Group A is greater than the weight of Group B:
   - The fake gold bar is in Group B.
   - Compare any two bars within Group B:
     - If the two bars have equal weight, the third bar is the fake gold bar.
     - Otherwise, the lighter bar is the fake gold bar.

4. If the weight of Group A is less than the weight of Group B:
   - The fake gold bar is in Group A.
   - Compare any two bars within Group A:
     - If the two bars have equal weight, the third bar is the fake gold bar.
     - Otherwise, the lighter bar is the fake gold bar.



Technical Requirements

The testing has been done using selenium and safari browser driver.the scripts are written using Python.so follow below steps to run the automation scripts

1) Open Terminal and run the following command safaridriver --enable
2) Then open Safari web browser and enable the Allow remote Automation by following below steps
Open safari browser-> develop -> Developer Settings -> Allow remote automation
3) use any IDE of your choice for python and install selenium package by running below command in the terminal
pip install selenium


Output
after the testing, the list of weighings are displayed in the console as well as in the web app


