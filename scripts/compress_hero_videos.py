from __future__ import annotations

import argparse
from pathlib import Path

import ffmpeg


def mb(size_bytes: int) -> float:
    return size_bytes / (1024 * 1024)


def compress_video(
    input_path: Path,
    output_path: Path,
    crf: int,
    maxrate_k: int,
    width: int,
    fps: int,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    (
        ffmpeg.input(str(input_path))
        .filter("fps", fps=fps)
        .filter("scale", f"min({width},iw)", "-2")
        .output(
            str(output_path),
            vcodec="libx264",
            pix_fmt="yuv420p",
            profile="main",
            preset="slow",
            movflags="+faststart",
            crf=crf,
            maxrate=f"{maxrate_k}k",
            bufsize=f"{maxrate_k * 2}k",
            an=None,
        )
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Comprime videos do hero para web (PageSpeed-friendly)."
    )
    parser.add_argument(
        "--video-dir",
        default="assets/video",
        help="Pasta onde estao os videos de entrada.",
    )
    parser.add_argument(
        "--output-dir",
        default="assets/video/optimized",
        help="Pasta de saida para os videos comprimidos.",
    )
    parser.add_argument("--crf", type=int, default=28, help="Qualidade x264 (menor = melhor).")
    parser.add_argument("--maxrate", type=int, default=1200, help="Bitrate maximo em kbps.")
    parser.add_argument("--width", type=int, default=1280, help="Largura maxima do video.")
    parser.add_argument("--fps", type=int, default=24, help="FPS de saida.")
    args = parser.parse_args()

    input_dir = Path(args.video_dir)
    output_dir = Path(args.output_dir)

    targets = [
        "1-video-hero.mp4",
        "2-video-hero.mp4",
    ]

    print("Iniciando compressao dos videos do hero...")
    for name in targets:
        input_path = input_dir / name
        if not input_path.exists():
            print(f"[AVISO] Arquivo nao encontrado: {input_path}")
            continue

        output_name = input_path.stem + "-optimized.mp4"
        output_path = output_dir / output_name

        original_size = input_path.stat().st_size
        print(f"\nProcessando: {input_path}")
        print(f"Tamanho original: {mb(original_size):.2f} MB")

        try:
            compress_video(
                input_path=input_path,
                output_path=output_path,
                crf=args.crf,
                maxrate_k=args.maxrate,
                width=args.width,
                fps=args.fps,
            )
            compressed_size = output_path.stat().st_size
            ratio = (1 - (compressed_size / original_size)) * 100
            print(f"Arquivo gerado: {output_path}")
            print(f"Tamanho comprimido: {mb(compressed_size):.2f} MB")
            print(f"Reducao: {ratio:.1f}%")
        except ffmpeg.Error as exc:
            print(f"[ERRO] Falha ao comprimir {input_path.name}")
            print(exc.stderr.decode("utf-8", errors="ignore"))

    print("\nConcluido.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
