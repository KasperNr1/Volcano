# Why You Cannot Have Infinite Cookies
### Animated Math Explainer — Script & Animation Plan

---

## Structure Overview

| Segment | Duration | Purpose |
|---|---|---|
| Hook | ~1 min | The dinner scene, pose the question |
| Formalization | ~1.5 min | Define the math, show convergence |
| The Intuition Trap | ~1.5 min | p=0 works but is useless; there must be a sweet spot |
| Large p fails | ~1.5 min | First bite already exceeds 1/n |
| The Round Reframe | ~2 min | Full-rounds argument kills the remaining hope |
| Algebraic confirmation | ~1 min | Derive the formula, show p=0 is the only solution |
| Payoff / title callback | ~0.5 min | Why you really can't have infinite cookies |

---

## Script

---

### Segment 1 — Hook

> Picture this: you're at dinner with some friends, and someone brings out a single dessert to share. Classic problem.
>
> Someone jokes — *"what if we each just took half of what's left? We could eat forever."*
>
> And you laugh. But then you think about it.
>
> **[ANIMATION: a full circle (the cake). A hand takes half — the circle splits, one wedge slides out. Another hand takes half of the remainder — a smaller wedge slides out. Then another. The wedges grow smaller but keep appearing, radiating around the circle.]**
>
> You'd each get smaller and smaller bites... but you'd *never* run out of dessert to take. Infinite bites. One cake.
>
> That's actually true, by the way. And we'll see why in a moment.
>
> But that joke raised a more interesting question: is there some fraction — call it *p* — where if everyone always takes *p* of whatever is left, everyone ends up with *exactly the same amount*?
>
> Seems like it should exist. Let's find out.

---

### Segment 2 — Formalization

> Let's make this precise. There's one dessert, normalized to size 1. Friends line up. Each takes fraction *p* of whatever remains. Then the next person. Then the next. Forever.
>
> **[ANIMATION: a full circle. A sector of angle p·360° is cut and colored (person 1). From the remainder, a sector of p·(1-p)·360° is cut and colored differently (person 2). Then p·(1-p)²·360° for person 3. Sectors fill the circle, each a different color, each visibly smaller than the last.]**
>
> Person 1 gets *p*.
> Person 2 gets *p(1-p)*.
> Person 3 gets *p(1-p)²*.
> Person *k* gets *p(1-p)^(k-1)*.
>
> Now, does this actually consume the whole dessert? Add them all up:
>
> **[ANIMATION: write the sum below the circle, factor out p, show it as a geometric series]**
>
> This is a geometric series with ratio *(1-p)*. As long as *p* is strictly between 0 and 1, that ratio is less than 1, and the series converges — to exactly 1. The whole dessert. Every bite.
>
> Infinite steps. Finite result. That's the "infinite cookies" part — you can eat forever and still only eat one cake.

---

### Segment 3 — The Intuition Trap

> So now the fairness question. We want everyone to get *1/n* — an equal share.
>
> **[ANIMATION: n=2 case. A circle split cleanly into two equal halves, each labeled 1/2. A question mark appears — can we achieve this with the rule?]**
>
> Let's think about *p=0* first. Everyone takes nothing. The dessert sits there untouched. Technically fair — everyone gets zero. But nobody gets fed. That doesn't count.
>
> What about *p=1*? Person 1 takes the entire dessert. Maximally unfair.
>
> **[ANIMATION: a slider for p from 0 to 1. As p moves, the circle updates: person 1's wedge grows, person 2's shrinks. At p=0 both wedges are invisible. At p=1 person 1 owns the whole circle.]**
>
> Somewhere between 0 and 1, fairness must live. Right?
>
> This is exactly the intuition that leads you astray. Let's chase it.

---

### Segment 4 — Large p fails instantly

> Start with two friends. Fair sharing means each gets exactly *1/2*.
>
> If *p > 1/2*, person 1 takes more than half the dessert in a single bite. Before person 2 even reaches the plate. Game over — person 1 already has more than their share, and person 2 is playing catch-up with less than half the dessert remaining.
>
> **[ANIMATION: circle with p slightly above 0.5. Person 1's first wedge is visibly larger than a semicircle. The remaining arc is highlighted — everything person 2 could ever receive, even over infinite turns, is contained in this smaller piece. It cannot reach 1/2.]**
>
> More generally, for *n* friends, any *p > 1/n* means person 1 takes more than their fair share in the first turn alone.
>
> So fair sharing, if it exists, requires *p ≤ 1/n*. The search narrows.
>
> **[ANIMATION: the p-slider zooms in on the interval (0, 1/n). The rest grays out.]**

---

### Segment 5 — The Round Reframe

> Now for the elegant part.
>
> Instead of thinking about the sequence as one long spiral of individual bites, regroup it. Think of *rounds*: one full round is everyone taking a turn once, in order.
>
> **[ANIMATION: the circle's wedges get bracketed into rounds. Round 1 is the first n wedges, round 2 the next n, and so on. Each round's wedges are outlined together. The rounds spiral inward as they shrink.]**
>
> In round 1: person 1 takes *p*, person 2 takes *p(1-p)*, ..., person *n* takes *p(1-p)^(n-1)*.
>
> In round 2: person 1 takes *p(1-p)^n*, person 2 takes *p(1-p)^(n+1)*, ...
>
> **[ANIMATION: isolate a single round. Extract those n wedges and display them side by side as a smaller circle divided into n sectors. Person 1's sector is always the largest.]**
>
> Look at any single round. Person 1 takes first, so they take *more* than person 2. Person 2 takes more than person 3. The order is strict, every single round.
>
> Now sum across all rounds. Person 1 wins every round. Not some of them — every last one, stretching to infinity.
>
> There is no *p > 0* that fixes this. Person 1 is always first in line, in every round, forever. The structure of the problem guarantees the unfairness — not the specific value of *p*.
>
> **[ANIMATION: pull back to show all rounds as a sequence of shrinking circles. Each one has person 1 in the lead. Stack their contributions — person 1's total arc is always the largest.]**
>
> So the search for a fair *p* in *(0, 1/n]* comes up empty too. The only remaining candidate is *p = 0*. And we already threw that out.

---

### Segment 6 — Algebraic Confirmation

> Let's confirm this with the formula. Person *k*'s total share across all rounds is:
>
> **[ANIMATION: write S_k = p(1-p)^(k-1) / (1 - (1-p)^n)]**
>
> For fairness, set *S_1 = S_2*:
>
> *p(1-p)^0 = p(1-p)^1*
>
> Divide both sides by *p* (since *p ≠ 0*):
>
> *1 = (1-p)*
>
> Which gives *p = 0*. Contradiction.
>
> **[ANIMATION: the equation simplifies step by step. "p = 0" appears, highlighted in red. The circle from earlier reappears — at p=0, all wedges vanish. The cake sits whole and untouched.]**
>
> The algebra agrees with the intuition. No fixed fraction can ever be fair.

---

### Segment 7 — Payoff

> So — why can't you have infinite cookies?
>
> Not because you run out of dessert. The dessert is always there; the bites are real; the series converges.
>
> You can't have infinite cookies because infinite fairness is impossible. The moment you pick *any* positive fraction, you've handed person 1 a permanent advantage — baked into the structure of the game itself, repeated infinitely.
>
> **[ANIMATION: final callback to the opening circle. The full cake reappears. Wedges fill it again in the same spiral pattern. Camera slowly zooms out as the wedges keep subdividing, infinitely small, the circle always just barely full.]**
>
> The only fair rule is to take nothing. And nobody came to dinner for that.

---

## Animation Plan (Manim)

| Scene | Key Objects | Notes |
|---|---|---|
| Hook | `Circle`, `Sector` | Recursive wedge cuts; each sector angle = p · remaining angle |
| Formalization | `Circle`, `Sector` array, `MathTex` | Sequential sectors fill circle; formula appears below |
| Slider | `ValueTracker` for p, `Sector` updating live | Smooth sweep; person 1 sector grows, others shrink |
| Large p fails | `Circle`, `Arc` highlight | Remainder arc after first bite; label shows it is < 1/2 |
| Round reframe | `VGroup` of `Sector` sets, bracket annotations | Group wedges into rounds; extract one round into its own mini-circle |
| Algebra | `MathTex`, `TransformMatchingTex` | Step-by-step simplification; p=0 highlighted in red |
| Payoff | Echo of opening `Circle` + `Sector` spiral | Camera zoom out; infinite subdivision implied |
