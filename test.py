from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"message": "DevOps Lab 2025!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
