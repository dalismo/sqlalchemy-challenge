import numpy as np
import pandas as pd
import datetime as dt

from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
session = Session(engine)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# view all the classes that automap found
Base.classes.keys()

#Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__)

# #Define the routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
#################################################
# Flask Routes
#################################################
# Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary 
# using date as the key and prcp as the value.
# Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).

prior_year = dt.date(2017,8,23) - dt.timedelta(365)
@app.route("/api/v1.0/precipitation")
def precipitation():
    p_results = session.query(Measurement.date, func.sum(Measurement.prcp)).group_by(Measurement.date).\
    order_by(Measurement.id.desc()).limit(365).all()
    p_results_dict = {}
    for date, prcp in p_results:
        if prcp !=None:
            p_results_dict.setdefault(date, []).append(prcp)

    return jsonify(p_results_dict)

@app.route("/api/v1.0/stations")
def stations():
    station_list = session.query(Station.station).all()
    stations = list(np.ravel(station_list))

    return jsonify(stations)



# Dictionary of TOBS Data
    # """Return a list of dates and tobs"""
    # """Query for the dates and temperature observations from the last year.
    # Convert the query results to a Dictionary using date as the key and tobs as the value.
    # Return the JSON representation of your dictionary."""




if __name__ == '__main__':
    app.run(debug=True)