# SPDX-License-Identifier: MIT
"""Write one childhood memory to /output/entry.txt."""

import os

SENTENCE = (
    "On Sunday nights before term, my father ironed my uniform in the hallway "
    "outside the bathroom, the board creaking, the radio low with cricket scores, "
    "starch and warm cotton in the air, while I slept on the floor beside him "
    "before the last shirt was done."
)


def main() -> None:
    text = SENTENCE.strip()
    if not text or not (1 <= len(text) <= 280):
        raise SystemExit(f"entry length {len(text)} is outside 1..280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    encoded = text.encode("utf-8")
    print(text)
    print(f"chars={len(text)} bytes={len(encoded)}")


if __name__ == "__main__":
    main()
