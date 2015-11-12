HELLO FELLOW GRADUATES

#If you do not have Git installed in your  machine already Follow these  steps:
Also checkout for more info http://brew.sh/

###Table of Contents:
1. Installation
2. Your First Pull Request (and all future submissions)

#Installation
##Install Homebrew
Homebrew is a command-line package manager for OS X, which means it is a tool that helps you find, install, and update other tools that were not installed on your system when it came out of the factory. (Go here if you'd like to learn more about Homebrew.)

Copy and paste this into the terminal:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Type this to verify your installation:
brew -v
You should get something like this:
Homebrew 0.9.5

#Install and Configure Git and GitHub
##Install Git
Git is the most popular versioning and source control software currently in use. It allows you to keep past working versions of your code safe from experimentation, and it allows multiple developers to work on the same code base without interfering with each other.

See if you have Git installed by typing
git --version
If you get something like
git version 2.x.x
go on to the next step. Otherwise, use Homebrew to install Git with
brew install git
Now check your version again to verify your install.

#Configure Git
If you already have a GitHub account for whatever reason, be absolutely certain which email address it uses, because you must use the same email address here. Either way, remember the email you use.
Type the following, substituting your actual name and email address. You must use the quotation marks if spaces are involved.

git config --global user.name "Your Actual Name"
git config --global user.email "Your Actual Email"
You can check your configuration by typing
git config --list
If you like, you can make your Git output colorful with
git config --global color.ui auto

#Generate an SSH Key
If you already have an SSH key for some reason, check by typing
ls ~/.ssh/id_rsa
and you'll see something like
/Users/YourName/.ssh/id_rsa

which means you're done with this step (move on to the GitHub section). If you get a No such file or directory message, you'll have to generate a new key.
Again, be absolutely certain you use the same email address for configuring Git, and type the following, substituting your actual email address:

ssh-keygen -C student@example.com -t rsa

Press enter to accept the default key save location.

Hit enter to accept blank passphrase, then hit enter again.

You should get some output like this:

Generating public/private rsa key pair.
Enter file in which to save the key (/Users/student/.ssh/id_rsa):
Created directory '/Users/student/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:

Your identification has been saved in /Users/student/.ssh/id_rsa.
Your public key has been saved in /Users/student/.ssh/id_rsa.pub.
The key fingerprint is:

88:54:ab:77:fe:5c:c3:7s:14:37:28:8c:1d:ef:2a:8d student@example.com

Finally, we'll add the key to the authentication agent with

ssh-add ~/.ssh/id_rsa

You should get some output like this:

Enter passphrase for /Users/student/.ssh/id_rsa:
Identity added: /Users/student/.ssh/id_rsa (/Users/student/.ssh/id_rsa)"


#GitHub
Originally Git was invented to help developers work on the Linux kernel, and code was distributed peer-to-peer. It was so loved that GitHub was created: a web-based Git repository hosting service that added many new features such as visualization tools, social networking, wikis, and more.

If you don't already have a GitHub account, go to http://github.com and register for one. Remember to use that same email address!

To add your SSH key to your GitHub account, first copy it to the clipboard with

pbcopy < ~/.ssh/id_rsa.pub

Navigate to http://github.com and make sure you are logged in. Click the black gear icon in the top right corner. This will take you to the account settings page.


On the account setting page, select SSH Keys from the column on the left.

If you've installed GitHub for Mac already, you should see your key here, in which case you're done with this step.

If you don't see a key assigned to your computer, click the button that says Add SSH Key. In the title field give a name for your key that makes sense, such as your computer's name. In the key field, paste the key you copied
.
Click Add Key.

Confirm the action by providing your GitHub password.

#Install Node.js
Node is an open-source, cross-platform runtime environment for server-side applications. Node apps are written in JavaScript (even though JS was ostensibly developed for front-end scripts). Node also comes with a REPL (read-eval-print loop) and can be used to run scripts on the command line (so all calls to console.log() print to the terminal).

Use Homebrew to install Node with

brew install node

Verify your installation with
node --version

You should expect some output like this:
v0.10.35

You can play around with Node REPL by typing
node

It will give you a prompt (>) that you can use like a JS console. Quit the REPL by pressing ^c(Control+C) twice.


#Install Dependencies
Type this into the terminal:

npm install
npm is short for Node Package Manager, another package management tool that searches, installs, and updates modules just for Node.js. npm install reads the package.json file in the repo and installs all the things the package file says it needs. In addition to Bower and Grunt, useful build tools, it installs FactoryB, a tool that helps you generate dummy data to test on (elsewhere known as "fixtures").


#Keep Updated
Commit or stash everything you're working on, then checkout the branch you want to update.

git fetch upstream master
git merge -s recursive -X theirs upstream/master -m "Your commit message"
