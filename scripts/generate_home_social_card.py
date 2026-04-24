from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_IMAGE = Path("/Users/yael/Desktop/Copy of yael.ca.png")
OUTPUT_IMAGE = ROOT / "static" / "images" / "og-home.jpg"

WIDTH = 1200
HEIGHT = 630


def fit_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize(
        (int(image.width * scale), int(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def main() -> None:
    source = Image.open(SOURCE_IMAGE).convert("RGB")

    # Remove the extra white bar at the top; the remainder is already at the
    # correct social-card aspect ratio.
    source = source.crop((0, 48, source.width, source.height))

    card = fit_cover(source, (WIDTH, HEIGHT))
    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    card.save(OUTPUT_IMAGE, quality=92, subsampling=0)


if __name__ == "__main__":
    main()
