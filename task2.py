class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # Множина призначених предметів


def create_schedule(subjects, teachers):
    if not subjects or not teachers:
        return None

    remaining_subjects = subjects.copy()
    selected_teachers = []

    while remaining_subjects:
        best_teacher = None
        max_subjects = 0

        for teacher in teachers:
            can_teach = teacher.can_teach_subjects.intersection(remaining_subjects)
            subjects_count = len(can_teach)

            if subjects_count > max_subjects or \
                    (subjects_count == max_subjects and best_teacher and teacher.age < best_teacher.age):
                best_teacher = teacher
                max_subjects = subjects_count

        if not best_teacher or max_subjects == 0:
            return None

        assignable_subjects = best_teacher.can_teach_subjects.intersection(remaining_subjects)
        best_teacher.assigned_subjects = assignable_subjects
        remaining_subjects -= assignable_subjects

        if best_teacher not in selected_teachers:
            selected_teachers.append(best_teacher)

    return selected_teachers


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")