#!/usr/bin/env python
# coding=utf-8

import os
import subprocess

print("\033[96mHelo! You are in the repository: \033[0m\n")
subprocess.call('git remote -v', shell=True)

print("\033[96m\nAvailable branches at the moment: \033[0m")
subprocess.call('git branch', shell=True)
valid_branches = subprocess.Popen('git branch', shell=True, stdout = subprocess.PIPE)
valid_branches = valid_branches.communicate()[0]
valid_branches = str(valid_branches)
valid_branches = valid_branches.replace('\\n','').replace('*','').replace('b','').replace("'",'').lstrip().rstrip()
valid_branches = valid_branches.split(' ')
valid_branches =[ x for x in valid_branches if x != '']



print("\033[96m\nBranches fused with the current: \033[0m")
subprocess.call('git branch --merged', shell=True)
fused = subprocess.Popen('git branch --merged', shell=True, stdout = subprocess.PIPE)
fused = fused.communicate()[0]
fused = str(fused)
fused = fused.replace('\\n','').replace('*','').replace('b','').replace("'",'').lstrip().rstrip()
fused = fused.split(' ')
fused =[ x for x in fused if x != '']



print("\033[91m\nand not fused: \033[0m")
subprocess.call('git branch --no-merged', shell=True)
not_fused = subprocess.Popen('git branch --no-merged', shell=True, stdout = subprocess.PIPE)



a = str(input("\033[96mDo you want to see the last commits on the selected branches?\033[0m \033[91m(Yy/Nn)\033[0m "))
if a =="Y" or a=="y":
    subprocess.call('git branch -v', shell=True)

branch1 = str(input("Enter the name of the first branch: "))
branch2 = str(input("Enter the name next branch: "))

if (branch1 == 'A' and branch2 !='A') or (branch1 == 'B' and branch2 != 'B') \
        or (branch1 == 'C' and branch2 !='C') or (branch1 == 'master' and branch2 != 'master'):
    print('\033[92mThe entered branch names are correct. Start merge\033[0m')
else:
    print('\033[91mError. Invalid branch names.\033[0m')


for x in fused:
    if branch1 == x:
        for y in fused:
            if branch2 == y:
                print("\033[91mThe selected branches were already merge! \nThe commit will be deleted and merging is made\033[0m")
                subprocess.call ('touch text', shell=True)
                f = open('text', 'w')
                for i in branch1:
                    f.write(i + '\n')
                f.close()
                subprocess.call('VAR1="cat text"', shell=True)
                subprocess.call('git checkout $VAR1', shell=True)
                subprocess.call('git log > text', shell=True)
                subprocess.call("awk '/Merge/ {print}' text > text_awk", shell=True)
                subprocess.call("awk '{print $2}' text_awk > text", shell=True)
                subprocess.call('VAR2="cat text"', shell=True)
                subprocess.call('git reset -- hard $VAR2', shell=True)
                f = open ('text', 'w')
                for i in branch1:
                    f.write(i + '\n')
                f.close()
                subprocess.call ('VAR3="cat text"', shell=True)
                subprocess.call ('git merge --squash $VAR3', shell=True)
                subprocess.call ('rm -rf text', shell=True)
                subprocess.call ('rm -rf text_awk', shell=True)
                subprocess.call ("notify-send 'complete! ))'", shell=True)


            else:
                subprocess.call ('touch text', shell=True)
                f = open ('text', 'w')
                for i in branch1:
                    f.write (i + '\n')
                f.close ()
                subprocess.call ('VAR1="cat text"', shell=True)
                subprocess.call ('git checkout $VAR1', shell=True)
                subprocess.call ('git merge --squash $VAR1', shell=True)
                subprocess.call ('rm -rf text', shell=True)
                subprocess.call ("notify-send 'complete! ))'", shell=True)














