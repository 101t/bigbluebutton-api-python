# BigBlueButton Python API

Python wrapper for BigBlueButton api, more information about BigBlueButton api can be found [here](http://docs.bigbluebutton.org/dev/api.html 'API doc').

## Installation
The project has been uploaded to pypi, and you can view the library from [here](https://pypi.org/project/bigbluebutton-api-python/ 'pypi'). You can simply download the library by
```
pip install bigbluebutton_api_python
```

## Example
Example to use the library:
```
from bigbluebutton_api_python import BigBlueButton

b = BigBlueButton('your BBB server url', 'your server credential')

# get api version
print(b.get_api_version().get_version())
```
