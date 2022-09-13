# OS DIRECTORY TRAVAERSAL ALGORITHM
Using pythons built in os.walk function, this file contians a recursive algorithm i created to transverse through a directory tree and viewing all sub-directories and files within said directory.

## Installation

Use the python command:

```bash
python traversal.py
```

## How it works

## 1. Traversing  through a directory tree
Lets say you have a directory tree like this

```txt
+--- test.py
|
+--- [subdir1]
|     |
|     +--- file1a.txt
|     +--- file1b.png
|
+--- [subdir2]
|
+--- file2a.jpeg
+--- file2b.html

```
And need to tranvese through the directory to get where a file is stored or read a particular file:

### Just run:

```python
import os

def tranvese(path):
	....

path = "C:/Your/directory/name/"

if __name__ == '__main__':
	print(tranvese(path))

```
### The Result: 

```javascript
root_directory:
{
    subdir:{
	file1a.txt: b'/0f/867b/da24', //file in bytestring
	file1b.png: b'/0f/835f/aa3c' 
	},

    subdir2: {
    	file2a.jpeg: b'/0f/7a5f/ba3c',
	file2b.html: b'/0f/ad2f/cb3c',
        },
    test.py: b'/0ffc/aaf2f/cec3c'
}
```

## 2. Copying a directory tree to another directory by traversing.

Lets say you needed to copy an entire directory tree to another directory in your python program.

### Run
```python
import os


def traverse(path:str):
    ....

    return dict


def create_traveral(hash:dict, destination_dir:str):
    ....

path = "C:/Your/directory/path/"

destination_dir = "C:/Your/destination_directory/path/"

if __name__ == '__main__':
    create_traveral(traverse(path), destination_dir)

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


Please make sure to update tests as appropriate.


## Contact Information

Email: wiizzydreadmill@gmail.com

Linkedin Profile: https://www.linkedin.com/in/wisdomdakoh/

Made with ❤️ By Wisdom Dakoh
