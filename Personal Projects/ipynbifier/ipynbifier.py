"""
Robert Davis
08/26/2021
"""

import json
from random import randint

def generate_base_ipynb(file_name):
    "Generates a blank .ipynb-styled dictionary. Input the file name."

    ipynb = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {
                "name": f"{file_name}.ipynb",
                "provenance": [],
                "collapsed_sections": []
            },
            "kernelspec": {
                "name": "python3",
                "display_name": "Python 3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "cells": []
    }

    return ipynb

def write_file(ipynb, path_output = ''):
    "Writes a ipynb dictionary into a file."

    file_text = json.dumps(ipynb, indent=2)
    file_path = path_output
    if path_output != '':
        file_path += '/'
    file_path += ipynb["metadata"]["colab"]["name"]

    file = open(file_path, 'w')
    file.write(file_text)
    file.close()

    return True

def _generate_id():
    "Generates a random 12 character ID that hopefull will work in a ipynb."

    valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'
    id12dig = ''

    for x in range(12):
        id12dig += valid_characters[randint(0, len(valid_characters)-1)]

    return id12dig

def format_code(string):
    "Adds an additional forward slash in the code portion of code lines."

    new_str = ''
    for char in string:
        # if char == '\\':
        #     new_str += '\\'
        new_str += char
    
    new_str += '\n'

    return new_str

def add_code_cell(ipynb, code_list):
    "Adds a code cell to your ipynb. Pass in the ipynb and a list of code."

    counter = 0
    for x in range(len(code_list)):
        if code_list[-(x+1)] == '\n':
            counter += 1
        else:
            break
    
    for x in range(counter):
        code_list.pop(-1) 

    code_list[-1] = code_list[-1][:-1]    

    cell = {
        "cell_type": "code",
        "metadata": {
            "id": _generate_id()
        },
        "source": code_list,
        "execution_count": None,
        "outputs": []
    }

    ipynb["cells"].append(cell)

    return ipynb

def write_file(ipynb, path_output = ''):
    "Writes a ipynb dictionary into a file."

    file_text = json.dumps(ipynb, indent=2)
    file_path = path_output
    if path_output != '':
        file_path += '/'
    file_path += ipynb["metadata"]["colab"]["name"]

    file = open(file_path, 'w')
    file.write(file_text)
    file.close()

    return True

def ipynbify(path, output_path, name):
    "Interprets a python file using ipynb notation to transform into a .ipynb"
    #n means new code block
    
    file = open(path, 'r')
    lines = file.read().split('\n')
    file.close()

    ipynb = generate_base_ipynb(name)

    block = []

    for x in lines:
        if x[0:2] == '#n':
            ipynb = add_code_cell(ipynb, block)
            block = []
        else:
            block.append(format_code(x))

    write_file(ipynb, output_path)
    