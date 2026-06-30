import psycopg2
from config import DB_CONFIG


def get_connection():
    """
    Creates and returns a PostgreSQL connection.
    """

    try:
        connection = psycopg2.connect(**DB_CONFIG)

        print("✅ Connected to PostgreSQL!")

        return connection

    except Exception as e:
        print("Database Connection Error:")
        print(e)

        return None
    
def save_candidate(candidate):

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        INSERT INTO candidates
        (name, email, phone, degree, institution, field, skills)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (email)
        DO NOTHING;
        """

        education = candidate["education"]

        skills = ", ".join(candidate["skills"])

        values = (
            candidate["name"],
            candidate["email"],
            candidate["phone"],
            education["degree"],
            education["institution"],
            education["field"],
            skills
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        print("✅ Candidate saved successfully!")

def get_all_candidates():
    """
    Fetches all candidates from the database.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    query = """
    SELECT name, degree, email, phone, skills
    FROM candidates
    ORDER BY id;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    candidates = []

    for row in rows:

        candidate = {
            "name": row[0],
            "degree": row[1],
            "email": row[2],
            "phone": row[3],
            "skills": row[4]
        }

        candidates.append(candidate)

    cursor.close()
    connection.close()

    return candidates
    
if __name__ == "__main__":

    conn = get_connection()

    if conn:
        conn.close()
        print("Connection Closed.")