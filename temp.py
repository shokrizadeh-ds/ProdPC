import os
from jinja2 import Environment, FileSystemLoader

# print(os.getcwd())

jobs024 = ["IINM025Q" "IINM027M", "IINM050Q", "iinm400q", "iinm401q", "iinm402q", "iinm403q", "ninm024q", "ninm025q", "ninm050q", "ninm400q", "ninm401q", "ninm402q", "ninm403q", "tinm024q", "tinm025q", "tinm027m", "tinm050q", "tinm400q", "tinm401q", "tinm402q", "tinm403q"]

path = r'C:\Users\LI2BTL\OneDrive - Industrial Alliance\Documents\Tide Test\Final\OUTPUT\INI OUT\Copied INI\024'

from jinja2 import Environment, FileSystemLoader

Template_file = 'INI024_Template_Jinja.txt'

file_loader = FileSystemLoader('template')

env = Environment(loader=file_loader)

template = env.get_template(Template_file)

# prodpc={'name' : 'NG1Y800M'}
# output = template.render(prodpc=prodpc)

job = {'jb': jobs024}

with open(Template_file, 'r') as f:
    d = f.read()

print(d)