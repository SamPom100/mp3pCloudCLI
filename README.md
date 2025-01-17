# mp3-pcloud-cli Tool
Tool to auto-download songs from Youtube and upload them to pCloud.

# Installing from Pip
`pip install mp3-pcloud-cli`

Project Link: `https://pypi.org/project/mp3-pcloud-cli/`

# Installing from Github
Ensure you have setuptools.

`pip install setuptools`

Run setup.py.

`python setup.py install`

then run `mp3-pcloud-cli` on your Terminal

# `mp3-pcloud-cli` Command Usage
```
    Usage: mp3-pcloud-cli <url> [--help] [--setup]

    Options:
    <url>                Youtube URL to download audio from.
    --help               Show this help message.
    --setup              Set up this mp3-pcloud-cli with the given credentials. 
    --tutorial           Show pCloud setup tutorial.
    
    Setup Usage (see --tutorial for more info):
    --setup <username> <password> <pcloud_folder_id> <pcloud_folder_code> 

    username:            Your pCloud username. 
    password:            Your pCloud password. (stored in plain text so use a dedicated account)
    pcloud_folder_id:    pCloud folder ID network inspection.
    pcloud_folder_code:  pCloud folder code from shared link.
```

# Preview
<img width="778" alt="Screenshot 2024-10-11 at 12 34 15 AM" src="https://github.com/user-attachments/assets/e91dd5ad-df7d-4e4a-8534-b6214f4542a9">
