# 3D Shapes Abstraction Project

## 📚 Objective

This project demonstrates the concept of **abstraction** and **polymorphism** in Python by using an **abstract base class** for 3D shapes. Different shape classes implement methods to calculate **surface area** and **volume** according to their specific formulas.

---

## 🏗️ Project Structure

- **Abstract Base Class: `Shape3D`**
  - Defines the blueprint for 3D shapes.
  - Declares two abstract methods:
    - `surface_area()` – Calculates the surface area.
    - `volume()` – Calculates the volume.

- **Shape Subclasses:**
  - `Sphere`
  - `Cylinder`
  - `Cube`
  - Each subclass:
    - Implements `surface_area()` and `volume()` methods.
    - Has its own constructor with appropriate dimensions.

- **Random Shape Generation:**
  - A list of 10 random 3D shapes is generated.
  - Shapes and their dimensions are randomly selected:
    - **Sphere radius**: 1–10
    - **Cylinder radius**: 1–10, height: 5–20
    - **Cube side length**: 1–10

- **Output:**
  - For each generated shape:
    - Display the shape name.
    - Display its surface area (rounded to two decimal places).
    - Display its volume (rounded to two decimal places).

---

## 🛠️ How It Works

1. The `Shape3D` class (using Python’s `abc` module) enforces that any subclass must implement `surface_area()` and `volume()` methods.
2. The program randomly creates instances of `Sphere`, `Cylinder`, or `Cube` with random dimensions.
3. It then calculates and displays each shape's properties using **polymorphism** — treating different shapes uniformly through their common abstract interface.

---

## 🚀 Requirements

- Python 3.6 or higher
- Standard Libraries: `random`, `math`, `abc`

---

## 📋 Example Output

```
Shape 1: Cylinder
  Surface Area: 565.49
  Volume: 753.98
------------------------------
Shape 2: Sphere
  Surface Area: 201.06
  Volume: 268.08
------------------------------
Shape 3: Cube
  Surface Area: 54.00
  Volume: 27.00
------------------------------
...
```

---

## 🌟 Key Concepts Covered

- Abstract Base Classes (ABC)
- Inheritance and Polymorphism
- Random object generation
- Mathematical calculations for 3D shapes
- Clean and formatted console output

---

