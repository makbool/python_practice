from pathlib import Path

curr_path = Path()

print(curr_path.exists())
print(curr_path.absolute())

new_path = Path("test_dir")

print(new_path.exists())
print(new_path.absolute())

try:
    new_path.mkdir()
    print("Directory Created")
except FileExistsError as fee:
    print("File Exists Error ", fee)

try:
    new_path.rmdir()
    print("Directory Deleted")
except FileNotFoundError as fnfe:
    print("File Not Found Error ", fnfe)

for file in curr_path.glob('*'):
    print(file)

for file in curr_path.glob('*.py'):
    print(file)


