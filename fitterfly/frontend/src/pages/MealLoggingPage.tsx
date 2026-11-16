import { Camera, CheckCircle2, RefreshCw, ShieldAlert, Upload } from "lucide-react";
import { useEffect, useMemo, useState } from "react";

import MealEstimateEditor from "../components/MealEstimateEditor";
import { analyzeMealPhoto, listMealLogs, saveMealLog, type MealEstimate, type MealItem, type MealLog } from "../services/meals";

export default function MealLoggingPage() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [estimate, setEstimate] = useState<MealEstimate | null>(null);
  const [items, setItems] = useState<MealItem[]>([]);
  const [logs, setLogs] = useState<MealLog[]>([]);
  const [status, setStatus] = useState("");
  const [error, setError] = useState("");
  const [isBusy, setIsBusy] = useState(false);

  const totals = useMemo(
    () => ({
      calories: items.reduce((sum, item) => sum + Number(item.calories || 0), 0),
      carbs: items.reduce((sum, item) => sum + Number(item.carbohydrates_g || 0), 0),
      protein: items.reduce((sum, item) => sum + Number(item.protein_g || 0), 0),
      fat: items.reduce((sum, item) => sum + Number(item.fat_g || 0), 0)
    }),
    [items]
  );

  useEffect(() => {
    void refreshLogs();
  }, []);

  async function refreshLogs() {
    try {
      const mealLogs = await listMealLogs();
      setLogs(mealLogs);
    } catch {
      setLogs([]);
    }
  }

  async function handleAnalyze() {
    if (!selectedFile) {
      setError("Choose a meal photo first.");
      return;
    }

    setIsBusy(true);
    setError("");
    setStatus("Analyzing meal photo...");
    try {
      const result = await analyzeMealPhoto(selectedFile);
      setEstimate(result);
      setItems(result.items);
      setStatus("Estimate ready for review.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not analyze meal photo.");
      setStatus("");
    } finally {
      setIsBusy(false);
    }
  }

  async function handleSave() {
    if (!estimate || items.length === 0) {
      setError("Analyze and confirm at least one food item before saving.");
      return;
    }

    setIsBusy(true);
    setError("");
    setStatus("Saving confirmed meal log...");
    try {
      await saveMealLog(estimate, items);
      await refreshLogs();
      setStatus("Confirmed meal log saved.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not save meal log.");
      setStatus("");
    } finally {
      setIsBusy(false);
    }
  }

  return (
    <main className="app-shell">
      <section className="hero-band">
        <div>
          <p className="eyebrow">Fitterfly chronic care MVP</p>
          <h1>Meal logging that stays confirmable before it becomes health data.</h1>
        </div>
        <div className="hero-metric">
          <span>Target</span>
          <strong>under 60 sec</strong>
          <small>photo to confirmed log</small>
        </div>
      </section>

      <section className="workflow-grid">
        <div className="upload-panel">
          <div className="section-header">
            <div>
              <h2>Photo intake</h2>
              <p>Upload a meal image and let the mock AI provider estimate nutrition.</p>
            </div>
            <Camera aria-hidden="true" />
          </div>

          <label className="dropzone">
            <Upload aria-hidden="true" />
            <span>{selectedFile ? selectedFile.name : "Choose meal photo"}</span>
            <input
              type="file"
              accept="image/png,image/jpeg,image/webp"
              onChange={(event) => setSelectedFile(event.target.files?.[0] ?? null)}
            />
          </label>

          <button type="button" className="primary-button" onClick={handleAnalyze} disabled={isBusy}>
            {isBusy ? <RefreshCw size={18} className="spin" /> : <Upload size={18} />}
            Analyze meal
          </button>

          {estimate && (
            <div className={estimate.needs_manual_review ? "status warning" : "status success"}>
              {estimate.needs_manual_review ? <ShieldAlert size={18} /> : <CheckCircle2 size={18} />}
              <span>
                Confidence {Math.round(estimate.confidence * 100)}%. {estimate.notes}
              </span>
            </div>
          )}

          {status && <p className="inline-status">{status}</p>}
          {error && <p className="inline-error">{error}</p>}
        </div>

        <div className="summary-panel">
          <h2>Current estimate</h2>
          <div className="macro-grid">
            <Metric label="Calories" value={totals.calories.toFixed(0)} />
            <Metric label="Carbs" value={`${totals.carbs.toFixed(1)}g`} />
            <Metric label="Protein" value={`${totals.protein.toFixed(1)}g`} />
            <Metric label="Fat" value={`${totals.fat.toFixed(1)}g`} />
          </div>
          <button type="button" className="primary-button" onClick={handleSave} disabled={!estimate || isBusy}>
            <CheckCircle2 size={18} />
            Save confirmed meal
          </button>
        </div>
      </section>

      {estimate && <MealEstimateEditor items={items} onChange={setItems} />}

      <section className="history-section">
        <div className="section-header">
          <div>
            <h2>Confirmed meal logs</h2>
            <p>Only reviewed or corrected entries appear here.</p>
          </div>
        </div>
        <div className="log-table" aria-label="Confirmed meal logs">
          <div className="log-row log-heading">
            <span>Meal</span>
            <span>Calories</span>
            <span>Status</span>
          </div>
          {logs.length === 0 ? (
            <p className="empty-state">No confirmed meals yet.</p>
          ) : (
            logs.map((log) => (
              <div className="log-row" key={log.id}>
                <span>{log.items.map((item) => item.name).join(", ")}</span>
                <span>{log.calories}</span>
                <span>{log.confirmation_status}</span>
              </div>
            ))
          )}
        </div>
      </section>
    </main>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div className="metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}
