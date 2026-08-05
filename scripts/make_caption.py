#!/usr/bin/env python3
"""Writes a simple, ready-to-post caption (feed or reel) to a temp file and
prints its path. No AI generation -- a small set of static templates in
Au Gratin's voice (playful, informal, food-craving language, light emoji
use, same pattern proven on GM Hamburgueria's automation), picked at random
so consecutive posts don't read identically. Swap this for an AI-generated
version later if the static set feels repetitive.

NOTE: no direct access to Au Gratin's Instagram/hours/delivery info was
available when this was written -- the FOOTER below is a placeholder Rob
should edit with the real hours/address/delivery info.

Usage: make_caption.py <feed|reel>
Prints: path to the temp file containing the caption.
"""
import random
import sys
import tempfile

FOOTER = (
    "\n\n📍 Au Gratin\n"
    "⏰ Confira nosso horario de funcionamento\n"
    "👉 Vem provar!"
)

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

TEMPLATES = {"feed": FEED_TEMPLATES, "reel": REEL_TEMPLATES}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in TEMPLATES:
        print("Uso: make_caption.py <feed|reel>", file=sys.stderr)
        raise SystemExit(1)
    kind = sys.argv[1]
    body = random.choice(TEMPLATES[kind])
    caption = body + FOOTER
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(caption)
        path = f.name
    print(path)


if __name__ == "__main__":
    main()
