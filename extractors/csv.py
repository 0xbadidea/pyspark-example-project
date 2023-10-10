import pyspark.sql.functions as F
from pyspark.sql.types import *

# Composable so that we can build up the options
# as per the properties desired.

class CSV:

    def __init__(self, something):
        self.something = something