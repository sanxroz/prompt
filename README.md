# Just Prompt

Generate your own prompts with Additive Prompting made by @nickfloats, this app is based on Flask, HTML, Javascript and CSS

Take your prompts to the next level now!!

Check the [demo](https://just-prompt.vercel.app/)

![Just Code](./api/static/Prompt.png)

## Contact

Feel free to reach me on [Twitter](https://twitter.com/SanxRoz)

I'd love to see what you build with this code - Looking forward to what you build!!!

## How it Works

Just ask me provides a simple, minimal and fully functional chat that you can use to build your own AI app powered by OpenAI.

Just plug and play, it has everything you need to start deploying.

To change the interface go to `api/templates/home.html`.

To modify your prompt or API go to `api/index.py`.

## Running Locally

**1. Clone Repo**

```bash
git clone https://github.com/SanxRoz/prompt.git
```

**2. Install Dependencies**

```bash
pip install requirements.txt
```

**3. Provide OpenAI API Key**

Create a .env.local file in the root of the repo with your OpenAI API Key:

```bash
OPENAI_API_KEY=<YOUR_KEY>
```

**4. Run App**

```bash
cd api
python index.py
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/import?s=https%3A%2F%2Fgithub.com%2FSanxRoz%2Fask&hasTrialAvailable=1&showOptionalTeamCreation=false&project-name=just-ask&framework=other&totalProjects=1&remainingProjects=1)
