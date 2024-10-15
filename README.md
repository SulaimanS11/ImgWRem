# **ImgWRem**  

## **Description**  
**ImgWRem** is a simple Python-based tool that removes unwanted whitespace from images. It is useful for:
- **Cropping unnecessary borders** or white padding.
- Preparing images for **presentations, printing**, or **automation**.
- Ensuring cleaner and more visually appealing images with **minimal effort**.
- Removes the white background and makes the image background transparent.

This tool works by identifying and cropping out regions with unnecessary whitespace surrounding the content in an image.

---

## **Features**
- **Automatic whitespace detection and removal** from images.
- **Batch processing**: Apply cropping to multiple images in one go.
- Supports **popular image formats**: PNG, JPEG, BMP, etc.
- **Simple CLI interface** for easy usage.

---

## **Installation**

### **1. Clone the Repository:**

```bash
git clone https://github.com/SulaimanS11/ImgWRem.git
cd ImgWRem
```
### **2. Install Dependencies:**

Ensure you have Python 3.x installed on your system. Install the required Python packages using:
```bash
pip install -r requirements.txt
```

---

## **Usage**

### **Command Line Usage:**

You can run the tool directly from the command line. Below are the most common use cases:
```bash
python imgwrem.py <input_image> [--output <output_image>] [--batch]
```

### **Options:**

| **Option**           | **Description**                                   | **Example**                                      |
|----------------------|----------------------------------------------------|-------------------------------------------------|
| `<input_image>`      | Path to the input image.                           | `python imgwrem.py image.png`                   |
| `--output`           | Optional: Path to save the cropped image.          | `--output cropped_image.png`                    |
| `--batch`            | Optional: Enable batch processing on a directory. | `python imgwrem.py input_folder/ --batch`       |

## **Examples:**

1. Remove whitespace from a single image:
```bash
python imgwrem.py sample.png --output sample_cropped.png
```
2. Batch processing of all images in a folder:
```bash
python imgwrem.py images/ --batch
```

---

## **Supported Image Formats**
- PNG
- JPEG / JPG
- BMP
- TIFF

---

## **How It Works**

The tool uses **Pillow (Python Imaging Library)** to open and process images. It:

1. Detects non-white pixel regions.
2. Crops the image to remove the surrounding whitespace.
3. Saves the new image (if --output is provided) or overwrites the original.

---

## **Limitations**

- The current version only detects pure white (#FFFFFF) and shades of white regions as whitespace. 
- For complex backgrounds or non-white padding, the tool might not perform as expected.

---

## **Contributing**

Contributions are welcome! If you would like to add new features or improve the code, feel free to:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## **Acknowledgments**

- Built with **Python** and the **Pillow** library.
- Thanks to all contributors and open-source libraries used in this project.

---

## **Contact**

If you encounter any issues, have questions, or would like to suggest improvements, feel free to reach out or open an issue on the [GitHub Issues](https://github.com/SulaimanS11/ImgWRem/issues) page.

You can also contact me directly:

- **GitHub:** [SulaimanS11](https://github.com/SulaimanS11)
- **Email:** [sult2271@mylaurier.ca](mailto:sult2271@mylaurier.ca)
- **LinkedIn:** [Mir Sulaiman Sultan](https://www.linkedin.com/in/mirssultan/)

---

## **Changelog**
**v1.0.0**

- Initial release with:
  * Whitespace removal for individual images.
  * Batch processing support.
  * Command-line interface for ease of use.

---

## **Future Improvements**

- Add support for detecting non-white backgrounds.
- Add GUI support for non-technical users.
- Enhance performance for large batch processing.




















