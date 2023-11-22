#!/usr/bin/env python3
import os

commit_amount = int(input("Enter how many commits you want infinitely made: "))

while True:
    for i in range(commit_amount):
        os.system(f'git commit --allow-empty -m "Commit {i} of {commit_amount}"')
    os.system("git push")
