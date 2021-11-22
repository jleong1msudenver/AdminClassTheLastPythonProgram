# AdminPrivs.py
from admin import Admin

privileges = ["can add post", "can delete post", "can modify post of user", "can ban user",
              "can add user", "can delete user", "can reset user", "can modify user profile"]

it_department_lead = Admin(
    "Josh", "Leong", "mail@email.com", 35, "323-333-3344", privileges)

print("IT Department Lead has permissions:",
      it_department_lead.show_privileges())

developers_team_lead = Admin(
    "Jim", "Jefferson", "email@mail.com", 36, '303-333-3444', privileges)

print("Developers Team Lead has permissions:",
      developers_team_lead.show_privileges())
