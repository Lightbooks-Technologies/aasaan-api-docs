import os
import json

def build_json_structure(root_path, base_path):
    result = {
        "group": os.path.basename(root_path),
        "pages": []
    }

    for item in os.listdir(root_path):
        path = os.path.join(root_path, item)
        if os.path.isdir(path):
            # Recursively build JSON for subdirectories
            result["pages"].append(build_json_structure(path, base_path))
        elif item.endswith('.mdx'):
            # Remove the base_path and '.mdx' extension from the file path
            relative_path = os.path.relpath(path, base_path).replace('\\', '/')
            relative_path = relative_path[:-4]  # Remove '.mdx' extension
            result["pages"].append(relative_path)

    return result

def generate_json_for_documentation(directory):
    json_structure = build_json_structure(directory, directory)
    return json.dumps(json_structure, indent=4)



# Replace 'your_documentation_folder_path' with the actual path of your documentation folder
documentation_folder_path = '/Users/sivaramrajugadiraju/Documents/Documents-sivaramMacBookPro/aasaan-api-docs/documentation'
json_output = generate_json_for_documentation(documentation_folder_path)

# Writing JSON output to a file
with open('output.json', 'w') as file:
    file.write(json_output)

