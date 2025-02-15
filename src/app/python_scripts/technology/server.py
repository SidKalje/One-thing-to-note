from fastapi import FastAPI
from main import run_workflow

app = FastAPI()


app.get("/")


def read_root():
    return {"Hello": "World"}


@app.get("/news-summary/technology")
def get_tech_summary():
    try:
        summary, article = run_workflow()
        return {"summary": summary, "article": article}
    except Exception as e:
        return {"error": f"Error running workflow: {e}"}
