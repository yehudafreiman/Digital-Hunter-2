from fastapi import FastAPI
from dal import SqlQueries

app = FastAPI()
conn = SqlQueries()

@app.get("/")
def health():
    return {"fast api is running"}

@app.get("/shifting_quality_targets")
def get_shifting_quality_targets():
    return conn.shifting_quality_targets()

@app.get("/analysis_of_collection_sources")
def get_analysis_of_collection_sources():
    return conn.analysis_of_collection_sources()

@app.get("/finding_new_targets")
def get_finding_new_targets():
    return conn.finding_new_targets()

@app.get("/identifying_targets_that_have_arisen")
def get_identifying_targets_that_have_arisen():
    return conn.identifying_targets_that_have_arisen()

# RuntimeError: Cannot create a GUI FigureManager outside the main thread using the MacOS backend.
# Use a non-interactive backend like 'agg' to make plots on worker threads.
@app.get("/visualization_of_target_trajectory")
def get_visualization_of_target_trajectory():
    return conn.visualization_of_target_trajectory()

@app.get("/analysis_of_escape_patterns_after_an_attack")
def get_analysis_of_escape_patterns_after_an_attack():
    return conn.analysis_of_escape_patterns_after_an_attack()

@app.get("/finding_meetings_between_quality_goals_and_unknown_entities")
def get_finding_meetings_between_quality_goals_and_unknown_entities():
    return conn.finding_meetings_between_quality_goals_and_unknown_entities()





