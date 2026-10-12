import os

def combine_files(input_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Walk through the folder
        for root, dirs, files in os.walk(input_folder):
            for filename in files:
                if filename != "__pycache__" and filename != "README.md":
                    file_path = os.path.join(root, filename)

                    # Write the label
                    outfile.write(f"===== FILE: {file_path} =====\n")

                    # Write the file contents
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"[Error reading file: {e}]")

                    outfile.write("\n\n")  # spacing between files


combine_files("planet-node", "ignore/current-planet-node.txt")
combine_files("solar-system-cluster", "ignore/current-solar-system-cluster.txt")