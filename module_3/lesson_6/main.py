from docx import Document


def extract_images_from_docx(docx_file):
    doc = Document(docx_file)
    images = []
    for rel in doc.part.rels:
        if "image" in rel.reltype:
            image_data = rel.target_part.blob
            images.append(image_data)
    return images


if __name__ == "__main__":
    docx_file = "task_photo.doc"  # Word fayl nomi
    images = extract_images_from_docx(docx_file)
    for i, image_data in enumerate(images):
        with open(f"image_{i}.png", "wb") as img_file:
            img_file.write(image_data)
