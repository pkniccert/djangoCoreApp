from faker import Faker
import random
from .models import Department, Student, StudentID

fake = Faker()

def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            depart_objs = Department.objects.all()
            if not depart_objs.exists():
                print("No departments found in the database.")
                return

            random_index = random.randint(0, len(depart_objs) - 1)
            department = depart_objs[random_index]

            student_id = f"STU-0{random.randint(100, 999)}"
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()  # Use fake.phone_number() to generate a phone number
            age = random.randint(20, 30)
            address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,  # Assuming you want to link to the StudentID instance
                name=name,
                email=email,
                phone=phone,
                age=age,
                address=address,
            )

    except Exception as e:
        print(f"An error occurred: {e}")
