# Installation
Requires Python 3.5 or greater. Install packages using the following command after cloning the repo:

`pip install -r requirements.txt`

A configuration file called *config.ini* is also required in the root directory.  See the example ini file for settings

# Sample Usage
<pre>
>>> from finance import DataModel
from finance import DataModel
>>> test = DataModel()
test = DataModel()
>>> test.show_graph('BCHAIN/ATRCT', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Wait time in minutes')
test.show_graph('BCHAIN/ATRCT', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Wait time in minutes')
>>> test.show_graph('BCHAIN/DIFF', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Difficulty')
test.show_graph('BCHAIN/DIFF', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Difficulty')
</pre>