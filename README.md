# PyJSONUtils

A Python library for using JSON files.

# Usage

To open a file:

```py
from pyjsonutils import pyjsonutils
pyjsonutils.open_file_as_dict("file_path.json")
```

To write to a file:

```py
from pyjsonutils import pyjsonutils
pyjsonutils.write_dict_to_file(dictionary, "file_path.json")
```

To update a JSON file:

```py
from pyjsonutils import pyjsonutils
pyjsonutils.update_json_file("file_path.json")
```

Find the first key having a given value:

```py
from pyjsonutils import pyjsonutils
pyjsonutils.find_key_from_value(dictionary, value)
```

Create a default value for a key if the key does not exist:

```py
from pyjsonutils import pyjsonutils
pyjsonutils.create_default_if_key_not_there(dictionary, key, default_value)
```


