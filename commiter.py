#!/usr/bin/env python3
import os

commit_amount = int(input("Enter how many commits you want infinitely made: "))

if commit_amount > 50000:
    print("No! That takes too long to do. Maximum commit amount is fifty thousand, rerun this file and try again.")
else:
    while True:
        for i in range(commit_amount):
            os.system(f'git commit --allow-empty -m "Commit {i} of {commit_amount}"')
        os.system("git push")
