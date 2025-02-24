from fastapi import FastAPI
from technology.main import run_workflow
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Message": "Hello World"}


@app.get("/news-summary")
def get_all_summary():
    try:
        cards = []
        categories = [
            "technology",
            "politics",
            "entertainment",
            "sports",
            "health",
            "business",
        ]
        for category in categories:
            summary, article = run_workflow(category)
            if summary is None or article is None:
                raise Exception("Valid article not found for category " + category)
            card = {
                "summary": summary,
                "headline": article[0],
                "source": article[2],
                "url": article[1],
                "image": article[3],
                "category": category,
            }
            cards.append(card)

        return cards

    except Exception as e:
        print("Error running workflow:", e)


@app.get("/news-summary/technology")
def get_tech_summary():
    try:
        summary, article = run_workflow()
        return {"summary": summary, "article": article}
    except Exception as e:
        return {"error": f"Error running workflow: {e}"}
