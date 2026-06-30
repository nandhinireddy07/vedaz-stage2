import json
from rapidfuzz import fuzz
from sklearn.model_selection import train_test_split

# Path to the JSONL file
file_path = "generated_chats.jsonl"

# Empty list to store chats
chats = []

with open(file_path, "r", encoding="utf-8") as file:
    # Read one line at a time
    for line in file:
        # Convert JSON text into Python dictionary
        chat = json.loads(line)

        # Store it in the list
        chats.append(chat)

# Print total number of chats
print("Total chats:", len(chats))

def check_structure(chat):

    messages = chat["messages"]

    valid_roles = ["system", "user", "assistant"]

    for message in messages:

        if "role" not in message:
            return False

        if "content" not in message:
            return False

        if message["role"] not in valid_roles:
            return False

    return True

def count_words(chat):

    total_words = 0

    messages = chat["messages"]

    for message in messages:

        text = message["content"]

        words = text.split()

        total_words += len(words)

    return total_words

def get_user_message(chat):

    for message in chat["messages"]:

        if message["role"] == "user":
            return message["content"]

    return ""


def check_safety(chat):

    unsafe_words = [
        "death",
        "die",
        "guaranteed",
        "100%",
        "cancer",
        "incurable",
        "you will definitely",
        "black magic"
    ]

    for message in chat["messages"]:

        if message["role"] == "assistant":

            text = message["content"].lower()

            for word in unsafe_words:

                if word in text:
                    return False

    return True

print("\nChecking for duplicate chats...\n")

for i in range(len(chats)):

    for j in range(i + 1, len(chats)):

        chat1 = get_user_message(chats[i])
        chat2 = get_user_message(chats[j])

        similarity = fuzz.ratio(chat1, chat2)

        if similarity > 90:
            print(f"⚠️ Chat {i+1} and Chat {j+1} are similar ({similarity:.2f}%)")

for i, chat in enumerate(chats):

    if check_structure(chat) and check_safety(chat):

        word_count = count_words(chat)

        print(f"✅ Chat {i+1}")
        print(f"Words: {word_count}")

    else:

        print(f"❌ Chat {i+1} : Invalid")

# Split dataset into training and test sets
train_chats, test_chats = train_test_split(
    chats,
    test_size=0.2,
    random_state=42
)

print("\nDataset Split")
print(f"Training chats: {len(train_chats)}")
print(f"Test chats: {len(test_chats)}")