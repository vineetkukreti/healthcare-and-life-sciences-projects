import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import MealLoggingPage from "../src/pages/MealLoggingPage";

describe("MealLoggingPage", () => {
  beforeEach(() => {
    vi.restoreAllMocks();
    vi.stubGlobal(
      "fetch",
      vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
        const url = String(input);
        if (url.includes("/meal-logs/analyze")) {
          return jsonResponse({
            items: [
              {
                name: "Brown rice",
                portion: "1 cup",
                calories: 216,
                carbohydrates_g: 45,
                protein_g: 5,
                fat_g: 2,
                fiber_g: 4
              }
            ],
            total_calories: 216,
            confidence: 0.82,
            notes: "Mock estimate",
            needs_manual_review: false
          });
        }

        if (url.endsWith("/meal-logs") && init?.method === "POST") {
          return jsonResponse({
            id: 1,
            user_id: "demo-user",
            captured_at: new Date().toISOString(),
            source: "corrected_ai",
            items: JSON.parse(String(init.body)).items,
            calories: 216,
            carbohydrates_g: 45,
            protein_g: 5,
            fat_g: 2,
            fiber_g: 4,
            ai_confidence: 0.82,
            confirmation_status: "corrected",
            correction_history: [],
            notes: "Mock estimate"
          }, 201);
        }

        return jsonResponse([]);
      })
    );
  });

  it("analyzes and saves a confirmed meal log", async () => {
    render(<MealLoggingPage />);

    const input = document.querySelector("input[type='file']") as HTMLInputElement;
    const file = new File(["fake"], "meal.png", { type: "image/png" });
    fireEvent.change(input, { target: { files: [file] } });
    fireEvent.click(screen.getByRole("button", { name: /analyze meal/i }));

    expect(await screen.findByDisplayValue("Brown rice")).toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: /save confirmed meal/i }));

    await waitFor(() => {
      expect(screen.getByText(/confirmed meal log saved/i)).toBeInTheDocument();
    });
  });
});

function jsonResponse(body: unknown, status = 200) {
  return Promise.resolve(
    new Response(JSON.stringify(body), {
      status,
      headers: { "Content-Type": "application/json" }
    })
  );
}
