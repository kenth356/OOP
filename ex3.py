grade = int(input("\nEnter your Grade: "))

if grade >= 75 and grade < 100:
    print("\nPassed!")
elif grade == 100:
    print("\nPerfect!")
else:
    print("\nFailed")