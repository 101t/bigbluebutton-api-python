# BigBlueButton Python API

Python wrapper for BigBlueButton api, more information about BigBlueButton api can be found [here](http://docs.bigbluebutton.org/dev/api.html 'API doc').

## Installation
The project has been uploaded to pypi, and you can view the library from [here](https://pypi.org/project/bigbluebutton-api-python/ 'pypi'). You can simply download the library by
```shell
pip install bigbluebutton_api_python
```

You can also install the latest from this repo with
```shell
pip install git+git://github.com/101t/bigbluebutton-api-python.git
```


## Example
Example to use the library:
```python
from bigbluebutton_api_python import BigBlueButton

b = BigBlueButton('your BBB server url', 'your server credential')

# get api version
print(b.get_api_version().get_version())
```
## Others Example

```python
from bigbluebutton_api_python import BigBlueButton

b = BigBlueButton('your BBB server url', 'your server credential')

#params
dict = { 'moderatorPW':'pw' }
#use create meeting
print(b.create_meeting ('room',params=dict))
#get info
print(b.get_meeting_info('room'))
#get url
print(b.get_join_meeting_url('user','fake2', 'pw'))
```
More Docs [here](https://www.pydoc.io/pypi/bigbluebutton-api-python-0.0.2/autoapi/bigbluebutton/index.html).

