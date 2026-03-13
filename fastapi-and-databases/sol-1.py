from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, insert, select, update, delete
)

engine = create_engine("sqlite:///student.db", echo=True)
metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
    Column("city", String)
)

metadata.create_all(engine)

with engine.connect() as conn:

    conn.execute(insert(students), [
        {"name": "Rahul", "age": 22, "city": "Mumbai"},
        {"name": "Amit", "age": 19, "city": "Delhi"},
        {"name": "Neha", "age": 25, "city": "Pune"}
    ])
    conn.commit()

    print("\nAfter Insert:")
    for row in conn.execute(select(students)):
        print(row)

    conn.execute(
        update(students)
        .where(students.c.name == "Rahul")
        .values(city="Bangalore")
    )
    conn.commit()

    print("After Update:")
    for row in conn.execute(select(students)):
        print(row)

    conn.execute(delete(students).where(students.c.age < 20))
    conn.commit()

    print("After Delete:")
    for row in conn.execute(select(students)):
        print(row)
