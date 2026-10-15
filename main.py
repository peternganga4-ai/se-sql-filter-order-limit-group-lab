import pandas as pd
import sqlite3


##### Part I: Basic Filtering #####

conn1 = sqlite3.connect('planets.db')

pd.read_sql("""
    SELECT *
    FROM planets;
""", conn1)


# STEP 1: Select planets that have no moons
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
""", conn1)


# STEP 2: Select the name and mass of planets with seven-letter names
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
""", conn1)


##### Part 2: Advanced Filtering #####


# STEP 3: Select planets with a mass less than or equal to 1.00
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
""", conn1)


# STEP 4: Select planets with at least one moon and mass below 1.00
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
""", conn1)


# STEP 5: Select planets whose color contains the word blue
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
""", conn1)


##### Part 3: Ordering and Limiting #####

conn2 = sqlite3.connect('dogs.db')

pd.read_sql("""
    SELECT *
    FROM dogs;
""", conn2)


# STEP 6: Select hungry dogs and order them by age
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)

# Convert missing names from NaN to None for the tests
df_hungry = df_hungry.astype(object).where(
    pd.notna(df_hungry), None
)


# STEP 7: Select hungry dogs aged between 2 and 7
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
""", conn2)


# STEP 8: Select the four oldest dogs and order them by breed
# STEP 8: Select the four oldest dogs and order them by breed
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM (
        SELECT name, age, breed
        FROM dogs
        ORDER BY age DESC
        LIMIT 4
    )
    ORDER BY age DESC;
""", conn2)


##### Part 4: Aggregation #####

conn3 = sqlite3.connect('babe_ruth.db')

pd.read_sql("""
    SELECT *
    FROM babe_ruth_stats;
""", conn3)


# STEP 9: Count the number of years in the statistics
df_ruth_years = pd.read_sql("""
    SELECT COUNT(*) AS years
    FROM babe_ruth_stats;
""", conn3)


# STEP 10: Calculate Babe Ruth's total home runs
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_home_runs
    FROM babe_ruth_stats;
""", conn3)


##### Part 5: Grouping and Aggregation #####


# STEP 11: Count the number of years played for each team
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY team ASC;
""", conn3)


# STEP 12: Calculate average at-bats for each team
# STEP 12: Calculate average at-bats for each team
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY average_at_bats DESC;
""", conn3)


# Close database connections
conn1.close()
conn2.close()
conn3.close()