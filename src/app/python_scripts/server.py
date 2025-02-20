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
        summary, article = run_workflow()
        if summary is None or article is None:
            raise Exception("Valid article not found")
        tech_card = {
            "summary": summary,
            "headline": article[0],
            "source": article[2],
            "url": article[1],
            "image": article[3],
            "category": "technology",
        }

        placeholders = [
            {
                "headline": "Placeholder Politics",
                "summary": "This is a placeholder for Politics news.",
                "source": "Placeholder Source",
                "url": "",
                "image": "/placeholder.svg?height=200&width=300",
                "category": "politics",
            },
            {
                "headline": "Placeholder Entertainment",
                "summary": "This is a placeholder for Entertainment news.",
                "source": "Placeholder Source",
                "url": "",
                "image": "/placeholder.svg?height=200&width=300",
                "category": "entertainment",
            },
            {
                "headline": "Placeholder Sports",
                "summary": "This is a placeholder for Sports news.",
                "source": "Placeholder Source",
                "url": "",
                "image": "/placeholder.svg?height=200&width=300",
                "category": "sports",
            },
            {
                "headline": "Placeholder Health",
                "summary": "This is a placeholder for Health news.",
                "source": "Placeholder Source",
                "url": "",
                "image": "/placeholder.svg?height=200&width=300",
                "category": "health",
            },
        ]

        # Return an array with the tech card first, then the placeholder cards.
        return [tech_card] + placeholders
    except Exception as e:
        print("Error running workflow:", e)
        return {"error": f"Error running workflow: {e}"}


@app.get("/news-summary/technology")
def get_tech_summary():
    try:
        summary, article = run_workflow()
        return {"summary": summary, "article": article}
    except Exception as e:
        return {"error": f"Error running workflow: {e}"}
