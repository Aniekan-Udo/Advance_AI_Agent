import os

# Define the directory structure
structure = {
    "final_code": {
        "__init__.py": "",
        "config.py": "",
        "main.py": "",
        "search": {
            "__init__.py": "",
            "rag_search.py": "",
            "internet_search.py": "",
            "url_search.py": "",
        },
        "publish": {
            "__init__.py": "",
            "reviewer.py": "",
            "writer.py": "",
        },
        "supervisor": {
            "__init__.py": "",
            "search_team.py": "",
            "publishing_team.py": "",
            "top_level.py": "",
        },
        "utils": {
            "__init__.py": "",
            "vector_store.py": "",
        }
    }
}

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Create file
            with open(path, "w") as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Project structure created successfully!")
