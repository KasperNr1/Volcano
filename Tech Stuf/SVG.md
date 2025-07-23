# Aufbau
``` XML
<svg version="1.1"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" fill="red" />

  <circle cx="150" cy="100" r="80" fill="green" />

  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>

</svg>
```

![](SvgDemo.svg)

## Transform
Die bei mehreren Operationen innerhalb eines `transform` Attributs ist die Reihenfolge relevant. [Die Operatoren werden von rechts nach links angewandt.](https://www.mediaevent.de/tutorial/svg-transform.html#:~:text=Mehrere%20Transformationen%20kombinieren)

Beispielsweise entsteht nur durch die Kombination
`new XAttribute("transform", $"rotate(...) translate(...)") `
das Ergebnis einer Rotierten Grafik um den in `rotate()` angegebenen Mittelpunkt.
Ein Vertauschen der beiden Transformationen führt durch die Verschiebung des Mittelpunkts zu einer Rotation die nicht in der Mitte des Objekts bleibt.