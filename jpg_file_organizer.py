import os
import shutil

def move_jpg_files():
    print("=" * 45)
    print("   📁 JPG FILE ORGANIZER - TASK AUTOMATION")
    print("=" * 45)

    # Step 1: Get source folder from user
    source_folder = input("\nEnter the path of the source folder\n(or press Enter to use current folder): ").strip()

    if source_folder == "":
        source_folder = os.getcwd()

    # Validate source folder
    if not os.path.exists(source_folder):
        print(f"\n❌ Folder not found: '{source_folder}'")
        return

    print(f"\n📂 Source folder: {source_folder}")

    # Step 2: Define destination folder
    destination_folder = os.path.join(source_folder, "JPG_Images")

    # Step 3: Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"✅ Created destination folder: 'JPG_Images'")
    else:
        print(f"📁 Destination folder already exists: 'JPG_Images'")

    # Step 4: Find all .jpg files in source folder
    jpg_files = [
        f for f in os.listdir(source_folder)
        if f.lower().endswith(".jpg") and os.path.isfile(os.path.join(source_folder, f))
    ]

    # Step 5: Check if any .jpg files found
    if not jpg_files:
        print("\n⚠️  No .jpg files found in the source folder.")
        return

    print(f"\n🔍 Found {len(jpg_files)} .jpg file(s):\n")

    # Step 6: Move each .jpg file
    moved = 0
    skipped = 0

    for filename in jpg_files:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Skip if file already exists in destination
        if os.path.exists(destination_path):
            print(f"  ⚠️  Skipped (already exists): {filename}")
            skipped += 1
        else:
            shutil.move(source_path, destination_path)
            print(f"  ✅ Moved: {filename}")
            moved += 1

    # Step 7: Display summary
    print("\n" + "=" * 45)
    print("           📊 SUMMARY")
    print("=" * 45)
    print(f"  Total .jpg files found : {len(jpg_files)}")
    print(f"  Successfully moved     : {moved}")
    print(f"  Skipped (duplicates)   : {skipped}")
    print(f"  Destination folder     : JPG_Images/")
    print("=" * 45)

    if moved > 0:
        print(f"\n🎉 Done! {moved} file(s) moved to 'JPG_Images' folder.")
    else:
        print("\n📁 No new files were moved.")

def main():
    move_jpg_files()

    again = input("\nRun again on another folder? (yes / no): ").lower().strip()
    if again == "yes":
        main()
    else:
        print("\nThank you for using JPG File Organizer! Goodbye 👋")

if __name__ == "__main__":
    main()
