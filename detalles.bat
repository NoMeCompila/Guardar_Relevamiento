@echo off
ipconfig > ip.txt
find /i "IPv4" ip.txt > ipriv.txt
del ip.txt