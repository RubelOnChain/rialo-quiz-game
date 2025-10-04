# Rialo Quiz Game 🎮
# Made for Rialo Community

print("🎉 Welcome to the Rialo Quiz Game! 🎉")
print("Answer the questions and earn points.\n")

score = 0

# Question list
questions = [
    {
        "q": "Q1: Which role in Rialo is given for quality development?",
        "options": ["a) Builder", "b) Raider", "c) Memer", "d) Helper"],
        "answer": "a"
    },
    {
        "q": "Q2: What is the main focus of the Rialo community?",
        "options": ["a) Gaming", "b) Development & Innovation", "c) Random Chat", "d) Music"],
        "answer": "b"
    },
    {
        "q": "Q3: What type of content is shared in the meme channel?",
        "options": ["a) Rules", "b) Jokes & Memes", "c) Tools", "d) Quizzes"],
        "answer": "b"
    },
    {
        "q": "Q4: How can you get the Builder role?",
        "options": ["a) Just stay active", "b) Create quality tools or games", "c) Random chatting", "d) Post memes only"],
        "answer": "b"
    }
]

# Run quiz
for q in questions:
    print("\n" + q["q"])
    for opt in q["options"]:
        print(opt)
    user_ans = input("👉 Your answer (a/b/c/d): ").lower()

    if user_ans == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer was:", q["answer"])

# Final score
print("\n🏆 Quiz Finished! You scored", score, "out of", len(questions))
if score == len(questions):
    print("🔥 Perfect! You are a true Rialo Builder!")
elif score >= 2:
    print("👍 Good job! Keep contributing to Rialo.")
else:
    print("😅 Better luck next time!")
