# Cognita: AI Math Notepad

Draw a maths problem by hand and Cognita solves it. Inspired by Apple's Math Notes.

Sketch equations, expressions or variable assignments on a canvas and press **Run**. A vision-language model reads your handwriting, solves the problem, and drops the typeset answer onto the canvas, where you can drag it anywhere.

## Features

- **Freehand canvas** with a colour palette
- **Handwriting to LaTeX:** the model turns what you drew into a typeset expression, rendered with MathJax
- **Variables that persist:** write `x = 5` once, and later expressions like `x² + 3` use it
- **Draggable results** placed straight onto the canvas
- **One-click reset** to start over

## Architecture

```
React canvas ──(base64 image + saved variables)──▶ FastAPI /calculate
                                                    │
                                                    ▼
                                          Gemini 1.5 Flash (vision)
                                                    │
        MathJax-rendered result ◀──(expr, result, assign)──┘
```

An earlier version ran **LLaVA-1.5-7B locally with 4-bit quantisation**. That code is still in the backend, commented out, for anyone who wants an offline variant.

## Tech stack

| | |
|---|---|
| **Frontend** | React 18, TypeScript, Vite, Tailwind, Mantine, MathJax, react-draggable |
| **Backend** | FastAPI, Pydantic, Pillow, Uvicorn |
| **Model** | Google Gemini 1.5 Flash (earlier: LLaVA-1.5-7B, 4-bit) |

## Run locally

**Backend**
```bash
cd Cognita/Cognita-be
pip install -r requirements.txt
# add GEMINI_API_KEY to a .env file
python main.py
```

**Frontend**
```bash
cd Cognita/Cognita-fe
npm install
npm run dev
```
