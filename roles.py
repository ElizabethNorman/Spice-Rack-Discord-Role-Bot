"""
Roles contains the Role class and the Role objects to be used to assign roles to people
Elizabeth Norman, August 7th, 2022, @spicedboi
"""


class Role:
    # A Simple class that contains the relevant data needed for each role
    def __init__(self, role_description, discord_id, emoji):
        self.role_description = role_description
        self.discord_id = discord_id
        self.emoji = emoji


# the roles are hardcoded and placed into an array.

eng = Role("300: Software Engineering", ROLE_ID_GOES_HERE, '🥰')
ops = Role("321: Operating Systems", ROLE_ID_GOES_HERE, '🤯')
comp = Role("340: Theory of Computation", ROLE_ID_GOES_HERE, '⛰')
mang = Role("351: Management Information Systems", ROLE_ID_GOES_HERE, '😴')
func = Role("370: Functional and Logic Programming", ROLE_ID_GOES_HERE, '😵')
data = Role("424: Advanced Databases", ROLE_ID_GOES_HERE, '💿')
risk = Role("499: Risk Management", ROLE_ID_GOES_HERE, '🩹')
math = Role("499: Mathematics of Machine Learning", ROLE_ID_GOES_HERE, '🤖')

roles = [eng, ops, comp, mang, func, data, risk, math]
