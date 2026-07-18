# Clogs (Continued Logarithms)
#
# Clogs are expressions of the form log_b(a_1 + log_b(a_2 + ... log_b(a_n)...))
# introduced by Jörg Neunhäuserer (http://www.neunhaeuserer.de/art27.pdf).
# A different object with the same name is due to Bill Gosper, developed by
# Borwein et al. (https://carmamaths.org/resources/jon/clogs.pdf) — see
# docs/clogs/two-lineages.md.
#
# Generates the scatter plots for docs/clogs/gallery.md:
#   uv run --with matplotlib --with numpy tools/clogs.py

import itertools
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).resolve().parent.parent / "docs" / "clogs" / "assets"


def clog_value(digit_sequence, base, log_base_precomputed):
    """
    Continued logarithm where the sequence is OUTERMOST -> INNERMOST.

    e.g. (1, 2, 1, 2) |--> log(1 + log(2 + log(1 + log(2))))
    """
    v = 0.0
    for d in reversed(digit_sequence):
        v = np.log(d + v) / log_base_precomputed
    return v


def unique_clogs_with_optional_annotations(base, n_iter=50000, n_annotate=0):
    """
    Get unique clogs, returning lists of (depth, value) and optionally
    (depth, value, expr) for the first n_annotate unique points.
    """
    x_depths, y_vals = [], []
    annotated = []
    seen = set()

    log_base = np.log(base)
    alphabet = tuple(range(1, base))

    # Only ever plot complete depth levels: cutting a level mid-enumeration
    # leaves a partial column whose spread is an artifact of digit order.
    L = 1
    while len(x_depths) < n_iter:
        for digit_sequence in itertools.product(alphabet, repeat=L):
            val = clog_value(digit_sequence, base, log_base)

            key = round(val, 12)
            if key in seen:
                continue
            seen.add(key)

            x_depths.append(L)
            y_vals.append(val)

            if len(annotated) < n_annotate:
                expr = f"\\log_{{{base}}}({digit_sequence[-1]})"
                for d in reversed(digit_sequence[:-1]):
                    expr = f"\\log_{{{base}}}({d}+{expr})"
                annotated.append((L, val, f"${expr}$"))

        L += 1

    return x_depths, y_vals, annotated


def plot_clog_grid(path, bases=range(3, 9), n_iter=10000):
    """
    Scatter of clogs for each base, first few points annotated with their
    expressions. X-axis = depth (number of logs).
    """
    n_rows, n_cols = 2, 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 12))
    fig.suptitle("Clogs (continued logarithms)", fontsize=34, y=0.98)

    for ax, base in zip(axes.flat, bases):
        print("base", base)

        x_depths, y_vals, annotated = unique_clogs_with_optional_annotations(
            base=base,
            n_iter=n_iter,
            n_annotate=max(16, (base - 1) ** 2),
        )

        ax.scatter(x_depths, y_vals, s=12)
        ax.set_title(f"Clogs base {base}", fontsize=16)
        ax.set_xlabel("Depth (number of log terms)", fontsize=10)
        ax.set_ylabel("Value", fontsize=10)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.tick_params(axis="both", which="major", labelsize=10)

        if x_depths:
            ax.set_xticks(range(min(x_depths), max(x_depths) + 1))

        for depth, yi, expr in annotated:
            ax.annotate(
                expr,
                xy=(depth, yi),
                xytext=(6, 6),
                textcoords="offset points",
                fontsize=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7),
            )

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print("wrote", path)


def plot_single_base(path, base, n_iter=20000):
    """One base on its own, more points, no annotations — the shape itself."""
    x_depths, y_vals, _ = unique_clogs_with_optional_annotations(base, n_iter=n_iter)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x_depths, y_vals, s=6, alpha=0.6)
    ax.set_title(f"Clogs base {base}", fontsize=18)
    ax.set_xlabel("Depth (number of log terms)", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.6)
    if x_depths:
        ax.set_xticks(range(min(x_depths), max(x_depths) + 1))

    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print("wrote", path)


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    plot_clog_grid(ASSETS / "clog-grid.png")
    plot_single_base(ASSETS / "clog-base3.png", base=3)
    plot_single_base(ASSETS / "clog-base10.png", base=10)
