# ShellPost
ShellPost is a command-line tool that allows you to send Emails with attachments directly from your Terminal. 

# Installation
1. Clone the Repository
git clone https://github.com/Sergius-Nyah/shellpost.git
2. Navigate to the project directory
cd shellpost
3. Install any dependencies. 
pip install -r requirements.txt

# Usage 
1. Add execution permission using the chmod command: 
   `chmod +x src/email/email_sender/py`
2. Run with python interpreter : `python3 src/email/email_sender.py`
You can provide the path to the attatchment as a Command Line Argument: ``` bash
                   python email_sender.py --attachment path/to/attachment 
Replace path/to/your/attachment with the actual path to the file you want to attach to the email.

You can also provide the recipient's email address and the subject of the email as command-line arguments:

python email_sender.py --recipient recipient@example.com --subject "Hello, World!" --attachment path/to/your/attachment

Replace recipient@example.com with the actual email address of the recipient, and replace "Hello, World!" with the actual subject of the email.

# Contributing
To contribute, please visit our [Contribution guidelines](/docs/contributing.md)
 