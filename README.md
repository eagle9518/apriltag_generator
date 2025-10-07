# AprilTag Page Generator

A command-line utility to arrange multiple AprilTag images onto a single, print-ready SVG page. This tool simplifies the generation of custom tag sheets for robotics and computer vision applications.

---

## Features

* Combines multiple AprilTag `.png` files into a single document.
* Arranges tags in a grid with a user-specified number of columns.
* Scales tags to a precise physical size (e.g., `mm`, `cm`).
* Outputs a vector-based `.svg` file suitable for high-quality printing.

---

## Installation

### Prerequisites

* Python 3.x
* Pip

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/eagle9518/apriltag_generator.git
    cd apriltag_generator
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    *(Note: A `requirements.txt` file will be added to the repository soon for streamlined installation.)*
    ```bash
    pip install <library_name_1> <library_name_2>
    ```

---

## Usage

Run the script from the command line, providing the input tag files and the desired output parameters.

### Command Structure

```bash
python main.py [tag_files...] --out [output_file.svg] --size [tag_size] --columns [number]
