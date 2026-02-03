from fastapi import FastAPI
from .generator import generate_event
from .writer import write_event

app = FastAPI()


@app.post("/produce")
def produce_event():
    event = generate_event()
    write_event(event.model_dump())
    return {"status": "event produced", "event_id": event.event_id}
