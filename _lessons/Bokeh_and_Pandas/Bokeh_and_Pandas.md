---
layout: page
title: Visualizing Data with Bokeh and Pandas
description: Programming Historian Lesson on using Bokeh and Panda libraries to visualize .csv data
---

# Visualizing Data with Bokeh and Pandas

## Source

[https://programminghistorian.org/en/lessons/visualizing-with-bokeh] (https://programminghistorian.org/en/lessons/visualizing-with-bokeh) 

## Reflection

Boken is a library that helps visualize a dataset given in a csv file in a graph format. It offers functions that help aggregate, filter, and sub-sample raw data. In this lesson, I visualize a given data set from the Theater History of Operations Reports about aerial bombing operations during WWII through plotted points, categorical data as bar graphs, and plotted coordinates on a map. With Pandas to process and read the .csv data, the Bokeh library easily shows this data in graph form as an image either directly in Jupyter Notebooks or as an HTML file.

This lesson was straightforward and easy to follow. There were a couple of errors in the provided code, but they were easily fixed based on the explanations given in the lesson. The main issue I had was with the final section of the lesson with plotting points on the map. For whatever reason, the coordinates were output incorrectly, maybe from how I filtered the data. However, the overall process wasn’t too difficult to follow, and the functions in the Bokeh library are useful and their purposes are easy to understand. 

A key point I learned in this lesson was the importance and usefulness of filtering data. In order for a dataset to be more legible, filtering the data is necessary to focus on specific data. Filtering based on keywords was much easier than I expected, although somewhat time-consuming. I also learned how to aggregate data to be categorical, which can be helpful depending on what kind of information you aim to present in the visualizations. I found the spatial data section to not be as useful as using a tool such as ArcGIS, but is definitely much simpler to implement, and may be ideal for smaller representations of geographical data.


## Code

For all the code in their individual files and the HTML files of each graph, please see this folder in my repo :)
Link: [Bokeh_and_Pandas](https://github.com/minnie91863/intro-dh-portfolio/tree/gh-pages/_lessons/Bokeh_and_Pandas)

### Your First Plot


```python
from bokeh.plotting import figure, output_file, show

output_file('my_first_graph.html')

x = [1, 3, 5, 7]
y = [2, 4, 6, 8]

p = figure()

p.circle(x, y, size = 10, color = 'red', legend_field = 'circle')
p.line(x, y, color = 'blue', legend_field = 'line')
p.triangle(y, x, color = 'gold', size = 10, legend_field = 'triangle')

p.legend.click_policy = 'hide'

show(p)
```

Photo of Graph

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-12%20124450.png)

### Loading Data in Pandas


```python
import pandas as pd

df = pd.read_csv('thor_wwii.csv')
print(df)

df.columns.tolist()
```


### The Bokeh ColumnDataSource


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('columndatasource_example.html')

df = pd.read_csv('thor_wwii.csv')

sample = df.sample(50)
source = ColumnDataSource(sample)

p = figure()
p.circle(x = 'TOTAL_TONS', y = 'AC_ATTACKING', 
        source = source, 
        size = 10, color = 'green')

p.title.text = 'Attacking Raircraft and Munitions Dropped'
p.xaxis.axis_label = 'Tons of Munitions Dropped'
p.yaxis.axis_label = 'Number of Attacking Aircraft'

hover = HoverTool()
hover.tooltips = [
    ('Attack Date', '@MSNDATE'),
    ('Attacking Aircraft', '@AC_ATTACKING'),
    ('Tons of Munitions', '@TOTAL_TONS'),
    ('Type of Aircraft', '@AIRCRAFT_NAME')
]
p.add_tools(hover)

show(p)
```

Photo of Graph
![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-12%20131428.png)

### Categorical Data and Bar Charts: Munitions Dropped by Country


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
output_file('munitions_by_country.html')

df = pd.read_csv('thor_wwii.csv')

grouped = df.groupby('COUNTRY_FLYING_MISSION')[['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG']].sum()

print(grouped)

#plotting data to scale it down
grouped = grouped / 1000

source = ColumnDataSource(grouped)
countries = source.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range = countries)

color_map = factor_cmap(field_name = 'COUNTRY_FLYING_MISSION', palette = Spectral5, factors = countries)
p.vbar(x = 'COUNTRY_FLYING_MISSION',
      top = 'TOTAL_TONS',
      source = source,
      width = 0.7,
      color = color_map)
p.title.text = 'Munitions Dropped by Allied Country'
p.xaxis.axis_label = 'Country'
p.yaxis.axis_label = 'Kilotons of Munitions'

hover = HoverTool()
hover.tooltips = [
    ("Totals", '@TONS_HE High Explosive / @TONS_IC Incendiary / @TONS_FRAG Fragmentation')
]

hover.mode = 'vline'

p.add_tools(hover)

show(p)
```

Photo of Graph

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-13%20111346.png)

### Stacked Bar Charts and Sub-sampling Data: Types of Munitions Dropped by Country


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('types_of_munitions.html')

df = pd.read_csv('thor_wwii.csv')

filter = df['COUNTRY_FLYING_MISSION'].isin((
    'USA',
    'GREAT BRITAIN'
))

df[filter]

grouped = df.groupby('COUNTRY_FLYING_MISSION')[
    'TONS_IC',
    'TONS_FRAG',
    'TONS_HE'
].sum()

grouped = grouped / 1000

source = ColumnDataSource(grouped)
#countries = source.data['COUNTRY_FLYING_MISSION'].tolist()
countries = ['USA', 'GREAT BRITAIN']
p = figure(x_range = countries)

p.vbar_stack(
            stackers = ['TONS_HE', 'TONS_FRAG', 'TONS_IC'],
            x = 'COUNTRY_FLYING_MISSION',
            source = source,
            legend_label = ['High Explosive', 'Fragmentation', 'Incendiary'],
            width = .5,
            color = Spectral3
            )

p.title.text = 'Types of Munitions Dropped by Allied Country'
p.legend.location = 'top_left'

p.xaxis.axis_label = 'Country'
p.xgrid.grid_line_color = None

p.yaxis.axis_label = 'Kilotons of Munitions'

show(p)
```

Photo of Graph

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-13%20113007.png)

### Time-Series and Annotiations: Bombing Operations over Time


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('simple_timeseries_plot.html')

df = pd.read_csv('thor_wwii.csv')

df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format = '%m/%d/%Y')

grouped = df.groupby(pd.Grouper(
                    key = 'MSNDATE',
                    freq = 'M'
                                )
                    )[
                        'TOTAL_TONS',
                        'TONS_IC',
                        'TONS_FRAG'
                    ].sum()

grouped = grouped / 1000

source = ColumnDataSource(grouped)

p = figure(x_axis_type = 'datetime')

p.line(
        x = 'MSNDATE',
        y = 'TOTAL_TONS',
        line_width = 2,
        source = source,
        legend_label = 'All Munitions'
)

p.line(
        x = 'MSNDATE',
        y = 'TONS_FRAG',
        line_width = 2,
        source = source,
        color = Spectral3[1],
        legend_label = 'Fragmentation'
)

p.line(
        x = 'MSNDATE',
        y = 'TONS_IC',
        line_width = 2,
        source = source,
        color = Spectral3[2],
        legend_label = 'Incendiary'
)

p.yaxis.axis_label = 'Kilotons of Munitions Dropped'

p.title.text = 'A Time-Series Plot with Data Resampled to Months'
p.legend.location = 'top_left'

show(p)
```

Photo of Graph

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-12%20124450.png)

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-13%20115004.png)

### Annotating Trends in Plots


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from datetime import datetime
from bokeh.palettes import Spectral3
output_file('eto_operations.html')

df = pd.read_csv('thor_wwii.csv')

filter = df['THEATER'] == 'ETO'
df = df[filter]

df['MSNDATE'] = pd.to_datetime(
                                df['MSNDATE'],
                                format = '%m/%d/%Y')
group = df.groupby(
                    pd.Grouper(
                                key = 'MSNDATE',
                                freq = 'M')
                    )[
                        'TOTAL_TONS',
                        'TONS_IC',
                        'TONS_FRAG'
                    ].sum()

group = group / 1000

source = ColumnDataSource(group)

p = figure(x_axis_type = 'datetime')

p.line(
        x = 'MSNDATE',
        y = 'TOTAL_TONS',
        line_width = 2,
        source = source,
        legend_label = 'All Munitions'
)

p.line(
        x = 'MSNDATE',
        y = 'TONS_FRAG',
        line_width = 2,
        source = source,
        color = Spectral3[1],
        legend_label = 'Fragmentation'
)

p.line(
        x = 'MSNDATE',
        y = 'TONS_IC',
        line_width = 2,
        source = source,
        color = Spectral3[2],
        legend_label = 'Incendiary'
)

p.title.text = 'European Theater of Operations'
p.yaxis.axis_label = 'Kilotons of Munitions Dropped'
p.legend.location = 'top_left'

from bokeh.models import BoxAnnotation

box_left = pd.to_datetime('6-6-1944')
box_right = pd.to_datetime('16-12-1944')
infer_datetime_format = True

box = BoxAnnotation(
                    left = box_left,
                    right = box_right,
                    line_width = 1,
                    line_color = 'black',
                    line_dash = 'dashed',
                    fill_alpha = .2,
                    fill_color = 'orange'
                    )
p.add_layout(box)

show(p)
```

Photo of Graph

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-13%20120447.png)

### Spatial Data: Mapping 


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import layout
from bokeh.palettes import Spectral3
from bokeh.tile_providers import get_provider
from pyproj import Transformer
output_file('mapping_targets.html')

def LongLat_to_EN(long, lat):
    try:
        transformer = Transformer.from_crs('epsg:4326',
                                          'epsg:3857')
        easting, northing = transformer.transform(long, lat)
        return easting, northing
    except:
        return None, None
    
df = pd.read_csv("thor_wwii.csv")

df['E'], df['N'] = zip(
                *df.apply(
                        lambda x: LongLat_to_EN(x['TGT_LONGITUDE'], x['TGT_LATITUDE']),
                        axis = 1
                        )
                    )
#         *df.apply(lambda x: LongLat_to_EN(x['TGT_LONGITUDE'], x['TGT_LATITUDE']), axis=1)))

grouped = df.groupby(['E', 'N'])[
                    ['TONS_IC', 'TONS_FRAG']
                                ].sum().reset_index()

filter = grouped['TONS_FRAG'] != 0
grouped = grouped[filter]

source = ColumnDataSource(grouped)

left = -2150000
right = 18000000
bottom = -5300000
top = 11000000

p = figure(
            x_range = Range1d(left, right),
            y_range = Range1d(bottom, top)
          )

provider = get_provider('CARTODBPOSITRON')
p.add_tile(provider)
p.circle(
        x = 'E',
        y = 'N',
        source = source,
        line_color = 'grey',
        fill_color = 'yellow'
        )
p.axis.visible = False

show(p)
```

Photo of Graph

![png](Bokeh_and_Pandas_Photos/Screenshot%202022-12-13%20135057.png)
