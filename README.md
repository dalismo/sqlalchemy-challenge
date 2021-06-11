# SQLAlchemy Homework - Surfs Up!

## Before You Begin

1. Create a new repository for this project called `sqlalchemy-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Add your Jupyter notebook, database, and `app.py` to this folder. These will be the main scripts to run for analysis.

4. Push the above changes to GitHub.

![surfs-up.png](Images/surfs-up.png)

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Link Python to the database by creating a SQLAlchemy session.

* **Important** Don't forget to close out your session at the end of your notebook.

### Precipitation Analysis

* Start by finding the most recent date in the data set.

* Using this date, retrieve the average precipitation per day for the previous 12 months. The query should be sorted by date ascending. **Note** you do not pass in the date as a variable to your query.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Plot the results using the DataFrame `plot` method. **NOTE: Your plot will look different from the one below.**

  ![precipitation](Images/precipitation.png)

* Use Pandas to print the summary statistics for the precipitation data. **HINT:** This will be a single line of code.

### Station Analysis

* Design a query to calculate the total number of stations in the dataset.

* Design a query that lists all stations with their corresponding observation count in descending order (observation count corresponds to the number of rows per station).

* Which station id is the most active (i.e., has the greatest number of observations)?

* Calculate the lowest, highest, and average temperature for that station id (i.e., the one with the greatest number of observations).

* **Hint:** You will need to use functions in your queries.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS) for the most active station.

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

* Close out your session.

- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

  * Query the dates and temperature observations of the **most active station** for the most recent 12 months of data.
  
  * Return a JSON list of temperature observations (TOBS) for that year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the minimum, average, and maximum obvserved temperature for dates between the start and end date inclusive.
  
  * Return a JSONified dictionary of these minimum, maximum, and average temperatures.

- - -

## Hints

* Pay very close attention to the requested JSON response format (are we asking for a JSON list or a dictionary? or a list of dictionaries?).

* Remember, a JSON list and dictionary is different from a regular python list and dictionary.

## Rubric

[Unit 10 Rubric - SQLAlchemy Homework - Surfs Up!](https://docs.google.com/document/d/1gT29iMF3avSvJruKpcHY4qovP5QitgXePqtjC6XESI0/edit?usp=sharing)

- - -

## References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
