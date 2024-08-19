
# Easy SSH

HEY! Welcome to Easy SSH. This is a simple Python-based SSH server that you can set up in no time.

## GETTING STARTED

1. **Set Up a Virtual Environment (Recommended)**

   To keep your project dependencies isolated, it's recommended to create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
   ```

2. **Install Dependencies**

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Generate an RSA Key**

   Run the following command to generate your key:

   ```bash
   ssh-keygen -t rsa -b 2048 -f test_rsa.key
   ```

   Remember the passphrase you used—you'll need it to run the application.

4. **Run the Server**

   Start the server with:

   ```bash
   python3 server.py
   ```

5. **Enter your passphrase** and now you're cooking.

## Notes

- Remember where you saved your key.
- Make sure Python 3.7+ is installed.

Enjoy your new SSH server!