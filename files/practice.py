import json
import subprocess

# my_bytes_value = b'[{\'Date\': \'2016-05-21T21:35:40Z\', \'CreationDate\': \'2012-05-05\', \'LogoType\': \'png\', \'Ref\': 164611595, \'Classe\': [\'Email addresses\', \'Passwords\'],\'Link\':\'http://some_link.com\'}]'
my_bytes_value = subprocess.check_output('echo "{\'key1\': \'val1\', \'key2\': \'val2\'}"', shell = True) 
# Decode UTF-8 bytes to Unicode, and convert single quotes 
# to double quotes to make it valid JSON
my_json = my_bytes_value.decode('utf8').replace("'", '"')
print(my_json)
print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
print(type(data))
str = json.dumps(data, indent=4, sort_keys=True)
print(str)
