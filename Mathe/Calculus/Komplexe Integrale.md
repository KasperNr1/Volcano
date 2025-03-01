# Eigenschaften des Integrals
## Linearität
$$
\int_a^br*f(x) \, dx = r*\int_a^bf(x)\, dx
$$
## Additivität
$$
\int_a^bf(x) \, dx + \int_a^bg(x) \, dx = \int_a^bf(x)+g(x)\, dx
$$
# Integration durch Substitution
Bekannt: Lineare Substitution
$$
\int_a^bf(r*x+s) \, dx = \frac{1}{r} * [F(r*x+s)]_a^b 
$$
Neu: Logarithmische Substitution
$$
\int_a^b \frac{g'(x)}{g(x)} \, dx = [\ln(|g(x)|)]_a^b
$$
Denn
$$
f(x) = \ln(|g(x)|) \rightarrow f'(x) = \frac{1}{g(x)} * g'(x) = \frac{g'(x)}{g(x)}
$$
