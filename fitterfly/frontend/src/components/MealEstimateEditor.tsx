import { Trash2 } from "lucide-react";

import type { MealItem } from "../services/meals";

type Props = {
  items: MealItem[];
  onChange: (items: MealItem[]) => void;
};

const numericFields: Array<keyof Pick<MealItem, "calories" | "carbohydrates_g" | "protein_g" | "fat_g" | "fiber_g">> = [
  "calories",
  "carbohydrates_g",
  "protein_g",
  "fat_g",
  "fiber_g"
];

export default function MealEstimateEditor({ items, onChange }: Props) {
  function updateItem(index: number, patch: Partial<MealItem>) {
    onChange(items.map((item, itemIndex) => (itemIndex === index ? { ...item, ...patch } : item)));
  }

  function removeItem(index: number) {
    onChange(items.filter((_, itemIndex) => itemIndex !== index));
  }

  function addItem() {
    onChange([
      ...items,
      {
        name: "New item",
        portion: "1 serving",
        calories: 0,
        carbohydrates_g: 0,
        protein_g: 0,
        fat_g: 0,
        fiber_g: 0
      }
    ]);
  }

  return (
    <section className="editor" aria-label="Editable meal estimate">
      <div className="section-header">
        <div>
          <h2>Review meal estimate</h2>
          <p>Confirm the AI result before it becomes part of the care record.</p>
        </div>
        <button type="button" className="secondary-button" onClick={addItem}>
          Add food
        </button>
      </div>

      <div className="food-list">
        {items.map((item, index) => (
          <div className="food-row" key={`${item.name}-${index}`}>
            <label>
              Food
              <input value={item.name} onChange={(event) => updateItem(index, { name: event.target.value })} />
            </label>
            <label>
              Portion
              <input value={item.portion} onChange={(event) => updateItem(index, { portion: event.target.value })} />
            </label>
            {numericFields.map((field) => (
              <label key={field}>
                {fieldLabel(field)}
                <input
                  type="number"
                  min="0"
                  value={item[field]}
                  onChange={(event) => updateItem(index, { [field]: Number(event.target.value) } as Partial<MealItem>)}
                />
              </label>
            ))}
            <button type="button" className="icon-button" aria-label={`Remove ${item.name}`} onClick={() => removeItem(index)}>
              <Trash2 size={18} />
            </button>
          </div>
        ))}
      </div>
    </section>
  );
}

function fieldLabel(field: string) {
  const labels: Record<string, string> = {
    calories: "Cal",
    carbohydrates_g: "Carbs",
    protein_g: "Protein",
    fat_g: "Fat",
    fiber_g: "Fiber"
  };
  return labels[field] ?? field;
}
