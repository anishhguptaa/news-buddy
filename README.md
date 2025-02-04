
# News Buddy

This project uses CrewAI to orchestrate a sophisticated News Article Generator. It fetches latest news and advancements on the given topic and writes a professoinal news article. You can even download the generated file to share it with your connections, by using the given streamlit UI.

## Stack used

- `CrewAI` for orchestration.
- `Gemini AI` for LLM
- `Serper.dev` for finding and validating news data
## How to use

- Clone the repo

```bash
git clone https://github.com/anishhguptaa/news-buddy.git
cd news-buddy
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Create `.env` file. Add `SERPAPI_KEY` and `GOOGLE_API_KEY`

```bash
cp .env.example .env
```

- You can either run the python code via terminal or you can interact using the streamlit UI. Example:

```bash
python run.py
```

OR

```bash
streamlit run app.py
```
