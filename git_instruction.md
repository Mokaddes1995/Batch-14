# Git & GitHub সম্পূর্ণ বাংলা গাইড
## নতুন Repository তৈরি থেকে GitHub-এ Push করা পর্যন্ত

====================================
PART 1: GITHUB REPOSITORY তৈরি
====================================

1. https://github.com এ যাও।
2. নিজের Account-এ Login করো।
3. New Repository-তে ক্লিক করো।
4. Repository Name দাও। যেমন: Batch-14
5. Description লিখো।
6. Public অথবা Private নির্বাচন করো।
7. README, .gitignore এবং License আপাতত Add করবে না।
8. Create Repository ক্লিক করো।

====================================
PART 2: LOCAL FOLDER তৈরি
====================================

নিজের Computer-এ Main Folder তৈরি করো।

Example:

Batch-14/
│
├── python/
├── javascript/
├── html/
├── rest api/
├── react js/
├── django/
├── sql/
├── project/
└── assignment/

মনে রাখবে:
Git খালি Folder Track করে না।
প্রতিটি Folder-এর ভিতরে README.md তৈরি করতে পারো।

====================================
PART 3: GIT CONFIGURE
====================================

Git Username:

git config --global user.name "Your Name"

Git Email:

git config --global user.email "your-email@gmail.com"

Configuration Check:

git config --global --list

====================================
PART 4: SSH CONFIGURE
====================================

Step 1: SSH Key তৈরি

ssh-keygen -t ed25519 -C "your-email@gmail.com"

Step 2: SSH Agent চালু

eval "$(ssh-agent -s)"

Step 3: SSH Private Key Add

ssh-add ~/.ssh/id_ed25519

Step 4: Public Key দেখো

cat ~/.ssh/id_ed25519.pub

Step 5: GitHub-এ Public Key Add

GitHub Settings
→ SSH and GPG Keys
→ New SSH Key
→ Public Key Paste
→ Add SSH Key

Link:
https://github.com/settings/keys

Step 6: SSH Connection Test

ssh -T git@github.com

গুরুত্বপূর্ণ:
id_ed25519 = Private Key
id_ed25519.pub = Public Key

Private Key কাউকে দেবে না।
GitHub-এ শুধু Public Key Add করবে।

====================================
PART 5: LOCAL REPOSITORY INITIALIZE
====================================

প্রথমে Main Folder-এর ভিতরে Terminal ওপেন করো।

Step 1:

git init

Step 2:

git add .

Step 3:

git commit -m "Initial commit"

Step 4:

git branch -M main

====================================
PART 6: REMOTE CONNECT
====================================

GitHub Repository থেকে SSH URL Copy করো।

Example:

git@github.com:USERNAME/REPOSITORY.git

Remote Add:

git remote add origin git@github.com:USERNAME/REPOSITORY.git

এখানে নিজের GitHub Username এবং Repository Name বসাবে।

Remote Check:

git remote -v

====================================
PART 7: GITHUB-এ PUSH
====================================

git push -u origin main

এবার তোমার Local Project GitHub-এ Upload হবে।

====================================
PART 8: DAILY GIT COMMANDS
====================================

নতুন Code বা Assignment Add করার পর:

Step 1: Add

git add .

Step 2: Commit

git commit -m "Added new assignment"

Step 3: Push

git push

GitHub থেকে Update আনতে:

git pull origin main

====================================
PART 9: IMPORTANT GIT COMMANDS
====================================

Git Status:

git status

Branch Check:

git branch

Commit History:

git log --oneline

Remote Check:

git remote -v

Remote Remove:

git remote remove origin

Remote URL Change:

git remote set-url origin git@github.com:USERNAME/REPOSITORY.git

====================================
PART 10: ANOTHER COMPUTER SETUP
====================================

অন্য Computer থেকে Repository ব্যবহার করতে:

1. Git Install করো।
2. Git Username ও Email Configure করো।
3. নতুন SSH Key তৈরি করো।
4. Public Key নিজের GitHub Account-এ Add করো।
5. SSH Connection Test করো।
6. Repository Clone করো।

Clone Command:

git clone git@github.com:USERNAME/REPOSITORY.git

মনে রাখবে:
প্রত্যেক Computer-এর জন্য আলাদা SSH Key তৈরি করা ভালো।
একই GitHub Account-এ একাধিক Public Key Add করা যায়।
Private Key কখনো অন্য কাউকে দেবে না।

====================================
PART 11: DEVELOPMENT TEAM MEMBER ADD
====================================

1. প্রত্যেক Team Member-এর নিজস্ব GitHub Account থাকতে হবে।
2. প্রত্যেকে নিজের Computer-এ SSH Key তৈরি করবে।
3. প্রত্যেকে নিজের Public Key নিজের GitHub Account-এ Add করবে।
4. Repository Owner তাদের Collaborator হিসেবে Invite করবে।
5. তারা Invitation Accept করবে।
6. এরপর SSH দিয়ে Repository Clone করবে।

Collaborator Add:

GitHub Repository
→ Settings
→ Collaborators
→ Add People

====================================
PART 12: COMPLETE GIT WORKFLOW
====================================

GitHub Repository তৈরি
          |
          v
Local Folder তৈরি
          |
          v
Git Configure
          |
          v
SSH Configure
          |
          v
git init
          |
          v
git add .
          |
          v
git commit -m "Initial commit"
          |
          v
git branch -M main
          |
          v
git remote add origin SSH_URL
          |
          v
git push -u origin main
          |
          v
        DONE!

====================================
IMPORTANT NOTES
====================================

1. এক Computer-এ SSH Key একবার Configure করলেই
   পরবর্তী Repository-গুলোতে ব্যবহার করতে পারবে।

2. একটি SSH Key দিয়ে একাধিক Repository ব্যবহার করা যায়।

3. Private Key কখনো GitHub-এ Upload করবে না।

4. Git খালি Folder Track করে না।

5. Team-এর সঙ্গে কাজ করার আগে সর্বশেষ Code Pull করে নেবে।

6. সবসময় অর্থপূর্ণ Commit Message ব্যবহার করবে।

7. Repository-তে Password, API Key বা Secret
   Information Upload করবে না।

====================================
শেষ কথা
====================================

Git = Version Control System

GitHub = Code Hosting Platform

দুটো একসঙ্গে ব্যবহার করে নিজের Project,
Assignment এবং Team Development পরিচালনা করতে পারবে।