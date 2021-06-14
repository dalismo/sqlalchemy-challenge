import numpy as np

from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary 
# using date as the key and prcp as the value.
# Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).
@app.route("/api/v1.0/precipitation")
def precip():
