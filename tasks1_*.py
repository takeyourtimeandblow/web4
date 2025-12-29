from pprint import pprint

from db_session import create_session, global_init
from models.department import Department
from models.jobs import Jobs
from models.user import User

db = input()
global_init(db)
session = create_session()

task_no = 3
# task 1.4
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
for user in session.query(User).filter(User.address == "module_1"):
    print(user)

# task 1.5
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
for user in session.query(User).filter(
    User.address == "module_1",
    ~User.speciality.contains("engineer"),
    ~User.position.contains("engineer"),
):
    print(user.id)

# task 1.6
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
for user in session.query(User).filter(User.age < 18):
    print(f"{user.surname} {user.name} {user.age}")

# task 1.7
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
for user in session.query(User).filter(
    (User.position.contains("chief")) | (User.position.contains("middle"))
):
    print(user)

# task 1.8
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
for job in session.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == False):
    print(job)

# task 1.9
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
jobs = session.query(Jobs).all()
max_team = max(len(j.collaborators.split(",")) for j in jobs)

leaders = set()
for job in jobs:
    if len(job.collaborators.split(",")) == max_team:
        leaders.add(job.leader)

for leader in leaders:
    print(leader.surname, leader.name)

# task 1.10
print("=" * 5, "task1." + str(task_no := task_no + 1), "=" * 5)
users = session.query(User).filter(User.address == "module_1", User.age < 21)

for user in users:
    user.address = "module_3"
    print(user)

session.commit()

print("=" * 5, "task1." + str(task_no := task_no + 2), "=" * 5)
dept = session.query(Department).filter(Department.id == 1).first()
member_ids = map(int, dept.members.split(","))

for user in session.query(User).filter(User.id.in_(member_ids)):
    total = sum(job.work_size for job in user.jobs)
    if total > 25:
        print(user.surname, user.name)
