import os # helps you create folders and navigate the file system.
from datetime import datetime

def create_folders():
    """Creates the following folder structure:
    - data
        - bronze
        - silver
        - gold
        - archive
    - logs
    - src
    - database
    """
    folders = ["data",
               "data/bronze",
               "data/silver", 
               "data/gold", 
               "data/archive", 
               "logs", 
               "src", 
               "database"
               ]
    
    for folder in folders:
        os.makedirs(folders, exist_ok= True)
        print(f"[OK] Folder ready: {folder}")
    
def show_structure():
    """Prints folder strucutre
    """    
    for root, dirs, files in os.walk("."):
        print(root)
        for d in dirs:
            print(f"  ┗ {d}/")
            
def main():
    """Creates the following folder structure and prints corresponding informations:
    - data
        - bronze
        - silver
        - gold
        - archive
    - logs
    - src
    - database
    """
    print("Starting project setup...")
    print(f"Time: {datetime.now()}")
    create_folders()
    print("\nProject structure:")
    show_structure()
    print("\nSetup completed successfully")
    
if __name__ == "__main__":
    main()