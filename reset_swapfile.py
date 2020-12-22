#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


def reset_swapfile(size_file=2048):
    '''
    If swapfile is already registered in /etc/fstab, then run the program.
    If swapfile is not registered, then MANDATORY!
    Before starting the program in the console, execute:
    sudo nano /etc/fstab

    at the end of the fstab file insert the line:
    /swapfile none swap sw 0 0

    Running the program:
    python3 reset_swapfile.py 1024

    1024 - the size of the created swapfile, by default 2048
    myname = '446d69747269657620566173696c79205061766c6f76696368'
    myemail = '646976696b733230303840676d61696c2e636f6d'
    '''

    commans = ['sudo -S swapoff -a',
               'sudo -S dd if=/dev/zero of=/swapfile bs=1M status=progress count=' + str(size_file),
               'sudo -S mkswap /swapfile',
               'sudo -S chmod 600 /swapfile',
               'sudo -S swapon /swapfile',
               'sudo -S swapon --show',
               'free -h']
    for command in commans:
        print(command)
        res = subprocess.run(command.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(res)


if __name__ == '__main__':
    reset_swapfile()
