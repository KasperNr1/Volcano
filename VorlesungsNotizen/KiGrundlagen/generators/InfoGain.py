import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# --- LaTeX-Konfiguration ---
# Dies erfordert eine lokale LaTeX-Installation (z.B. TeX Live oder MiKTeX)
try:
    mpl.rcParams.update({
        'text.usetex': True,
        'font.family': 'serif',
        'text.latex.preamble': r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{lmodern}'
    })
    print("LaTeX-Rendering aktiviert.")
except Exception as e:
    print(f"Warnung: LaTeX-Rendering fehlgeschlagen ({e}). Fallback auf Standard-Renderer.")
    mpl.rcParams.update({'text.usetex': False})

# --- Daten erstellen ---
# Erstelle einen Bereich von 0 bis 1. 
# Wir fangen etwas nach 0 an, um den log(0)-Fehler zu vermeiden, und fügen (0,0) manuell hinzu.
x = np.linspace(0.0001, 1.0, 500)
# Die Funktion y = -x * log_2(x)
y = -x * np.log2(x)

# Manuelles Hinzufügen der Punkte (0,0) und (1,0) für einen sauberen Graphen
x_plot = np.concatenate(([0], x))
y_plot = np.concatenate(([0], y))


# --- Plot erstellen ---
fig, ax = plt.subplots(figsize=(8, 6))

# Die Funktion plotten
ax.plot(x_plot, y_plot, lw=2)

# --- Achsen und Beschriftungen (passend zum Bild) ---

# Achsenbeschriftungen (mit LaTeX gerendert)
ax.set_xlabel(r'Wahrscheinlichkeit P(A)', fontsize=14)
ax.set_ylabel(r'Informationsgehalt', fontsize=14)

# Achsengrenzen setzen
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 0.6])

# Ticks (Achsenunterteilungen) setzen
ax.set_xticks(np.arange(0.0, 1.1, 0.2))
ax.set_yticks(np.arange(0.0, 0.61, 0.1))

# Schriftgröße der Ticks
ax.tick_params(axis='both', which='major', labelsize=12)

# Optional: Ein feines Gitter hinzufügen, ähnlich dem Originalbild
ax.grid(True, linestyle=':', alpha=0.7)

# Layout optimieren und Plot anzeigen
plt.tight_layout()
plt.savefig("informationsgehalt.png", dpi=300) # Speichert die Datei
plt.show()