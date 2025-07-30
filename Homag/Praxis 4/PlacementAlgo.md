# Anforderung
Mittelpunkt der Werkstücke liegt innerhalb der Traverse

# Ablauf
Es wird immer versucht das Werkstück mit Überhang zu greifen, da ein Absetzen mit Schieber langsamer ist.
## Bei Leerer Traverse

### Fall 1 (Normales Teil)
Kann mit viel Überhang gegriffen werden.

1. Prüfung ob Zahl freier Sauggreifer ausreicht (Early Return für Performance)
2. Wahl der Seite zur Einführung in Maschine (Mindestens 170mm? Überhang)
3. Zielposition "X" mit 170 Überhang, "Y" Bündig
4. Griffkraft prüfen
5. Ausreichend -> Überhang vergrößern

Die Schritte 4 und 5 werden beliebig oft ausgeführt um den optimalen Überhang mit $170 < d < \text{MaxBreite}$ zu bestimmen. (Binary Search? Größer ist immer besser?)

### Fall 2 (Kleinteil)
1. Prüfung ob Zahl freier Sauggreifer ausreicht (Early Return für Performance)
2. Wahl der Seite zur Einführung in Maschine (Mindestens 170mm? Überhang)
   Seitenlänge ist nicht ausreichend $<340$ um die Mitte in der Traverse zu behalten.
3. Zielposition "X" mit 170 Überhang, "Y" Bündig
4. Griffkraft prüfen
5. Nicht ausreichend
6. Bündig mit Ecke der Traverse Positionieren
7. Diagonal alle Positionen testen bis die erste mögliche gefunden ist

# Werkstücke
## Fall 1 (Normales Teil)
Kann mit viel $(\text{d} > 170)$ Überhang gegriffen werden
Ideale Position ist oben bündig, mit maximiertem Überhang
![](Positionierung1PieceOverhang.png)
## Fall 2 (Kleinteil)
Kann nicht mit Überhang aufgenommen werden
![](Positionierung1SmallPiece.png)

## Fall 3 (Großes Teil)
Größtes Werkstück, benötigt die gesamte Traverse, mittige Positionierung ist vorteilhafter.
![](Positioning1LargePiece.png)


# Umrechnungen
$$
1m * 1m * 1m = 1000 * 1000 * 1000 = 1.000.000.000mm^3
$$

$$
\frac{1kg}{1m^3} = \frac{1kg}{1.000.000.000mm^3} = \frac{1.000g}{1.000.000.000mm^3} = \frac{1}{1.000.000}\frac{g}{mm^3}
$$

$$
\frac{10N}{kg} = \frac{1N}{100g} 
$$


Great question! Let's break it down:

### You have:
- Box sides in **mm** (let’s call them $$ a, b, c $$)
- **Density** in **kg/m³** ($$ \rho $$)
- **g** = 10 m/s²

### To find:
- **Force needed to lift** = **Weight** = $$ m \times g $$ (in Newtons)
- Need to convert everything to compatible units and find the **multiplicative factor** to go from your given measurements to Force (N).

---

## Step 1: Calculate Volume in m³

Your box’s volume in mm³:
$$
V = a \times b \times c \;\; \text{(in mm³)}
$$

Convert mm³ to m³:
$$
1\, \text{mm} = 10^{-3}\, \text{m} \implies 1\, \text{mm}^3 = 10^{-9}\, \text{m}^3
$$
$$
V_{\text{m}^3} = (a \times b \times c) \times 10^{-9}
$$

---

## Step 2: Calculate Mass

$$
m = \rho \times V_{\text{m}^3}
$$

---

## Step 3: Calculate Weight (Force)

$$
F = m \times g = \rho \times V_{\text{m}^3} \times g
$$
Substitute for $$ V_{\text{m}^3} $$:
$$
F = \rho \times (a \times b \times c) \times 10^{-9} \times g
$$

---

## **Final Formula and Factor**

$$
\boxed{
F = (a \times b \times c) \times \rho \times g \times 10^{-9}
}
$$

So, **the factor you need is:**
$$
\boxed{
\rho \times g \times 10^{-9}
}
$$

where:
- $$ a, b, c $$ in **mm**
- $$ \rho $$ in **kg/m³**
- $$ g $$ in **m/s²** (here, 10)

**Multiply your product of side lengths (in mm), the density, and g, then multiply by $$ 10^{-9} $$.**

---

### **Example**

Box: $$ 100\,\mathrm{mm} \times 200\,\mathrm{mm} \times 300\,\mathrm{mm} $$

Density: $$ 800\,\mathrm{kg/m}^3 $$

g: 10

$$
F = 100 \times 200 \times 300 \times 800 \times 10 \times 10^{-9}
$$
$$
F = (6,000,000) \times 8000 \times 10^{-9}
$$
$$
F = 48,000,000,000 \times 10^{-9} = 48\; \text{N}
$$

---

## **Summary Table**

| Quantity         | Unit   |
|------------------|--------|
| Sides            | mm     |
| Density ($$ \rho $$) | kg/m³ |
| Gravity ($$ g $$)    | m/s²  |
| Factor           | $$ \rho \times g \times 10^{-9} $$ |

---

**That’s your conversion factor!**