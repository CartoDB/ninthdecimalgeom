# Ninth Decimal transform polygon geom

## Usage:

This tool is for repairing Ninth Decimal geometries that were created with a web tool they use for drawing polygon geometries. These geometries have latitude, longitude pairs and this tool aims to ingest those files as a .csv and create a proper Well-Known Text (WKT) field and then import into Carto using the Import API. 

### Testing:
You can test this application with this data: [https://github.com/CartoDB/ninthdecimalgeom/blob/master/data/example.csv](https://github.com/CartoDB/ninthdecimalgeom/blob/master/data/example.csv)

![img/screenshot.png](img/screenshot.png)


<!--Assuming there is a .carto file called `my_carto_file.carto` that came as the result of exporting a visualization with (at least) one layer that came from dataset `customers` and another layer that came from a `providers` dataset, you can replace those datasets with `customers_new` and `providers_new` as follows:

```python
from dotcarto import DotCartoFile

carto_file = DotCartoFile("my_carto_file.carto", "https://my_carto_account.carto.com/api/", "my_api_key")

carto_file.replace_dataset("customers", "customers_new")
carto_file.replace_dataset("providers", "providers_new")

carto_file.get_new("my_new_carto_file.carto")
```

The `DotCarto` object can also be initialized with a file-like object.

If no file name is passed to the `get_new` method, a `StringIO` object will be returned, instead of an actual file being created.-->

<!--## Caveats

* `customers_new` and `providers_new` must be existing datasets on the CARTO account at the time of generating the new .carto file
* `customers_new` and `providers_new` must have the same structure as `customers` and `providers`, otherwise the visualization will not render.
* When the new .carto file is uploaded, if `customers_new` and `providers_new` exist on the target CARTO account, they will be respected; if not, they will be created alongside with the visualization.-->

## Web UI

You can run a nice web interface to replace datasets on a .carto file by running:

```
$ honcho start
```

And then pointing your browser to `http://localhost:5000`
