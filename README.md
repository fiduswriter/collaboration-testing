HOWTO
======

Test driver
====

1. Install Selenium chromedriver.

2. Enter the virtual fiduswriter environment (or create a new one).

3. Install python selenium bindings:

    pip install selenium

4. Copy test-driver.py to testing.py.

5. Fill in the server details at the top of testing.py.

6. Execute the test:

    python testing.py

Test keyboard events via X-Server (Linux)
====

1. Enter the virtual fiduswriter environment (or create a new one).

2. Install loremipsum and python bindings for libxdo:

    pip install selenium python-libxdo

3. Open the browser window on the page where the typing is to happen.

4. Start the test:

    python autotype.py

5. Switch back to the browser window within 5 seconds.

6. In order to stop the test, switch to the terminal window where you started
   the test and hit CTRL+C. Test will end after a few seconds.
