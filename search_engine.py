import os

def search_files(keyword, folder="text_corpus"):
    results = []
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_num, line in enumerate(lines, start=1):
                    if keyword.lower() in line.lower():
                        results.append((filename, line_num, line.strip()))
    return results

def main():
    print("🔍 Simple Search Engine")
    query = input("Enter a keyword to search: ")
    matches = search_files(query)

    if matches:
        print(f"\n✅ Found {len(matches)} match(es):")
        for file, line_num, content in matches:
            print(f"{file} [Line {line_num}]: {content}")
    else:
        print("❌ No matches found.")

if __name__ == "__main__":
    main()
