spamWordsFile = open("spamWords.txt", "r", encoding="utf-8")
spamWords = spamWordsFile.read().split("\n")
spamWordsFile.close()

file = open("emails.txt", "r", encoding="utf-8")
emails = file.read()
file.close()

emailList = emails.split("\n\n")

spamFile = open("Spam.txt", "w", encoding="utf-8")
notSpamFile = open("NotSpam.txt", "w", encoding="utf-8")
spamSendersFile = open("spamSenders.txt", "w", encoding="utf-8")

for email in emailList:
    emailLower = email.lower()
    isSpam = False

    for word in spamWords:
        if word != "" and word.lower() in emailLower:
            isSpam = True

    if isSpam:
        spamFile.write(email + "\n\n")

        lines = email.split("\n")

        for line in lines:
            if line.startswith("from:"):
                sender = line.replace("from:", "").strip()
                spamSendersFile.write(sender + "\n")
    else:
        notSpamFile.write(email + "\n\n")

spamFile.close()
notSpamFile.close()
spamSendersFile.close()

print("Проверка писем завершена!")
print("Созданы файлы: Spam.txt, NotSpam.txt, spamSenders.txt")

