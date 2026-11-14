
"""A simple pet shelter registration and adoption system."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute("""
CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    species TEXT,
    age INTEGER,
    adopted INTEGER
)
""")


def register_pet(name, species, age, tags=None):
    """Register a pet and return its updated tags."""
    if tags is None:
        tags = []

    conn.execute(
        """
        INSERT INTO pets (name, species, age, adopted)
        VALUES (?, ?, ?, 0)
        """,
        (name, species, age),
    )

    tags.append(species)
    return tags


def adopt(pet_id, adoption_count):
    """Mark a pet as adopted and return the updated count."""
    conn.execute(
        "UPDATE pets SET adopted = 1 WHERE id = ?",
        (pet_id,),
    )
    return adoption_count + 1


def adoption_code():
    """Generate a pet adoption code."""
    return f"PET-{secrets.randbelow(9000) + 1000}"


def oldest_available():
    """Return the name of the oldest available pet."""
    row = conn.execute("""
        SELECT name, age
        FROM pets
        WHERE adopted = 0
        ORDER BY age DESC
    """).fetchone()

    if row is None:
        return None

    return row[0]


def clear_unadopted():
    """Remove all pets that have not been adopted."""
    conn.execute("DELETE FROM pets WHERE adopted = 0")


def shelter_status(adoption_count):
    """Return the current shelter status."""
    if adoption_count > 0:
        return "active"
    return "quiet"


def main():
    """Run the pet shelter example."""
    adoption_count = 0

    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)

    adoption_count = adopt(1, adoption_count)

    print(
        oldest_available(),
        adoption_code(),
        shelter_status(adoption_count),
    )

    clear_unadopted()


if __name__ == "__main__":
    main()
