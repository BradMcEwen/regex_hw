# ============= Question 1 ==================
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9._%+-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)