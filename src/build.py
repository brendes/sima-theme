#!/usr/bin/env python3

import json
import os
from typing import Dict, Any

base_colors = {
    "light": {
        "theme_type": "light",
        "red_1": "#bb5555",
        "red_2": "#e89090",
        "orange_1": "#d08868",
        "orange_2": "#f0bca0",
        "yellow_1": "#aa8866",
        "yellow_2": "#eed0bb",
        "green_1": "#889944",
        "green_2": "#b0c088",
        "blue_1": "#5577aa",
        "blue_2": "#bbc8dd",
        "purple_1": "#8c6d9c",
        "purple_2": "#bbaadd",
        "magenta_1": "#aa7788",
        "magenta_2": "#d8b8c8",
        "cyan_1": "#669988",
        "cyan_2": "#b8dbd4",
        "invisible": "#00000000",
    },
    "dark": {
        "theme_type": "dark",
        "red_1": "#dd7777",
        "orange_1": "#dd9922",
        "yellow_1": "#eebb88",
        "green_1": "#aab866",
        "blue_1": "#80a8b0",
        "purple_1": "#8c6d9c",
        "magenta_1": "#d3889b",
        "cyan_1": "#88b4a0",
        "invisible": "#00000000",
    },
}

themes = {
    "white": {
        **base_colors["light"],
        "theme_name": "sima white",
        "base_0": "#ffffff",
        "base_1": "#f9f9f9",
        "base_2": "#f4f4f4",
        "base_3": "#eaeaea",
        "base_4": "#dddddd",
        "base_5": "#707070",
        "base_6": "#000000",
        "base_7": "#000000",
    },
    "sun": {
        **base_colors["light"],
        "theme_name": "sima sun",
        "base_0": "#fffffa",
        "base_1": "#f9f9f4",
        "base_2": "#f4f4ef",
        "base_3": "#eaeae5",
        "base_4": "#ddddd8",
        "base_5": "#70706b",
        "base_6": "#000000",
        "base_7": "#000000",
    },
    "paper": {
        **base_colors["light"],
        "theme_name": "sima paper",
        "base_0": "#faf7f2",
        "base_1": "#f2efea",
        "base_2": "#ece7e2",
        "base_3": "#e0d8d0",
        "base_4": "#d0c8bd",
        "base_5": "#887872",
        "base_6": "#403a32",
        "base_7": "#000000",
    },
    "acme": {
        **base_colors["light"],
        "theme_name": "sima acme",
        "base_0": "#ffffee",
        "base_1": "#f9f9e9",
        "base_2": "#f4f4e4",
        "base_3": "#eaeada",
        "base_4": "#ddddcc",
        "base_5": "#707060",
        "base_6": "#000000",
        "base_7": "#000000",
        "red_1": "#bb5d5d",
        "red_2": "#ee9999",
        "yellow_1": "#998866",
        "yellow_2": "#eeeeaa",
        "green_1": "#448844",
        "green_2": "#bbddbb",
        "blue_1": "#6677bb",
        "blue_2": "#ccccff",
        "magenta_1": "#aa77aa",
        "magenta_2": "#ddbbdd",
        "cyan_1": "#66aaaa",
        "cyan_2": "#addddd",
    },
    "dark": {
        **base_colors["dark"],
        "theme_name": "sima dark",
        "base_0": "#282828",
        "base_1": "#303030",
        "base_2": "#383838",
        "base_3": "#484848",
        "base_4": "#585858",
        "base_5": "#a8a8a8",
        "base_6": "#cccccc",
        "base_7": "#eeeeee",
    },
    "gruv": {
        **base_colors["dark"],
        "theme_name": "sima gruv",
        "base_0": "#32302f",
        "base_1": "#3a3837",
        "base_2": "#403d3c",
        "base_3": "#4c4948",
        "base_4": "#595654",
        "base_5": "#c0b09b",
        "base_6": "#e0d0bb",
        "base_7": "#ffefcc",
    },
    "nord": {
        **base_colors["dark"],
        "theme_name": "sima nord",
        "base_0": "#2e3440",
        "base_1": "#363d4c",
        "base_2": "#3c4352",
        "base_3": "#434c5e",
        "base_4": "#576279",
        "base_5": "#abb3c2",
        "base_6": "#d8dee9",
        "base_7": "#e8eef9",
        "red_1": "#bf616a",
        "orange_1": "#d08770",
        "green_1": "#a3be8c",
        "yellow_1": "#ebcb8b",
        "blue_1": "#81a1c1",
        "magenta_1": "#b48ead",
        "cyan_1": "#88c0d0",
    },
}

for theme_name, theme in themes.items():
    theme["bg_main"] = theme["base_0"]
    theme["bg_subtle"] = theme["base_1"]
    theme["bg_fade"] = theme["base_2"]
    theme["bg_hl"] = theme["base_3"]
    theme["bg_sel"] = theme["base_3"] + "ee"
    theme["bg_strong"] = theme["base_4"]
    theme["bg_bold"] = theme["base_5"]
    theme["bg_drop"] = theme["bg_hl"] + "88"
    theme["fg_main"] = theme["base_6"]
    theme["fg_bold"] = theme["base_7"]

    if theme.get("theme_type") == "light":
        theme["fg_ghost"] = theme["fg_main"] + "18"
        theme["fg_faint"] = theme["fg_main"] + "33"
        theme["fg_fade"] = theme["fg_main"] + "55"
        theme["fg_dim"] = theme["fg_main"] + "80"
        theme["fg_subtle"] = theme["fg_main"] + "a0"
        theme["bg_match_1"] = theme["bg_strong"] + "ee"
        theme["bg_match_2"] = theme["yellow_2"] + "dd"
        theme["border_hard"] = theme["fg_main"] + "58"
        theme["border_soft"] = theme["fg_main"] + "20"
        theme["black_1"] = theme["fg_main"]
        theme["white_2"] = theme["bg_main"]
        theme["link"] = theme["blue_1"]

    elif theme.get("theme_type") == "dark":
        theme["fg_ghost"] = theme["fg_main"] + "18"
        theme["fg_faint"] = theme["fg_main"] + "38"
        theme["fg_fade"] = theme["fg_main"] + "70"
        theme["fg_dim"] = theme["fg_main"] + "98"
        theme["fg_subtle"] = theme["fg_main"] + "bb"
        theme["bg_match_1"] = theme["bg_strong"] + "bb"
        theme["bg_match_2"] = theme["bg_bold"] + "dd"
        theme["border_hard"] = theme["fg_main"] + "50"
        theme["border_soft"] = theme["fg_main"] + "28"
        theme["black_1"] = theme["bg_main"]
        theme["white_2"] = theme["fg_main"]
        theme["link"] = theme["cyan_1"]
        for color in [
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "orange",
            "purple",
        ]:
            theme[f"{color}_2"] = theme[f"{color}_1"]


def generate_theme(theme: Dict[str, str], template_path: str, output_path: str):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_path, "r") as f:
        template = json.load(f)

    def recursive_format(value: Any) -> Any:
        if isinstance(value, str):
            return value.format(**theme)
        elif isinstance(value, list):
            return [recursive_format(item) for item in value]
        elif isinstance(value, dict):
            return {key: recursive_format(val) for key, val in value.items()}
        else:
            return value

    theme_output = recursive_format(template)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(theme_output, f, indent=2)


def main():
    for name, theme in themes.items():
        output_file = f"themes/sima-{name.replace('_', '-')}-color-theme.json"
        generate_theme(theme, "src/template.json", output_file)


if __name__ == "__main__":
    main()
