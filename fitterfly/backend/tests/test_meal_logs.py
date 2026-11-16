def test_analyze_meal_endpoint(client):
    response = client.post(
        "/meal-logs/analyze",
        files={"image": ("idli.png", b"fake-image", "image/png")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["items"]
    assert body["total_calories"] > 0
    assert body["needs_manual_review"] is False


def test_create_and_list_confirmed_meal_log(client):
    payload = {
        "user_id": "demo-user",
        "source": "corrected_ai",
        "ai_confidence": 0.82,
        "confirmation_status": "corrected",
        "notes": "User reduced rice portion.",
        "correction_history": [{"field": "portion", "from": "1 cup", "to": "1/2 cup"}],
        "items": [
            {
                "name": "Brown rice",
                "portion": "1/2 cup",
                "calories": 108,
                "carbohydrates_g": 22.5,
                "protein_g": 2.5,
                "fat_g": 1,
                "fiber_g": 2,
            }
        ],
    }

    create_response = client.post("/meal-logs", json=payload)
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["calories"] == 108
    assert created["confirmation_status"] == "corrected"

    list_response = client.get("/meal-logs", params={"user_id": "demo-user"})
    assert list_response.status_code == 200
    logs = list_response.json()
    assert len(logs) == 1
    assert logs[0]["items"][0]["portion"] == "1/2 cup"
