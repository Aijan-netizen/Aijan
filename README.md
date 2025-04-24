# NINTH ASSIGNMENT
# 3D Shape Abstraction in Python

## 📌 Objective
This project demonstrates the use of **abstraction** and **polymorphism** in Python through an abstract base class `Shape3D` and its subclasses representing 3D shapes: `Sphere`, `Cylinder`, and `Cube`.

## 🧱 Implemented Classes

### Shape3D (Abstract)
- `surface_area()` – abstract
- `volume()` – abstract

### Sphere
- Constructor: `__init__(radius)`
- Surface Area: `4 * π * r²`
- Volume: `(4/3) * π * r³`

### Cylinder
- Constructor: `__init__(radius, height)`
- Surface Area: `2 * π * r * (r + h)`
- Volume: `π * r² * h`

### Cube
- Constructor: `__init__(side_length)`
- Surface Area: `6 * a²`
- Volume: `a³`

## 🔁 Random Shape Generator
Generates a list of 10 random shapes with:
- Radius: 1–10
- Height: 5–20
- Side Length: 1–10

## 💻 Example Output

```
![Screenshot](https://github.com/Aijan-netizen/Aijan/blob/oop-9-assignment/images/Capture.PNG) 
