import { apiRequest } from "./api";

export type MealItem = {
  name: string;
  portion: string;
  calories: number;
  carbohydrates_g: number;
  protein_g: number;
  fat_g: number;
  fiber_g: number;
};

export type MealEstimate = {
  items: MealItem[];
  total_calories: number;
  confidence: number;
  notes: string;
  needs_manual_review: boolean;
};

export type MealLog = {
  id: number;
  user_id: string;
  captured_at: string;
  source: string;
  items: MealItem[];
  calories: number;
  carbohydrates_g: number;
  protein_g: number;
  fat_g: number;
  fiber_g: number;
  ai_confidence: number | null;
  confirmation_status: string;
  correction_history: Record<string, unknown>[];
  notes: string | null;
};

export async function analyzeMealPhoto(file: File): Promise<MealEstimate> {
  const formData = new FormData();
  formData.append("image", file);
  return apiRequest<MealEstimate>("/meal-logs/analyze", {
    method: "POST",
    body: formData
  });
}

export async function saveMealLog(estimate: MealEstimate, items: MealItem[]): Promise<MealLog> {
  return apiRequest<MealLog>("/meal-logs", {
    method: "POST",
    body: JSON.stringify({
      user_id: "demo-user",
      source: "corrected_ai",
      items,
      ai_confidence: estimate.confidence,
      confirmation_status: "corrected",
      correction_history: [
        {
          source: "meal_estimate_editor",
          note: "User confirmed or edited the AI estimate before saving"
        }
      ],
      notes: estimate.notes
    })
  });
}

export async function listMealLogs(): Promise<MealLog[]> {
  return apiRequest<MealLog[]>("/meal-logs?user_id=demo-user");
}
