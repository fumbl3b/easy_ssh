HEY! Welcome to Easy SSH. This is a simple Python-based SSH server that you can set up in no time.

GETTING STARTED

1. Install dependencies

``` pip install -r requirements.txt ```

1. Generate a RSA Key

``` ssh-keygen -t rsa -b 2048 -f test_rsa.key ```

remember what passphrase you used.  you'll need it to run the application.

2.	Run the Server

``` python3 server.py ```

3. Enter your passphrase and now you're cooking.

4. Notes

	•	Remember where you saved your key.
	•	Make sure Python 3.7+ is installed.

Enjoy your new SSH server!