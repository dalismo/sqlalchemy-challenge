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
last_year = dt.date(2017,8,23) - dt.timedelta(365)
@app.route("/api/v1.0/precipitation")
def precipitation():
    p_results = session.query(Measurement.date, func.sum(Measurement.prcp)).group_by(Measurement.date).\
    order_by(Measurement.id.desc()).limit(365).all()
    p_results_dict = {}
    for date, prcp in p_results:
        if prcp !=None:
            p_results_dict.setdefault(date, []).append(prcp)

    return jsonify(p_results_dict)

# Return a JSON list of stations from the dataset.
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
@app.route("/api/v1.0/tobs")
def tobs():
    observes = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= last_year).all()
    observes_dict = {}
    for date, tobs in observes:
        if tobs !=None:
            observes_dict.setdefault(date, []).append(tobs)
    
    return jsonify(observes_dict)

# Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range
# When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date
# When given the start and the end date, calculate the minimum, average, and maximum obvserved temperature for dates between the start and end date inclusive
# Return a JSONified dictionary of these minimum, maximum, and average temperatures
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def date(start=None, end=None):
    if not end:
        start = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()
        start_sort = list(np.ravel(start))
        return jsonify(start_sort)
    else:
        end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date <= end).all()
        end_sort = list(np.ravel(end))
        return jsonify(end_sort)

if __name__ == '__main__':
    app.run(debug=True)