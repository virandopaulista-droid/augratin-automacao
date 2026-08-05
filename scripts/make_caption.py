#!/usr/bin/env python3
"""Writes a simple, ready-to-post caption (feed or reel) to a temp file and
prints its path. No AI generation -- a small set of static templates in Au
Gratin's voice (playful, informal, food-craving language, light emoji use),
picked at random so consecutive posts don't read identically. Swap this for
an AI-generated version later if the static set feels repetitive.

Au Gratin is dine-in only (buffet by weight, salão), NOT delivery -- unlike
GM Hamburgueria. Never write "peça já"/delivery-style CTAs here; invite
people to come eat in person instead. Real info from Rob (2026-08-05):
address R. Amador Bueno, 771, Santo Amaro, São Paulo - SP; hours seg a sex
11h às 15h; buffet muda todo dia, é por peso.

The buffet has day-specific dishes some weekdays -- pass --weekday
<segunda|terca|quarta|quinta|sexta> to get a caption that name-drops that
day's special (falls back to a generic "pratos variados" line otherwise).
Confirmed by Rob 2026-08-05:
  segunda/terca: pratos variados (no single standout dish)
  quarta: feijoada
  quinta: massas, sushi e costela no bafo
  sexta: salmão e rabada

Usage: make_caption.py <feed|reel> [--weekday <dia>]
Prints: path to the temp file containing the caption.
"""
import random
import sys
import tempfile

FOOTER = (
    "\n\n📍 Au Gratin, R. Amador Bueno, 771, Santo Amaro, São Paulo\n"
    "⏰ Seg a sex, 11h às 15h, presencial, buffet por peso\n"
    "👉 Vem provar!"
)

WEEKDAY_SPECIALS = {
    "quarta": "feijoada",
    "quinta": "massas, sushi e costela no bafo",
    "sexta": "salmão e rabada",
}

FEED_TEMPLATES = [
    "Óia que fartura! 🧀 Cada prato temperado com carinho, do jeitinho que só a Au Gratin faz.",
    "Reparou no capricho? Comida de verdade, feita fresquinha pra você se deliciar.",
    "Sabor que não erra, direto da nossa pista pro seu prato. Bora matar essa vontade?",
    "Aqui não tem meio-termo: é sabor de verdade, sempre fresquinho e bem servido.",
]

REEL_TEMPLATES = [
    "Direto da nossa cozinha pra sua tela! 🔥 Vem ver o capricho que colocamos em cada prato.",
    "Bastidores da Au Gratin: é assim que preparamos tudo, com muito carinho e capricho.",
    "Água na boca só de ver! Passa aqui pra conferir de perto o que está saindo agora.",
]

FEED_TEMPLATES_SPECIAL = [
    "Hoje tem {prato} na nossa pista! 🧀 Chega por peso e monte o seu prato do jeito que quiser.",
    "É dia de {prato} na Au Gratin! Vem cedo que é bom, viu?",
    "Óia o que tá saindo hoje: {prato}. Sabor de verdade, pesado com carinho.",
]

REEL_TEMPLATES_SPECIAL = [
    "Hoje é dia de {prato} aqui na Au Gratin! 🔥 Vem de salão, é por peso e sempre fresquinho.",
    "Segredo revelado: hoje tem {prato} esperando por você na nossa pista.",
]

TEMPLATES = {"feed": FEED_TEMPLATES, "reel": REEL_TEMPLATES}
TEMPLATES_SPECIAL = {"feed": FEED_TEMPLATES_SPECIAL, "reel": REEL_TEMPLATES_SPECIAL}


def build_caption(kind, weekday=None):
    prato = WEEKDAY_SPECIALS.get(weekday)
    if prato:
        body = random.choice(TEMPLATES_SPECIAL[kind]).format(prato=prato)
    else:
        body = random.choice(TEMPLATES[kind])
    return body + FOOTER


def main():
    args = sys.argv[1:]
    if not args or args[0] not in TEMPLATES:
        print("Uso: make_caption.py <feed|reel> [--weekday <dia>]", file=sys.stderr)
        raise SystemExit(1)
    kind = args[0]
    weekday = None
    if "--weekday" in args:
        idx = args.index("--weekday")
        if idx + 1 < len(args):
            weekday = args[idx + 1]
    caption = build_caption(kind, weekday)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(caption)
        path = f.name
    print(path)


if __name__ == "__main__":
    main()
