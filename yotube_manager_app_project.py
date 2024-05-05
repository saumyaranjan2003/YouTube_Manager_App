import json

def load_data():
    """
    Load data from the 'YouTube.txt' file if it exists.
    If the file doesn't exist, return an empty list.
    """
    try:
        with open('YouTube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    """
    Save the list of videos to the 'YouTube.txt' file.
    """
    with open('YouTube.txt', 'w') as file:
        json.dump(videos, file)
    print("File updated successfully.")

def list_all_videos(videos):
    """
    Print all the videos in a tabular format.
    """
    print("\n")
    print("*" * 70)
    print("| {:<5} | {:<30} | {:<15} |".format("Index", "Name", "Duration"))
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print("| {:<5} | {:<30} | {:<15} |".format(index, video['name'], video['time']))
        print("-" * 70)
    print("*" * 70)
    print("\n")

def add_a_video(videos):
    """
    Add a new video to the list of videos.
    """
    name = input('Enter Video Name: ')
    time = input('Enter Video Time: ')
    videos.append({'name': name, "time": time})
    save_data_helper(videos)

def update_a_video(videos):
    """
    Update the details of an existing video.
    """
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, "time": time}
        save_data_helper(videos)
        print("Video updated successfully.")
    else:
        print("Invalid Index Selected")

def delete_a_video(videos):
    """
    Delete a video from the list.
    """
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully.")
    else:
        print("Invalid Video index selected")

def main():
    """
    Main function to manage the YouTube manager app.
    """
    videos = load_data()
    while True:
        print("\n YouTube Manager | Choose an Input ")
        print("1. List all Favorite Videos ")
        print("2. Add a YouTube Video ")
        print("3. Update a YouTube Video Details ")
        print("4. Delete a YouTube Video ") 
        print("5. Exit the App ") 
        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_a_video(videos)
            case '3':
                update_a_video(videos)
            case '4':
                delete_a_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":  
    main()
