# AquaGuard AI v4.2

AquaGuard AI is an AI-powered water network monitoring system designed for Jordan's water distribution network. It detects and classifies anomalies such as leaks, bursts, and theft, estimates fault location, and visualizes network status through an interactive dashboard.

## Project track

Sustainability / AI for water infrastructure.

## Core idea

The system compares real-time flow and pressure readings against physically expected hydraulic behavior. It then classifies the network state as normal, leak, burst, or theft and presents operational alerts through a live dashboard.

## Main components

- **ML pipeline:** LightGBM, XGBoost, ResNet-MLP, BiLSTM, stacking meta-learner, isotonic calibration, and localization model.
- **Frontend:** React + Vite dashboard with live map, KPIs, telemetry charts, alert log, and offline simulation fallback.
- **Backend:** Flask/Colab/ngrok-ready API structure.
- **Data:** sample CSV files are included for review; full datasets can be placed locally or in Colab when retraining.

## Repository structure

```text
frontend/   React/Vite dashboard
backend/    Flask demo backend and API placeholder
ml/         AquaGuard v4.2 training pipeline
data/       sample train/test data and data notes
docs/       presentation, documentation, and demo-video link placeholder
```

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

If no backend URL is configured, the dashboard runs using offline simulation mode.

## Optional API URL

Create `frontend/.env.local` from `frontend/.env.example`:

```env
VITE_API_URL=https://your-ngrok-url.ngrok-free.app
```

## Run the demo backend

```bash
cd backend
pip install -r ../requirements.txt
python app.py
```

## Run the ML pipeline on Colab

Upload the full dataset files to Colab as:

```text
jordan_v4_train.csv
jordan_v4_test.csv
```

Then run:

```python
!pip install -q lightgbm xgboost scikit-learn pandas numpy matplotlib seaborn joblib torch
exec(open('/content/data/aquaguard_v4_2_model.py').read())
```

## Submission notes

The demo video is intentionally not committed in this lightweight repository package. Upload the video separately and add the link in `docs/demo_video_link.md` or directly in the competition form.

## Team

Change The Future — Amman Arab University.
